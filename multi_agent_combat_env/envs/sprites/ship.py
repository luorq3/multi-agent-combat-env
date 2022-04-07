from typing import Tuple
from multi_agent_combat_env.envs.sprites.base import SpriteBase, Movable
from multi_agent_combat_env.envs.sprites.ship_missile import ShipMissile
from multi_agent_combat_env.envs.utils import *

import pygame


class Ship(SpriteBase, Movable):

    def __init__(self,
                 screen_size: Tuple[int, int],
                 rect: Rect,
                 speed: int = 10,
                 hp: int = 5):
        SpriteBase.__init__(self, screen_size, rect, hp)
        Movable.__init__(self, self, speed)
        self.missile_group = pygame.sprite.Group()

    def fire(self):
        missile = ShipMissile(self.screen_size, Rect(*self.get_center_coord(), *ship_missile_size))
        self.missile_group.add(missile)

    # def handle(self, action):
    #     reward = 0
        # if action in [1, 2, 3, 4]:
        #     self.move(action)
        # if action == 5:
        #     self.fire()
        #
        # return 0


# s = Ship(pygame.surface.Surface((10, 10)), (50, 50), (10, 10), (0, 0))
