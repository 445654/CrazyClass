from pygame.math import Vector2

class BaseObject:
	def __init__(self, pos, size, shape, collision_shape, render_order):
		self.position = pos
		self.size = size
		self.rotation = 0.0

		self.shape = shape
		self.collision_shape = collision_shape
		self.render_order = render_order

	def collide(self, other):
		return self.collision_shape.collide(other.collision_shape,
				self.position, other.position)

	def get_noise(self):
		return 0
