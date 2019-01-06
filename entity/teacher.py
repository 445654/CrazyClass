from . import human
import texture
import effect
import collision
import config
import random
from pygame.math import Vector2
from math import atan2, pi

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

class Teacher(human.Human):
	def __init__(self, paths, position):
		super().__init__(position, config.TEACHER_SIZE, texture.TEACHER_TEXTURE)

		# Configuration
		self.speed = config.TEACHER_SPEED
		self.noise_sensibility = 11

		self.paths = paths

		self.nav_points = []
		self._build_intersects()
		self.current_path = 0

		self._random_target()

		self.noisest = None

		self.view_effect = effect.Cone(Vector2(self.position), None, \
			config.VIEW_DISTANCE, config.VIEW_ANGLE, config.VIEW_COLOR)
		self.view = collision.Cone(config.VIEW_DISTANCE, config.VIEW_ANGLE)

	def get_noise(self):
		return 0

	def set_noisest(self, noisest, intensity):
		if intensity > self.noise_sensibility:
			self.noisest = noisest

	def _build_intersects(self):
		self.intersects = [[] for i in range(len(self.paths))]
		for i, p1 in enumerate(self.paths):
			v1 = p1[1] - p1[0]
			for j, p2 in enumerate(self.paths):
				if p1 == p2:
					continue

				v2 = p2[1] - p2[0]
				inter = intersect(v1, p1[0], v2, p2[0])
				if inter is not None:
					self.intersects[i].append((j, inter))

	def _get_nearest_path(self, pos):
		min_dist = 1000000
		nearest_path = None
		nearest_path_ind = -1
		for i, p in enumerate(self.paths):
			dist = distance_point_line(pos, p[0], p[1])
			if dist < min_dist:
				min_dist = dist
				nearest_path = p
				nearest_path_ind = i

		return nearest_path_ind, nearest_path

	def _random_target(self):
		# Selection du chemin cible.
		target_path_ind = random.randint(0, len(self.paths) - 1)
		target_path = self.paths[target_path_ind]
		# Selection du point sur le chemin.
		target = Vector2(random.uniform(target_path[0].x, target_path[1].x),
				random.uniform(target_path[0].y, target_path[1].y))

		self._build_nav_points(target, 2.0)

	def _build_nav_points(self, target, target_dist):
		# On récupère le chemin le plus proche de la cible.
		target_path_ind, target_path = self._get_nearest_path(target)

		# On récupère le chemin actuel.
		cur_path_ind, cur_path = self._get_nearest_path(self.position)

		self.nav_points = []

		path_ind = cur_path_ind
		# Trouver tout les points de navigation.
		while path_ind != target_path_ind:
			min_len = 100000
			nav_point = None
			# Trouver l'intesection la plus proche de la cible.
			for next_path, point in self.intersects[path_ind]:
				l = (target - point).length()
				if min_len > l:
					min_len = l
					path_ind = next_path
					nav_point = point

			self.nav_points.append((nav_point, 2.0))
		self.nav_points.append((target, target_dist))

	def _update_target(self):
		if self.noisest is not None:
			self._build_nav_points(self.noisest.position, 50.0)
			# Mise à none pour ne pas continuer à ce diriger vers la source de bruit.
			self.noisest = None
		else:
			if len(self.nav_points) == 0:
				self._random_target()

	def update(self):
		self._update_target()

	def update_motion(self):
		if len(self.nav_points) == 0:
			return

		next_target, point_dist = self.nav_points[0]
		vect = next_target - self.position
		dist = vect.length()
		if dist > point_dist:
			vectn = vect.normalize()
			self.position += vectn * self.speed
			self.rotation = atan2(vect.x, vect.y)
		else:
			self.nav_points.pop(0)

		# Mise a jour de la transformation du cone de vue.
		self.view_effect.position = self.position
		self.view_effect.rotation = pi / 2 - self.rotation

	def test_view(self, player):
		return self.view.collide(player.collision_shape, self.position, player.position, \
			pi / 2 - self.rotation, player.rotation)[0]
