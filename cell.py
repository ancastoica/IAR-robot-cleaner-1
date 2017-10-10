class Cell:
    def __init__(self, x, y, dirty=0, home=0):
        self.x = x
        self.y = y
        self.dirty = dirty
        self.home = home

    def clean(self):
        self.dirty = 0

    def to_string(self):
        text = ""
        text += str(self.x)
        text += str(self.y)
        text += str(self.dirty)
        text += str(self.home)
        return text
