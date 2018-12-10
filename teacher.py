import human
import texture
import random
from pygame.math import Vector2

TARGET_DELAY = 500

def intersect(v1, p1, v2, p2):
	if (v2.x - v1.x) == 0 or (v2.x - v1.x) == 0:
		return None

	dx = (p1.x - p2.x) / (v2.x - v1.x)
	dy = (p1.y - p2.y) / (v2.y - v1.y)
	return p1 + Vector2(v1.x * dx, v1.y * dy)

class Teacher(human.Human):
	def __init__(self, paths, position):
		super().__init__(position, Vector2(30, 30), texture.TEACHER_TEXTURE)
		self.time = 0
		self.paths = paths
		self.nav_points = []
		self._build_intersects()
		self.current_path = 0
		self.speed = 1
		self._random_target()

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

	def _get_path(self, pos):
		# Renvoi le chemin contenant cette position.
		for i, p in enumerate(self.paths):
			minx = min(p[0].x, p[1].x) - 3.0
			maxx = max(p[0].x, p[1].x) + 3.0
			miny = min(p[0].y, p[1].y) - 3.0
			maxy = max(p[0].y, p[1].y) + 3.0
			if minx <= pos.x <= maxx and miny <= pos.y <= maxy:
				return i, p

	def _random_target(self):
		# Selection du chemin cible.
		target_path_ind = random.randint(0, len(self.paths) - 1)
		target_path = self.paths[target_path_ind]
		# Selection du point sur le chemin.
		target = Vector2(random.uniform(target_path[0].x, target_path[1].x),
				random.uniform(target_path[0].y, target_path[1].y))

		# On récupère le chemin actuel.
		cur_path_ind, cur_path = self._get_path(self.position)

		self.nav_points = []
		path_ind = cur_path_ind
		# Trouver tout les points de navigation.
		while path_ind != target_path_ind:
			min_len = 100000
			nav_point = None
			for next_path, point in self.intersects[path_ind]:
				l = (target - point).length()
				if min_len > l:
					min_len = l
					path_ind = next_path
					nav_point = point

			self.nav_points.append(nav_point)
		self.nav_points.append(target)

	def _update_target(self):
		if len(self.nav_points) == 0:
			self._random_target()

	def update(self):
		self._update_target()

	def update_motion(self):
		if len(self.nav_points) == 0:
			return

		next_target = self.nav_points[0]
		vect = next_target - self.position
		dist = vect.length()
		if dist > 2.0:
			vectn = vect.normalize()
			self.position += vectn * self.speed
		else:
			self.nav_points.pop(0)
