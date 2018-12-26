import student
import texture
from pygame.math import Vector2

class Player(student.Student):
	def __init__(self, pos):
		super().__init__(pos, texture.PLAYER_TEXTURE)
		self.speed = 0.2

		self.target = pos
		self.follow = False
		self.noise = 0

	def set_target(self, target):
		self.target = target
		self.follow = True

	def update(self):
		pass

	def get_noise(self):
		noise = self.noise
		self.noise = 0
		return noise

	def update_motion(self):
		if self.follow:
			vect = self.target - self.position
			dist = vect.length()
			if dist > 2.0:
				vectn = vect.normalize()
				self.position += vectn * self.speed

	def stop(self):
		self.follow = False
		self.noise = 15
