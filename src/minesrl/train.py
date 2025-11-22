from stable_baselines3 import PPO
env = ...

model = PPO("MipPolicy", env, verbose=1, learning_rate=0.0001)

print("Start Learning")
model.learn(total_timesteps=1_000_000)

model.save("mines_model_v0")
print("Model saved")