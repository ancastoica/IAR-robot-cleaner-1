class State:
    def __init__(self, robot, mapp, base):
        self.robot = robot
        self.mapp = mapp
        self.base = base

    def hash(self):
        info = []
        info.append(self.base)
        for i in range(len(self.mapp)):
            for j in range(len(self.mapp[i])):
                cell = self.mapp[i][j]
                info.append(cell.x)
                info.append(cell.y)
                info.append(cell.dirty)
                info.append(cell.home)
        info.append(self.robot.battery)
        info.append(self.robot.x)
        info.append(self.robot.y)
        info.append(self.robot.orientation)
        full_text = ""
        for c in info:
            full_text += str(c)
        return full_text
