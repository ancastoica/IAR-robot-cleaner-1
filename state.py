class State:
    def __init__(self, robot, mapp, base):
        self.robot = robot
        self.mapp = mapp
        self.base = base

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
