from state import State
from robot import Robot
from random import randrange
from cell import Cell


MAPSIZE = 3     # The size of the map knowing that it is a square
ACTIONS = ["go_forward_vacuuming", "go_forward_no_vacuuming", "rotate_left", "rotate_right", "vacuum"]      # List of possible actions
DISCOUNTED_FACTOR = 0.01    # The factor used to make the series converge

"""
Print a terminal version of the map
"""
def printmap(mapp):
    for i in range(len(mapp)):
        line = ""
        for j in range(len(mapp[i])):
            if mapp[i][j].home == 1:
                line += "h"
            elif mapp[i][j].dirty == 1:
                line += "x"
            elif mapp[i][j].dirty == 0:
                line += "o"
        print(line)


"""
Print a readable state
"""
def printstate(state):
    print("Robot coordinates : (", state.robot.x, ", ", state.robot.y, ")")
    print("Robot battery : ", state.robot.battery)
    print("Robot orientation (0 for N, 1 fro E, 2 for S, 3 for W): ", state.robot.orientation)
    print("Home base coordinates: (", state.base[0], ", ", state.base[1], ")")
    printmap(state.mapp)


"""
Creates a random map given the position of the homebase
"""
def randommap(basex, basey):
    mapp = [[Cell(0, 0) for j in range(MAPSIZE)] for i in range(MAPSIZE)]

    for i in range(MAPSIZE):
        for j in range(MAPSIZE):
            if i == basex and j == basey:
                mapp[i][j] = Cell(i, j, randrange(2), 1)
            else:
                mapp[i][j] = Cell(i, j, randrange(2))
    return mapp


"""
Creates a random states with random robot and map
"""
def randomstate():
    base = (randrange(0, MAPSIZE), randrange(0, MAPSIZE))
    robot = Robot(randrange(0, MAPSIZE), randrange(0, MAPSIZE), MAPSIZE, MAPSIZE, randrange(0, 4), randrange(0, 100))

    rstate = State(
        robot,
        randommap(base[0], base[1]),
        base
    )

    return rstate
