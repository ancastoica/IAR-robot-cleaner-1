from emulator import Emulator
from state import State
from robot import Robot
from cell import Cell
from random import randrange
import api
from policy import Policy


class DP:
    def __init__(self):
        self.states = []    # all possible states
        self.threshold = 0.01   # The threshold used to stop the interations
        self.values = []    # The values of the states at t-1

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
        mapp = api.randommap(base_x, base_y)

        abs_battery = 100
        if battery == 0:
            abs_battery = 0
        elif battery == 1:
            abs_battery = randrange(1, 10)
        elif battery == 2:
            abs_battery = randrange(11, 100)

        robot = Robot(robot_x, robot_y, api.MAPSIZE, api.MAPSIZE, robot_orientation, abs_battery)
        self.states.append(State(robot, mapp, (base_x, base_y)))

    """
    Get the infinite norm of the difference of two vectors
    """
    def get_infinite_norme(self, policy_matrix, second_values):
        max = 0
        temp = 0
        for i in range(len(policy_matrix)):
            temp = abs(policy_matrix[i][2] - second_values[i])
            if temp > max:
                max = temp
        return max

    def run(self):
        # Initialization of the simulation
        self.generate_all_states()
        self.values = [0 for i in range(len(self.states))]
        averageperf = []
        emulator = Emulator("dynamic_programming")
        policy = Policy()
        policy.init_policy(len(self.states))
        rewards = [0 for i in range(len(api.ACTIONS))]
        values = [0 for i in range(len(api.ACTIONS))]
        newstates = [0 for i in range(len(api.ACTIONS))]
        probabilities = [0 for i in range(len(api.ACTIONS))]

        while True:
            # Update the values at t-1 according to the values at t
            for k in range(len(policy.matrix)):
                self.values[k] = policy.matrix[k][2]

            # Go through all the states
            for i in range(len(self.states)):
                # Try each and every one of the possible actions
                for j in range(len(api.ACTIONS)):
                    # Get the rewards, states, probabilities as lists
                    rewards[j], newstates[j], probabilities[j] = emulator.simulate(self.states[i], api.ACTIONS[j])
                    # Compute V
                    values[j] = rewards[j] + api.DISCOUNTED_FACTOR * probabilities[j] * self.values[i]

                # Update the new maximum value and the attached action
                maximum_value = max(values)
                optimal_action = api.ACTIONS[rewards.index(maximum_value)]
                policy.insert_state_action(i, self.states[i], optimal_action, maximum_value)

            # If the threshold is bigger than the difference between Vs and their predecessors, then we consider the algorithm as successful
            if self.get_infinite_norme(policy.matrix, self.values) < self.threshold:
                average = 0
                for i in range(len(policy.matrix)):
                    average = average + policy.matrix[i][2]

                average = average / len(policy.matrix) * -1
                averageperf.append(average)
                break
            else:
                average = 0
                for i in range(len(policy.matrix)):
                    average = average + policy.matrix[i][2]

                average = average / len(policy.matrix) * -1
                averageperf.append(average)

        return averageperf

