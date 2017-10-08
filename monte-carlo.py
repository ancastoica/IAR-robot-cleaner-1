from cell import Cell
from state import State
from robot import Robot
from emulator import Emulator
from random import randrange

class Monte_Carlo:

    def __init__(self):
        self.emulator = Emulator()
        self.size = self.emulator.mapsize

    def random_state(self):
        self.emulator.createmap()
        robot = Robot(randrange(self.size),randrange(self.size))
        return State(robot, self.emulator.map)

    def generate_episode(self, n):
        episode = []
        for i in range(1, n):
            state = self.random_state()
            action = self.actions[randrange(4)]
            reward = self.emulator.simulate(state, action)
            episode.append((state, action, reward))
        return episode

    def mc_run(self, limit, reward, state):
        i = 0
        Q = {}
        Returns = []
        while(i<limit):
            i += 1
            episode = self.generate_episode(3)
            for s in [e[0] for e in episode]:
                for a in [e[1] for e in episode]:
                    G = self.emulator.simulate(s, a)
                    Returns.append(G)
                    Q[(s, a)] = G
            for s in [e[0] for e in episode]:
                # π ← pi-greedy w.r.t Q0