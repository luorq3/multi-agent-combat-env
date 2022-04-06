import fight_env_gym

from stable_baselines3 import A2C
from stable_baselines3.common.evaluation import evaluate_policy


if __name__ == "__main__":
    env = fight_env_gym.make("Fight-rgb-v0")

    model = A2C.load("saved_model", env=env)

    mean_reward, std_reward = evaluate_policy(model, model.get_env(), n_eval_episodes=10)

    obs = env.reset()
    for i in range(1000):
        action, _state = model.predict(obs, deterministic=True)
        obs, reward, done, info = env.step(action)
        env.render()
        if done:
            obs = env.reset()

