from pygame.math import Vector2

class Rectangle:
	corners = (
		Vector2(-0.5, -0.5),
		Vector2(0.5, -0.5),
		Vector2(0.5, 0.5),
		Vector2(-0.5, 0.5)
	)

	def __init__(self, width, height):
		self.size = Vector2(width, height)

	def collide(self, other, pos1, pos2):
		for i in range(4):
			dir = (self.corners[(i + 1) % 4] - self.corners[i])
			corner = self.corners[i].elementwise() * self.size + pos1
			d = (pos2 - corner)
			side = dir.x * d.y - dir.y * d.x
			if (side + other.radius) < 0.0:
				return False
		return True
