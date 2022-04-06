from typing import Tuple, Any

from pygame.rect import Rect
from multi_agent_combat_env.envs.sprites.base import SpriteBase


class Missile(SpriteBase):

    def __init__(self,
                 screen_size: Tuple[int, int],
                 rect: Rect,
                 speed: int = 5):
        super(Missile, self).__init__(screen_size, rect)
        self.speed = speed

    def update(self, *args: Any, **kwargs: Any) -> None:
        pass
