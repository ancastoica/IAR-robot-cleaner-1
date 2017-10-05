class Cell:
	def __init__(self, tag, x, y, dirty=0, home=0):
		self.x = x
		self.y = y
		self.dirty = dirty
		self.home = home

	def clean(self):
		self.dirty = 0