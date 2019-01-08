from . import student
import texture
import config
from pygame.math import Vector2
from math import atan2

class Player(student.Student):
	def __init__(self, speed, pos):
		super().__init__(pos, texture.PLAYER_TEXTURE)
		self.speed = speed

		self.target = pos
		self.follow = False
		self.noise = 0

	def set_target(self, target):
		self.target = target
		self.follow = True

	def update(self):
		# Remise a zéro du bruit après une potentielle collision.
		self.noise = 0

	def get_noise(self):
		return self.noise

	def update_motion(self):
		if self.follow:
			vect = self.target - self.position
			dist = vect.length()
			if dist > 2.0:
				vectn = vect.normalize()
				self.position += vectn * self.speed
				self.rotation = atan2(vect.x, vect.y)

	def hit(self, other, normal):
		# Bruit de la collision
		self.noise = config.COLLISION_NOISE

		# On arrête notre mouvement.
		self.follow = False

		# On se fait repousser par l'objet.'
		self.position += normal * config.COLLISION_FORCE
