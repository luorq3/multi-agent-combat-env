import os
# os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# Exporting envs:
from multi_agent_combat_env.envs.fight_env_rgb import FightEnvRGB

from gym import make

from gym.envs.registration import register

register(
    id="Fight-rgb-v0",
    entry_point="multi_agent_combat_env:FightEnvRGB"
)

__all__ = [
    make.__name__,
    FightEnvRGB.__name__
]
