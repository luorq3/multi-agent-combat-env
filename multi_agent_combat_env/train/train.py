import fight_env_gym

from stable_baselines3 import A2C


if __name__ == "__main__":
    env = fight_env_gym.make("Fight-rgb-v0")

    model = A2C("CnnPolicy", env, create_eval_env=False, verbose=2)
    model.learn(total_timesteps=10000)
    model.save("saved_model")
