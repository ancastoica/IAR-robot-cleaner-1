class Robot:
    def __init__(self, x, y, X, Y, orientation=1, battery=100):
        """
        Robot's position x, y
        Boundaries of the map - number of lines Y and number of columns X
        Orientation between 0 and 4:
           0
        3 | | 1
           2
        """
        self.x = x
        self.y = y
        self.X = X
        self.Y = Y
        self.orientation = orientation
        self.battery = battery

    def set_position(self, x, y):
        if 0 <= x < self.X:
            self.x = x
        if 0 <= y < self.Y:
            self.y = y

    def rotate_right(self):
        """
        Right rotation => orientation 2 becomes 3, 3 becomes 0 etc.
        """
        if self.battery > 0:
            self.orientation = (self.orientation + 1) % 4
            self.battery = self.battery - 1

    def rotate_left(self):
        """
        Left rotation => orientation 3 becomes 2, 0 becomes 3 etc.
        """
        if self.battery > 0:
            self.orientation = (self.orientation - 1) % 4
            self.battery = self.battery - 1

    def go_forward(self):
        """
        Go forward 1 cell according to the orientation - only if possible (between boundaries)
        """
        if self.battery > 0:
            self.battery = self.battery - 1

            if self.orientation == 0 and self.x != 0:
                self.x = self.x - 1
            elif self.orientation == 1 and self.y != self.Y - 1:
                self.y = self.y + 1
            elif self.orientation == 2 and self.x != self.X - 1:
                self.x = self.x + 1
            elif self.orientation == 3 and self.y != 0:
                self.y = self.y - 1

    def lower_battery(self, n=1):
        """
        Lower robot's battery by n units
        """
        if self.battery >= n:
            self.battery = self.battery - n
        else:
            self.battery = 0
