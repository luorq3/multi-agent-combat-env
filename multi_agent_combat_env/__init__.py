import os
# os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# Exporting envs:
from multi_agent_combat_env.envs.multi_agent_combat_env_rgb import MultiAgentCombatEnvRGB

from gym import make

from gym.envs.registration import register

register(
    id="MultiAgentCombat-rgb-v0",
    entry_point="multi_agent_combat_env:MultiAgentCombatEnvRGB"
)

__all__ = [
    make.__name__,
    MultiAgentCombatEnvRGB.__name__
]
