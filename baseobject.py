from pygame.math import Vector2

class BaseObject:
	def __init__(self, pos, size, shape, collision_shape):
		self.position = pos
		self.size = size
		self.shape = shape
		self.collision_shape = collision_shape

	def collide(self, other):
		return self.collision_shape.collide(other.collision_shape,
				self.position, other.position)
