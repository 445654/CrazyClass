from . import student
import texture
from pygame.math import Vector2
from math import atan2

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

	def get_noise(self): # TODO begin / end logic
		noise = self.noise
		self.noise = 0
		return noise

	def update_motion(self):
		if self.follow:
			vect = self.target - self.position
			dist = vect.length()
			self.rotation = atan2(vect.y, vect.x)
			if dist > 2.0:
				vectn = vect.normalize()
				self.position += vectn * self.speed

	def hit(self, other):
		# Bruit de la collision
		self.noise = 50

		# On arrête notre mouvement.
		self.follow = False
		# On se fait repousser par l'objet.'
		dir = (self.position - other.position).normalize()
		self.position += dir * 20
