from . import moveable
import texture
import config
from pygame.math import Vector2
from math import atan2

class Player(moveable.Moveable):
	# Peut naviguer.
	STATUS_NORMAL = 0
	# Retourne à sa chaise.
	STATUS_CAUGHT = 1

	def __init__(self, paths, speed, pos):
		super().__init__(config.PLAYER_SIZE, texture.PLAYER_TEXTURE, paths, speed, pos)

		# Position initial de notre chaise.
		self.init_position = Vector2(pos)
		self.status = self.STATUS_NORMAL
		self.noise = 0

	def set_target(self, target):
		if self.status == self.STATUS_NORMAL:
			# On se dirige directement vers la cible.
			self.nav_points = [moveable.NavPoint(target, 2.0, 0)]

	def update(self):
		super().update()

		# On repasse en état normal après être retourné à sa chaise.
		if self.status == self.STATUS_CAUGHT and len(self.nav_points) == 0:
			self.status = self.STATUS_NORMAL

		# Remise a zéro du bruit après une potentielle collision.
		self.noise = 0

	def get_noise(self):
		return self.noise

	def return_seat(self):
		# On retourne à notre chaise
		self.status = self.STATUS_CAUGHT
		self._build_nav_points(self.init_position, 2.0, config.PLAYER_COLLISION_WAIT)

	def hit(self, other, normal):
		# Bruit de la collision
		self.noise = config.COLLISION_NOISE
		# On se fait repousser par l'objet.
		self.position += normal * config.COLLISION_FORCE

