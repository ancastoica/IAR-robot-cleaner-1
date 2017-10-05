class Robot:
	def __init__(self, x, y, X, Y, orientation=1, battery=100):
		"""
		Position x, y
		Orientation entre 0 et 4, on met a 1 par defaut
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
		if x >= 0 and x <= X:
			self.x = x
		if y >= 0 and y <= Y:
			self.y = y

	def rotate_right(self):
		"""
		Rotation -90 dgr => orientation 2 devient 3, 3 devient 0 etc.
		"""
		if self.battery > 0:
			self.orientation = (self.orientation + 1)%4
			self.battery = self.battery - 1

	def rotate_left(self):
		"""
		Rotation +90 dgr => orientation 3 devient 2, 0 devient 3 etc.
		"""
		if self.battery > 0:
			self.orientation = (self.orientation - 1)%4
			self.battery = self.battery - 1

	def go_forward(self):
		"""
		Avance 1 case dans le sens de l'orientation, rotation si avancement pas possible
		"""
		if self.battery > 0:
			self.battery = self.battery - 1

			if self.orientation == 0 and self.y != self.Y:
				self.y = self.y + 1
			elif self.orientation == 1 and self.x != self.X:
				self.x = self.x + 1
			elif self.orientation == 2 and self.y != 0:
				self.y = self.y - 1
			elif self.orientation == 3 and self.x != 0:
				self.x = self.x - 1
			

	def lower_battery(self, n=1):
		if self.battery >= n:
			self.battery = self.battery - n
		else:
			self.battery = 0