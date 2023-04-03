# Computational Intelligence And Deep Learning Techniques In Developing Intelligent Agents For Games

The aim of this work is the analysis and study of computer intelligence and in-depth learning techniques in the development of intelligent gaming agents. In other words, the aim of this work is to methodologically compare the deep learning techniques of Stable Baselines3: PPO, A2C, DQN and QR-DQN, that have been proposed for games. For this reason, systematic experiments were performed on the Atari game environments of OpenAI Gym: MsPacman, SpaceInvaders and Q*bert, in order to compare deep reinforcing learning techniques in terms of their performance, training time and convergence time. In addition, more modern techniques such as learning spatial representations were used on the same environments to compare state representation learning methods in terms of f1 score and accuracy.

# Open AI Gym

OpenAI Gym is a toolkit that provides a wide variety of simulated environments (Atari games, board games, 2D and 3D physical simulations, and so on), so you can train agents, compare them, or develop new Machine Learning algorithms (Reinforcement Learning).

# Stable Baselines 3

Stable Baselines 3 (SB3) is a set of reliable implementations of reinforcement learning algorithms in PyTorch. W&B's SB3 integration will: Record metrics such as losses and episodic returns. Upload videos of agents playing the games. Save the trained model.

# Experiments

The experiments done are presented in this section.

The results of every algorithm in SpaceInvaders is the following:
![spaceinvaders-reward](https://user-images.githubusercontent.com/37047286/229602602-25053544-f86f-4fee-bc42-933a9b34a208.png)

The results of every algorithm in Q*Bert is the following:
![qbert-reward](https://user-images.githubusercontent.com/37047286/229602707-b562ec4c-2b13-47fc-b851-0beafe8aa610.png)

The results of every algorithm in MsPacman is the following:
![mspacman-reward](https://user-images.githubusercontent.com/37047286/229602744-99fe66c9-3855-4fec-9d0d-250b91b6fcdd.png)

# Results

In general, QR-DQN and PPO achieve better results than the rest of the reinforcement learning algorithms used in the specific experiments. Also, A2C and PPO are slower algorithms during training than DQN and QR-DQN, as they take almost twice as long as the others to complete the of their own experiments. Finally, regarding the difficulty level of the environments from the easiest are firstly Q*bert, then MsPacman and lastly SpaceInvaders, according to the experiments of this work, but all below of the corresponding human level.
