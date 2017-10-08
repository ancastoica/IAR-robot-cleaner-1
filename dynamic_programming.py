from emulator import Emulator
from state import State
from robot import Robot
from cell import Cell
from random import randrange
import api
from policy import Policy


class DP:
    def __init__(self):
        self.states = []
        self.policy = Policy().matrix

    def generate_all_states(self):
        for battery in range(0, 3):
            for robot_x in range(api.MAPSIZE):
                for robot_y in range(api.MAPSIZE):
                    for robot_orientation in range(0, 4):
                        for basex in range(api.MAPSIZE):
                            for basey in range(api.MAPSIZE):
                                self.generate_all_map(battery, robot_x, robot_y, robot_orientation, basex, basey)

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

