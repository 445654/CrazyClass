from pygame.math import Vector2
from . import rectangle

class InnerRectangle(rectangle.Rectangle):
	def collide(self, other, pos1, pos2):
		if (pos2.x + other.radius) > self.size.x:
			return True, Vector2(-1, 0)
		if (pos2.x - other.radius) < 0:
			return True, Vector2(1, 0)
		if (pos2.y + other.radius) > self.size.y:
			return True, Vector2(0, -1)
		if (pos2.y - other.radius) < 0:
			return True, Vector2(0, 1)

		return False, Vector2(0, 0)
