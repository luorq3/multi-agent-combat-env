from enum import IntEnum
from typing import Tuple

from multi_agent_combat_env.envs.sprites import Ship
from multi_agent_combat_env.envs.sprites import Fort
from multi_agent_combat_env.envs.utils import *


class GameLogic:

    def __init__(self, images, screen_size: Tuple[int, int]):
        self._screen_width = screen_size[0]
        self._screen_height = screen_size[1]

        self.ship = Ship(screen_size, Rect(*self._ship_init_position(), *ship_size))
        self.fort = Fort(screen_size, Rect(*self._fort_init_position(), *fort_size))

        self.fort_fire_speed = 6  # TODO: The value is inversely proportional to the fire_speed, to be perfected
        self.fort_fire_clock = 0

        # hit mask
        self.ship_mask = get_hitmask(images["ship"])
        self.fort_mask = get_hitmask(images["fort"])
        self.ship_missile_mask = get_hitmask(images["ship_missile"])
        self.fort_missile_mask = get_hitmask(images["fort_missile"])

    class Action(IntEnum):
        NOOP, UP, DOWN, LEFT, RIGHT, FIRE = 0, 1, 2, 3, 4, 5

    class Reward(IntEnum):
        # FIRE, HIT, BE_HIT, VICTORY, DEFEATED = 0, 1, -1, 3, -3
        FIRE, HIT, BE_HIT = 0, 1, -1

    def _ship_init_position(self, nums=1):
        if nums == 1:
            return self._screen_width // 2, self._screen_height - 100
        else:
            # TODO: multi ship position initialization
            return 0, 0

    def _fort_init_position(self, nums=1):
        if nums == 1:
            return self._screen_width // 2, 100
        else:
            # TODO: multi ship position initialization
            return 0, 0

    def update_state(self, action: int):
        alive = True
        reward = 0
        reward_list = []
        print(f"update_state start, reward:{reward}")

        if action in [1, 2, 3, 4]:
            self.ship.move(action)
        if action == 5:
            reward += self.Reward.FIRE
            reward_list.append(self.Reward.FIRE)
            self.ship.fire()

        # machine fort fire logic
        if self.fort_fire_clock % self.fort_fire_speed == 0:
            self.fort.update(*get_center_rect(self.ship.rect))
            self.fort.fire()
            self.fort_fire_clock = 0

        self.fort_fire_clock += 1

        # Collision check
        # Was Fort be hit
        for missile in self.ship.missile_group:
            collided = pixel_collision(self.fort.rect, missile.rect, self.fort_mask, self.ship_missile_mask)
            # collided = pixel_collision2(self.fort.rect, missile.rect)
            if collided:
                missile.kill()
                self.fort.hp -= 1
                reward += self.Reward.HIT
                reward_list.append(self.Reward.HIT)
            if self.fort.hp == 0:
                alive = False
                # reward_list.append(self.Reward.VICTORY)
                # reward += self.Reward.VICTORY
                break  # When victory, jump out of the loops to avoid calculating the wrong reward
        # Was Ship be hit
        for missile in self.fort.missile_group:
            collided = pixel_collision(self.ship.rect, missile.rect, self.ship_mask, self.fort_missile_mask)
            # collided = pixel_collision2(self.ship.rect, missile.rect)
            if collided:
                missile.kill()
                self.ship.hp -= 1
                reward += self.Reward.BE_HIT
                reward_list.append(self.Reward.BE_HIT)
            if self.ship.hp == 0:
                alive = False
                # reward += self.Reward.DEFEATED
                # reward_list.append(self.Reward.DEFEATED)
                break  # When failed, jump out of the loops to avoid calculating the wrong reward

        print(f"update_state end, reward:{reward}")
        print(f"reward list:{reward_list}")

        return reward, alive

