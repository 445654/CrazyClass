from . import moveable
import texture
import effect
import collision
import config
import random
import numpy
from pygame.math import Vector2
from math import atan2, pi

class NavPoint:
	def __init__(self, point, dist, delay):
		self.point = point
		self.dist = dist
		self.delay = delay

def distance_point_line(p, l1, l2):
	dir = l2 - l1
	dist = abs(dir.y * p.x - dir.x * p.y + l2.x * l1.y - l2.y * l1.x) / dir.length()
	return dist

def intersect(v1, p1, v2, p2):
	if (v2.x - v1.x) == 0 or (v2.x - v1.x) == 0:
		return None

	dx = (p1.x - p2.x) / (v2.x - v1.x)
	dy = (p1.y - p2.y) / (v2.y - v1.y)
	return p1 + Vector2(v1.x * dx, v1.y * dy)

class Teacher(moveable.Moveable):
	def __init__(self, paths, random_targets, speed, position):
		super().__init__(config.TEACHER_SIZE, texture.TEACHER_TEXTURE, paths, speed, position)

		# Configuration
		self.noise_sensibility = 11

		self.random_targets = random_targets
		self._random_target()

		self.noisest_position = None

		self.view_effect = effect.Cone(Vector2(self.position), None, \
			config.VIEW_DISTANCE, config.VIEW_ANGLE, config.VIEW_COLOR)
		self.view = collision.Cone(config.VIEW_DISTANCE, config.VIEW_ANGLE)

	def get_noise(self):
		return 0

	def set_noisest(self, position, intensity):
		if intensity > self.noise_sensibility:
			self.noisest_position = Vector2(position)

	def _get_random_target_delay(self):
		return random.randint(config.TEACHER_MIN_RANDOM_DELAY, config.TEACHER_MAX_RANDOM_DELAY)

	def _random_target(self):
		# Selection de la cible aléatoire.
		target_ind = numpy.random.choice(range(len(self.random_targets)), p=[v for _, v in self.random_targets])
		target, _ = self.random_targets[target_ind]

		self._build_nav_points(target, 2.0, self._get_random_target_delay())

	def _update_target(self):
		if self.noisest_position is not None:
			self._build_nav_points(self.noisest_position, 50.0, 0)
			# Mise à none pour ne pas continuer à ce diriger vers la source de bruit.
			self.noisest_position = None
		elif len(self.nav_points) == 0:
			self._random_target()

	def update(self):
		super().update()
		self._update_target()

	def update_motion(self):
		super().update_motion()

		# Mise a jour de la transformation du cone de vue.
		self.view_effect.position = self.position
		self.view_effect.rotation = pi / 2 - self.rotation

	def test_view(self, player):
		return self.view.collide(player.collision_shape, self.position, player.position, \
			pi / 2 - self.rotation, player.rotation)[0]
