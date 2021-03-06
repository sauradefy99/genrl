from typing import Tuple

import gym
import numpy as np


class QLearning:
    """
    Q-Learning Algorithm

    Paper- https://link.springer.com/article/10.1007/BF00992698

    :param env: standard gym environment to train on
    :param epsilon: exploration coefficient
    :param gamma: discount factor
    :param lr: learning rate
    :type env: Gym environment
    :type epsilon: float
    :type gamma: float
    :type lr: float
    """

    def __init__(
        self, env: gym.Env, epsilon: float = 0.9, gamma: float = 0.95, lr: float = 0.01
    ):
        self.env = env
        self.epsilon = epsilon
        self.gamma = gamma
        self.lr = lr

        self.Q = np.zeros((self.env.observation_space.n, self.env.action_space.n))

    def get_action(self, state: np.ndarray, explore: bool = True) -> np.ndarray:
        """
        Epsilon greedy selection of epsilon in the explore phase

        :param state: Current state
        :param explore: Whether you are exploring or exploiting
        :type state: int, float, ...
        :type explore: bool
        :returns: Action based on the Q table
        :rtype: int, float, ...
        """
        if explore:
            if np.random.uniform() > self.epsilon:
                return self.env.action_space.sample()
        return np.argmax(self.Q[state, :])

    def update(self, transition: Tuple) -> None:
        """
        Update the Q table

        :param transition: step taken in the environment
        """
        state, action, reward, next_state = transition

        self.Q[state, action] += self.lr * (
            reward + self.gamma * np.max(self.Q[next_state, :]) - self.Q[state, action]
        )
