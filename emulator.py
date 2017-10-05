from random import randrange
from cell import Cell


class Emulator:
    def __init__(self):
        self.map = [[Cell(0, 0) for j in range(3)] for i in range(3)]   # The map matrices containing the cells
        self.algorithm = 0  # 0 for dynamic programming, 1 for MonteCarlo, 2 for Time Differentials
        # rewards model
        self.empty_battery = {"go_forward_vacuuming" : (-100 + -1 + -1 + -1), "go_forward_no_vacuuming" : (-100 + -1 + -1), "rotate_left": (-100 + -1 + -1), "rotate_right": (-100 + -1 + -1), "vacuum": (-100 + -1 + -1)}
        self.critical_battery = {"go_forward_vacuuming" : -100, "go_forward_no_vacuuming" : -100, "rotate_left": -100, "rotate_right": -100, "vacuum": -100}
        self.sufficient_battery = {"go_forward_vacuuming" : -100, "go_forward_no_vacuuming" : -100, "rotate_left": -100, "rotate_right": -100, "vacuum": -100}
        self.cell_class0 = {"go_forward_vacuuming" : -100, "go_forward_no_vacuuming" : -100, "rotate_left": -100, "rotate_right": -100, "vacuum": -100}
        self.cell_class1 = {"go_forward_vacuuming" : -100, "go_forward_no_vacuuming" : -100, "rotate_left": -100, "rotate_right": -100, "vacuum": -100}
        self.cell_class2 = {"go_forward_vacuuming" : -100, "go_forward_no_vacuuming" : -100, "rotate_left": -100, "rotate_right": -100, "vacuum": -100}
        self.dirty_cell = {"go_forward_vacuuming" : -100, "go_forward_no_vacuuming" : -100, "rotate_left": -100, "rotate_right": -100, "vacuum": -100}
        self.clean_cell = {"go_forward_vacuuming" : -100, "go_forward_no_vacuuming" : -100, "rotate_left": -100, "rotate_right": -100, "vacuum": -100}

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
    def simulate(self):
        return

