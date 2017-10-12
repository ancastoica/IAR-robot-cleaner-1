from emulator import Emulator
from state import State
from robot import Robot
from random import randrange
from cell import Cell
import numpy as np
import itertools
import api


class DP:

    def __init__(self):
        self.states = []  # all possible states
        self.values = []
        self.threshold = 0.01  # The threshold used to stop the interations

    """
    generate all the possible states
    """

    def generate_all_states(self):
        for battery in range(0, 3):
            for robot_x in range(api.MAPSIZE):
                for robot_y in range(api.MAPSIZE):
                    for robot_orientation in range(0, 4):
                        for basex in range(api.MAPSIZE):
                            for basey in range(api.MAPSIZE):
                                self.generate_all_map(battery, robot_x, robot_y, robot_orientation, basex, basey)

    """
    Generate a map using the given parameters
    """

    def generate_all_map(self, battery, robot_x, robot_y, robot_orientation, base_x, base_y):
        mapp = api.initmap(base_x, base_y)
        all_maps = [np.reshape(np.array(i), (api.MAPSIZE, api.MAPSIZE)) for i in itertools.product([0, 1], repeat=api.MAPSIZE * api.MAPSIZE)]
        abs_battery = 100

        if battery == 0:
            abs_battery = 0
        elif battery == 1:
            abs_battery = randrange(1, 10)
        elif battery == 2:
            abs_battery = randrange(11, 100)

        robot = Robot(robot_x, robot_y, api.MAPSIZE, api.MAPSIZE, robot_orientation, abs_battery)

        for maps_ind in range(len(all_maps)):
            for x in range(api.MAPSIZE):
                for y in range(api.MAPSIZE):
                    if x == base_x and y == base_y:
                        mapp[x][y] = Cell(x, y, 0, 1)
                    else:
                        mapp[x][y] = Cell(x, y, all_maps[maps_ind][x][y], 0)
            if all_maps[maps_ind][base_x][base_y] == 0:
                self.states.append(State(robot, mapp, (base_x, base_y)))



    """
    Get the infinite norm of the difference of two vectors
    """

    def get_infinite_norme(self, values, values_prime):
        maxvalue = 0.0
        temp = 0.0
        for i in range(len(values)):
            temp = abs(values[i] - values_prime[i])
            if temp > maxvalue:
                maxvalue = temp
        return maxvalue


    """
    Return the value function of a given state
    """

    def get_value_function(self, emulator, state_ind, values_prime):
        rewards = [0.0 for i in range(len(api.ACTIONS))]
        newstates = [[0.0, 0.0] for i in range(len(api.ACTIONS))]
        probabilities = [0.0 for i in range(len(api.ACTIONS))]
        q_values = [0.0 for i in range(len(api.ACTIONS))]

        # Try each and every one of the possible actions
        for action_ind in range(len(api.ACTIONS)):
            # Get the rewards, states, probabilities as lists
            rewards[action_ind], newstates[action_ind], probabilities[action_ind] = emulator.simulate(self.states[state_ind], api.ACTIONS[action_ind])
            # Compute Q value
            q_values[action_ind] = rewards[action_ind]

            if type(newstates[action_ind]) == list:
                for possible_action in range(len(newstates[action_ind])):
                    possible_ind = self.state_exists(newstates[action_ind][possible_action])
                    q_values[action_ind] += api.DISCOUNTED_FACTOR * probabilities[action_ind] * values_prime[possible_ind]
            else:
                q_values[action_ind] += api.DISCOUNTED_FACTOR * probabilities[action_ind] * values_prime[self.state_exists(newstates[action_ind])]

        return max(q_values)

    def state_exists(self, state):
        index = 0
        while index < len(self.states):
            if state == self.states[index]:
                return index
            index += 1
        return -1

    def run(self):
        # Initialization of the simulation
        self.generate_all_states()
        print(len(self.states))
        self.values = [0.0 for i in range(len(self.states))]
        values_prime = [0.0 for i in range(len(self.states))]

        emulator = Emulator("DP")

        while True:
            # Update the values at t-1 according to the values at t
            values_prime = self.values[:]
            # Go through all the states
            for state_ind in range(len(self.states)):

                # Update the new maximum value
                self.values[state_ind] = self.get_value_function(emulator, state_ind, values_prime)

            # If the threshold is bigger than the difference between Vs and their predecessors, then we consider the algorithm as successful
            if self.get_infinite_norme(self.values, values_prime) < self.threshold:
                break

        s0_index = self.state_exists(api.INITIAL_STATE)

        return self.values[s0_index]
