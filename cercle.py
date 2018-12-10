class Cercle:
	def __init__(self, radius):
		self.radius = radius

	def collide(self, other, pos1, pos2):
		return (pos1 - pos2).length() <= (other.radius + self.radius)
