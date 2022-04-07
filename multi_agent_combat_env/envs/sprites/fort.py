from typing import Tuple

import pygame

from multi_agent_combat_env.envs.sprites.base import SpriteBase
from multi_agent_combat_env.envs.sprites.fort_missile import FortMissile
from multi_agent_combat_env.envs.utils import *


class Fort(SpriteBase):

    def __init__(self,
                 screen_size: Tuple[int, int],
                 rect: Rect,
                 hp: int = 5):
        super(Fort, self).__init__(screen_size, rect, hp)
        self.angle = 0
        self.radian = 0
        self.missile_group = pygame.sprite.Group()

    def fire(self):
        missile = FortMissile(
            self.screen_size,
            Rect(*self.get_center_coord(), *fort_missile_size),
            self.radian)
        self.missile_group.add(missile)

    def update(self, target_x, target_y, *args: Any, **kwargs: Any) -> None:
        offset_x = target_x - self.rect.x
        offset_y = target_y - self.rect.y

        self.radian = math.atan2(offset_x, offset_y)

        self.angle = self.radian * 180 / math.pi

    def turn(self, action):
        pass
