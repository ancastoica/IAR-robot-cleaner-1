from emulator import Emulator
import random
import api
import copy


class QL:
    emulator = Emulator("MC")
    epsilon = 0.2
    alpha = 0.1
    gamma = 0.99
    Q_function = {}

    def argmax_q_function(self, state):
        """
        Calculate argmax(a) of Q(s, a)
        :return: a ( the action that maximizez Q(s,a) ), max_q (the maximal value)
        """
        a = api.ACTIONS[random.randrange(len(api.ACTIONS))]
        if (state, a) not in self.Q_function.keys():
            self.Q_function[(state, a)] = 0
        max_q = self.Q_function[(state, a)]
        for action in api.ACTIONS:
            if (state, action) not in self.Q_function.keys():
                self.Q_function[(state, action)] = 0
            if self.Q_function[(state, action)] > max_q:
                max_q = self.Q_function[(state, action)]
                a = action
        return a, max_q

    def run(self, limit):
        """
        Run Q-Learning algorithm
        :param limit: when to stop algorithm / episode length
        :return: max Q(s0, a)
        """
        i = 0
        # self.Q_function = {}

        s = copy.deepcopy(api.INITIAL_STATE)
        id_s = s.to_string()

        # epsilon-greedy choice of a0
        dice = random.uniform(0, 1)
        if dice > self.epsilon:
            a = self.argmax_q_function(id_s)[0]
        else:
            a = api.ACTIONS[random.randrange(len(api.ACTIONS))]

        while i < limit:
            i += 1
            if s.robot.battery <= 0 or s.is_final_state():
                break
            r = self.emulator.simulate(s, a)[0]
            s_prime = copy.deepcopy(self.emulator.simulate(s, a)[1])

            # epsilon-greedy choice of a_prime
            dice = random.uniform(0, 1)
            if dice > self.epsilon:
                (a_prime, maxQ) = self.argmax_q_function(s_prime)
            else:
                a_prime = api.ACTIONS[random.randrange(len(api.ACTIONS))]
                if (id_s, a_prime) in self.Q_function.keys():
                    maxQ = self.argmax_q_function(s_prime)[1]
                else:
                    maxQ = 0

            if (id_s, a) not in self.Q_function.keys():
                self.Q_function[(id_s, a)] = 0

            delta = r + self.gamma * maxQ - self.Q_function[id_s, a]
            self.Q_function[id_s, a] = self.Q_function[id_s, a] + self.alpha * delta

            a = copy.deepcopy(a_prime)
            s = copy.deepcopy(s_prime)
            id_s = s.to_string()
        return self.argmax_q_function(api.INITIAL_STATE.to_string())[1]
