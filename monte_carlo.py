from emulator import Emulator
from state import State
from robot import Robot
from cell import Cell
import numpy as np
import itertools
import random
import api


class MC:
    emulator = Emulator("MC")
    epsilon = 0.1
    alpha = 0.1
    gamma = 0.99
    Q_function = {}

    def all_states(self):
        """
        Generate all possible states
        :return: Dictionnary of all states with their unique id as key
        """
        all_s = {}
        all_maps = [np.reshape(np.array(i), (api.MAPSIZE, api.MAPSIZE)) for i in itertools.product([0, 1], repeat=api.MAPSIZE * api.MAPSIZE)]
        for basex in range(api.MAPSIZE):
            for basey in range(api.MAPSIZE):
                for m in all_maps:
                    mapp = [[Cell(0, 0) for j in range(api.MAPSIZE)] for i in range(api.MAPSIZE)]
                    for i in range(len(m)):
                        for j in range(len(m[i])):
                            if i == basex and j == basey:
                                mapp[i][j] = Cell(i, j, m[i][j], 1)
                            else:
                                mapp[i][j] = Cell(i, j, m[i][j])
                            for battery in range(80, 100):
                                for robot_x in range(api.MAPSIZE):
                                    for robot_y in range(api.MAPSIZE):
                                        for robot_orientation in range(0, 4):
                                            robot = Robot(robot_x, robot_y, api.MAPSIZE, api.MAPSIZE, robot_orientation, battery)
                                            state = State(robot, mapp, (basex, basey))
                                            id_state = state.to_string()
                                            all_s[id_state] = state
        return all_s

    def init_q_fuction(self):
        """
        Initialize Q(s,a) = 0 for all pairs (s,a)
        """
        all_s = self.all_states()
        for a in api.ACTIONS:
            for s in all_s.keys():
                self.Q_function[(s, a)] = 0

    def argmax_q_function(self, state):
        """
        Calculate argmax(a) of Q(s, a)
        :return: a ( the action that maximizez G(s,a) ), max_q (the maximal value)
        """
        a = api.ACTIONS[0]
        max_q = self.Q_function[(state, a)]
        for action in api.ACTIONS:
            if self.Q_function[(state, action)] > max_q:
                max_q = self.Q_function[(state, action)]
                a = action
        return a, max_q

    def generate_episode(self, length):
        """
        Generate an episode
        :param length: number of (s, a, r) sequences
        :return: list of (s, a, r) sequences
        """

        episode = []
        index_episode = 1

        # (s0, a0, r0) generation

        s = api.INITIAL_STATE
        id_s = s.to_string()

        # epsilon-greedy choice of a0

        dice = random.uniform(0, 1)
        if dice > self.epsilon:
            a = self.argmax_q_function(id_s)[0]
        else:
            a = api.ACTIONS[random.randrange(len(api.ACTIONS))]

        r = self.emulator.simulate(s, a)[0]
        episode.append([id_s, a, r])

        # Generation of the nex length-1 sequences

        while index_episode < length:
            id_s = ""
            index_episode += 1
            s = self.emulator.simulate(s, a)[1]
            id_s = s.to_string()

            # epsilon-greedy choice of a0

            dice = random.uniform(0, 1)
            if dice > self.epsilon:
                a = self.argmax_q_function(id_s)[0]
            else:
                a = api.ACTIONS[random.randrange(len(api.ACTIONS))]

            r = self.emulator.simulate(s, a)[0]
            episode.append([id_s, a, r])
        return episode

    def run(self, limit, T):
        """
        Run Monte Carlo algorithm
        :param limit: when to stop algorithm ( limit -> infinity)
        :param T: episodes length
        :return: max Q(s0, a)
        """
        i = 0
        G = {}
        self.init_q_fuction()

        while i < limit:
            i += 1
            episode = self.generate_episode(T)
            for t in range(0, T):
                G[t] = 0
                for k in range(t, T):
                    G[t] += pow(self.gamma, t-k) * episode[k][2]
                self.Q_function[(episode[t][0], episode[t][1])] = self.Q_function[(episode[t][0], episode[t][1])] + self.alpha * (G[t] - self.Q_function[(episode[t][0], episode[t][1])])
        return self.argmax_q_function(api.INITIAL_STATE.to_string())[1]
