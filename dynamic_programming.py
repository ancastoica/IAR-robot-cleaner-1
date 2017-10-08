from emulator import Emulator
from state import State
from robot import Robot
from cell import Cell
from random import randrange
import api


class DP:
    def __init__(self):
        self.states = []
        self.mapsize = 3  # Number of cells knowing that the map is a square

    """
        Creates a 3x3 map with random dirtiness state
        """

    def randommap(self, basex, basey):
        mapp = [[Cell(0, 0) for j in range(self.mapsize)] for i in range(self.mapsize)]

        for i in range(self.mapsize):
            for j in range(self.mapsize):
                if i == basex and j == basey:
                    mapp[i][j] = Cell(i, j, randrange(2), 1)
                else:
                    mapp[i][j] = Cell(i, j, randrange(2))
        return mapp

    def generate_all_states(self):
        for battery in range(0, 3):
            for robot_x in range(self.mapsize):
                for robot_y in range(self.mapsize):
                    for robot_orientation in range (0, 4):
                        for basex in range(self.mapsize):
                            for basey in range(self.mapsize):
                                self.generate_all_map(battery, robot_x, robot_y, robot_orientation, basex, basey)

    def generate_all_map(self, battery, robot_x, robot_y, robot_orientation, base_x, base_y):
        mapp = self.randommap(base_x, base_y)

        abs_battery = 100
        if battery == 0:
            abs_battery = 0
        elif battery == 1:
            abs_battery = randrange(1, 10)
        elif battery == 2:
            abs_battery = randrange(11, 100)

        robot = Robot(robot_x, robot_y, self.mapsize, self.mapsize, robot_orientation, abs_battery)
        self.states.append(State(robot, mapp, (base_x, base_y)))

