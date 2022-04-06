import math
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
        super(Fort, self).__init__(screen_size, rect)
        self.hp = hp
        self.angle = 0
        self.radian = 0
        self.missile_group = pygame.sprite.Group()

    def fire(self):
        missile = FortMissile(
            self.screen_size,
            Rect(*get_center_rect(self.rect), *fort_missile_size),
            self.radian)
        self.missile_group.add(missile)

    # TODO: angle over 90 degree and less than -90
    def update(self, target_x, target_y, *args: Any, **kwargs: Any) -> None:
        offset_x = target_x - self.rect.x
        offset_y = target_y - self.rect.y

        if offset_y != 0:
            self.radian = math.atan(offset_x / offset_y)
        else:
            sign = 1
            if offset_x < 0:
                sign *= -1
            self.radian = sign * math.pi / 2

        self.angle = self.radian * 180 / math.pi
