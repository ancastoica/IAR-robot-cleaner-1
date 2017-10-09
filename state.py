import api


class State:
    def __init__(self, robot, mapp, base):
        self.robot = robot
        self.mapp = mapp
        self.base = base

    def is_final_state(self):
        # Check if all map is clean
        for i in range(api.MAPSIZE):
            for j in range(api.MAPSIZE):
                if self.mapp[i][j].dirty == 1:
                    return False
        # Check if robot at base
        if self.robot.x == self.base[0] and self.robot.y == self.base[1]:
            return True
        else:
            return False

    def to_string(self):
        text = ""
        for i in range(len(self.mapp)):
            for j in range(len(self.mapp[i])):
                cell = self.mapp[i][j]
                text += str(cell.dirty)
                text += str(cell.home)
        text += str(self.base[0])
        text += str(self.base[1])
        text += str(self.robot.battery)
        text += str(self.robot.x)
        text += str(self.robot.y)
        text += str(self.robot.orientation)
        return text
