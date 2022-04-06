from abc import ABC
from typing import Tuple, Any

import pygame
from pygame.rect import Rect


class SpriteBase(pygame.sprite.Sprite, ABC):

    def __init__(self,
                 screen_size: Tuple[int, int],
                 rect: Rect):
        super(SpriteBase, self).__init__()
        self.screen_size = screen_size
        self.rect = rect
        size = (self.rect.width, self.rect.height)
        self.max_rect = [limit_rect - size for size, limit_rect in zip(size, self.screen_size)]

    def update(self, *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError(f"Tried to call `{self.image.__class__}.update()`,"
                                  f" but it hasn't been implemented yet!")




