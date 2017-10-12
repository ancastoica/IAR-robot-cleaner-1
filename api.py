from state import State
from robot import Robot
from random import randrange
from cell import Cell

MAPSIZE = 3     # The size of the map knowing that it is a square
ACTIONS = ["go_forward_vacuuming", "go_forward_no_vacuuming", "rotate_left", "rotate_right", "vacuum"]      # List of possible actions
DISCOUNTED_FACTOR = 0.01    # The factor used to make the series converge
INITIAL_MAP = [[Cell(0, 0, 0, 1), Cell(0, 1, 1, 0), Cell(0, 2, 0, 0)], [Cell(1, 0, 1, 0), Cell(1, 1, 0, 0), Cell(1, 2, 1, 0)], [Cell(2, 0, 0, 0), Cell(2, 1, 1, 0), Cell(2, 2, 0, 0)]]
# Initial map
# hxo
# xox
# oxo
INITIAL_STATE = State(Robot(0, 0, MAPSIZE, MAPSIZE, 1, 100), INITIAL_MAP, (0, 0))


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


def initmap(base_x=0, base_y=0):
    mapp = [[Cell(0, 0, 0, 0) for j in range(MAPSIZE)] for i in range(MAPSIZE)]
    mapp[base_x][base_y] = Cell(base_x, base_y, 0, 1)

    return mapp


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


def resetvector(vector):
    return [0.0 for i in range(len(vector))]

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


def get_state(text):
    index = 0
    robot = Robot(0, 0, MAPSIZE, MAPSIZE, 0, 0)
    mapp = [[Cell(0, 0) for j in range(MAPSIZE)] for i in range(MAPSIZE)]
    for i in range(len(mapp)):
        for j in range(len(mapp[i])):
            mapp[i][j].set(i, j, int(text[index]), int(text[index+1]))
            index += 2
    index += 1
    base = (int(text[index-1]), int(text[index]))

    index += 1
    robot.x = int(text[index])

    index += 1
    robot.y = int(text[index])

    index += 1
    robot.orientation = int(text[index])

    index += 1
    robot.battery = int(text[index:])

    return State(robot, mapp, base)
