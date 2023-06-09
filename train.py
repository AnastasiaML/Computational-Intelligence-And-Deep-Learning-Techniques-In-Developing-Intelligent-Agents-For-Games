import gym 
from stable_baselines3.common.vec_env import DummyVecEnv 
from stable_baselines3.common.monitor import Monitor 
from stable_baselines3 import PPO, A2C, DQN 
from sb3_contrib import QRDQN 
from torch.nn import Sigmoid, Softplus, Tanh, Softmax, LogSigmoid 
from torch.optim import RMSprop, Adamax, SGD, ASGD, AdamW, Adadelta, Rprop, Adam 
import numpy as np 
import matplotlib.pyplot as plt 
import time 
import pandas as pd 
import torch as th

# Function for evaluation
def evaluate(model, num_episodes=100):
    """
    Evaluate a RL agent
    :param model: (BaseRLModel object) the RL Agent
    :param num_episodes: (int) number of episodes to evaluate it
    :return: (array) rewards of each episode
    """
    # This function will only work for a single Environment
    env = model.get_env()
    all_episode_rewards = []
    print("Num episodes:", num_episodes)
    for i in range(num_episodes):
        episode_rewards = []
        done = False
        obs = env.reset()
        while not done:
            # _states are only useful when using LSTM policies
            action, _states = model.predict(obs)
            # here, action, rewards and dones are arrays
            # because we are using vectorized env
            obs, reward, done, info = env.step(action)
            episode_rewards.append(reward)
        all_episode_rewards.append(sum(episode_rewards))
        print("Episode:", i+1,",reward:", float(all_episode_rewards[i]))
    mean_episode_reward = np.mean(all_episode_rewards)
    print("Mean reward:", mean_episode_reward)
    return all_episode_rewards

# Create environment
env = gym.make('SpaceInvaders-ram-v0')

# Wrap environment
env = Monitor(env)

# Vectorize environment
env = DummyVecEnv([lambda: env])

# Define the model
model = QRDQN("MlpPolicy", env, verbose=1, tensorboard_log='logs/SpaceInvaders/DQN/QR/')

# Train the agent
t0= time.time() 
model.learn(total_timesteps=50000000) 
seconds = time.time() - t0 
print("done, took ", seconds, "seconds.")

# Save the agent
path = '/home/panastasic/Desktop/Py/Weights/SpaceInvaders/DQN/QR/1/1.h5f'
model.save(path)

# Delete the model
#del model 

# Load the trained agent
#model = PPO.load(path, env=env)

# Evaluate the agent
test_reward = evaluate(model, 8000)

# Take rewards
test_reward = pd.DataFrame(test_reward)

# Create smoothed graphs
plt.plot(test_reward, 'lightblue', test_reward.rolling(5).mean(), 'b')
plt.xlabel('episodes') 
plt.ylabel('scores') 
plt.title('test/episode_reward', loc='left') 
plt.show()

# Close the environment
env.close()
