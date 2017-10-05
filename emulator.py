from random import randrange
from cell import Cell


class Emulator:
    def __init__(self):
        self.map = [[Cell(0, 0) for j in range(3)] for i in range(3)]  # The map matrices containing the cells
        self.algorithm = 0  # 0 for dynamic programming, 1 for MonteCarlo, 2 for Time Differentials
        # rewards and transition model under the idea of ((action reward + time reward), probability of success)
        self.empty_battery = {"go_forward_vacuuming": ((-100 + -1), 0.0),
                              "go_forward_no_vacuuming": ((-100 + -1), 0.0),
                              "rotate_left": ((-100 + -1), 0.0),
                              "rotate_right": ((-100 + -1), 0.0),
                              "vacuum": ((-100 + -1), 0.0)}
        self.critical_battery = {"go_forward_vacuuming": ((-3 + -1), 1.0),
                                 "go_forward_no_vacuuming": ((0 + -1), 1.0),
                                 "rotate_left": ((0 + -1), 1.0),
                                 "rotate_right": ((0 + -1), 1.0),
                                 "vacuum": ((-5 + -1), 1.0)}
        self.sufficient_battery = {"go_forward_vacuuming": ((0 + -1), 1.0),
                                   "go_forward_no_vacuuming": ((0 + -1), 1.0),
                                   "rotate_left": ((0 + -1), 1.0),
                                   "rotate_right": ((0 + -1), 1.0),
                                   "vacuum": ((0 + -1), 1.0)}
        self.front_wall = {"go_forward_vacuuming": (-10, 0.0),
                           "go_forward_no_vacuuming": (-10, 0.0),
                           "rotate_left": (10, 1.0),
                           "rotate_right": (10, 1.0),
                           "vacuum": (0, 1.0)}
        self.right_wall = {"go_forward_vacuuming": (0, 1.0),
                           "go_forward_no_vacuuming": (0, 1.0),
                           "rotate_left": (0, 1.0),
                           "rotate_right": (-10, 1.0),
                           "vacuum": (0, 1.0)}
        self.left_wall = {"go_forward_vacuuming": (0, 1.0),
                          "go_forward_no_vacuuming": (0, 1.0),
                          "rotate_left": (-10, 1.0),
                          "rotate_right": (0, 1.0),
                          "vacuum": (0, 1.0)}
        self.dirty_cell = {"go_forward_vacuuming": (40, 0.9),
                           "go_forward_no_vacuuming": (-40, 0.8),
                           "rotate_left": (0, 1.0),
                           "rotate_right": (0, 1.0),
                           "vacuum": (40, 1.0)}
        self.clean_cell = {"go_forward_vacuuming": (-10, 0.9),
                           "go_forward_no_vacuuming": (5, 0.9),
                           "rotate_left": (0, 1.0),
                           "rotate_right": (0, 1.0),
                           "vacuum": (-10, 1.0)}

    """
    Creates a 3x3 map with random dirtiness state
    """

    def createmap(self):
        nb = 0
        for i in range(3):
            for j in range(3):
                if nb == 0:
                    self.map[i][j] = Cell(i, j, randrange(2), 1)
                else:
                    self.map[i][j] = Cell(i, j, randrange(2))
                nb += 1
        self.printmap()

    """
    Prints the map in the terminal (h = homebase, x = dirty, o = clean)
    """

    def printmap(self):
        for i in range(3):
            line = ""
            for j in range(3):
                if self.map[i][j].home == 1:
                    line += "h"
                elif self.map[i][j].dirty == 1:
                    line += "x"
                elif self.map[i][j].dirty == 0:
                    line += "o"
            print(line)

    """
    Simulate the model according to the algorithm we're using
    """

    def simulate(self, state, action):
        reward = 0
        probability = 0.0
        newstate = state

        # Battery check
        if state.robot.battery == 0:
            reward += self.empty_battery.get(action)[0]
            probability *= self.empty_battery.get(action)[1]
        elif state.robot.battery <= 10:
            reward += self.critical_battery.get(action)[0]
            probability *= self.critical_battery.get(action)[1]
        elif state.robot.battery >= 10:
            reward += self.sufficient_battery.get(action)[0]
            probability *= self.sufficient_battery.get(action)[1]

        # Position check
        if state.robot.orientation == 0:
            if state.robot.x == 0:
                reward += self.left_wall.get(action)[0]
                probability *= self.left_wall.get(action)[1]
            if state.robot.y == 0:
                reward += self.front_wall.get(action)[0]
                probability *= self.front_wall.get(action)[1]
            if state.robot.x == self.mapsize - 1:
                reward += self.right_wall.get(action)[0]
                probability *= self.right_wall.get(action)[1]

        elif state.robot.orientation == 1:
            if state.robot.y == 0:
                reward += self.left_wall.get(action)[0]
                probability *= self.left_wall.get(action)[1]
            if state.robot.x == self.mapsize - 1:
                reward += self.front_wall.get(action)[0]
                probability *= self.front_wall.get(action)[1]
            if state.robot.y == self.mapsize - 1:
                reward += self.right_wall.get(action)[0]
                probability *= self.right_wall.get(action)[1]

        elif state.robot.orientation == 2:
            if state.robot.x == self.mapsize - 1:
                reward += self.left_wall.get(action)[0]
                probability *= self.left_wall.get(action)[1]
            if state.robot.y == self.mapsize - 1:
                reward += self.front_wall.get(action)[0]
                probability *= self.front_wall.get(action)[1]
            if state.robot.x == 0:
                reward += self.right_wall.get(action)[0]
                probability *= self.right_wall.get(action)[1]

        elif state.robot.orientation == 3:
            if state.robot.y == self.mapsize - 1:
                reward += self.left_wall.get(action)[0]
                probability *= self.left_wall.get(action)[1]
            if state.robot.x == 0:
                reward += self.front_wall.get(action)[0]
                probability *= self.front_wall.get(action)[1]
            if state.robot.y == 0:
                reward += self.right_wall.get(action)[0]
                probability *= self.right_wall.get(action)[1]

        # Dirtiness check
        if self.map[state.robot.x][state.robot.y].dirty == 0:
            reward += self.clean_cell.get(action)[0]
            probability *= self.clean_cell.get(action)[1]
        elif self.map[state.robot.x][state.robot.y].dirty == 1:
            reward += self.dirty_cell.get(action)[0]
            probability *= self.dirty_cell.get(action)[1]
        
        return newstate
