import pygame

class Debugger:
	def __init__(self):
		pass

	def render(self, screen, teacher, player, safe_areas):
		self._render_safe_areas(screen, safe_areas)
		self._render_teacher(screen, teacher)

	def _render_teacher(self, screen, teacher):
		for p1, p2 in teacher.paths:
			pygame.draw.line(screen, (255, 0, 0, 255), p1, p2)

		for p, v in teacher.random_targets:
			pygame.draw.circle(screen, (0, 0, 255, 255), (int(p.x), int(p.y)), 1)

		if len(teacher.nav_points) != 0:
			nav = [point.point for point in teacher.nav_points]

			if len(teacher.nav_points) == 1:
				nav.insert(0, teacher.position)

			pygame.draw.lines(screen, (0, 255, 0, 255), False, nav)

	def _render_safe_areas(self, screen, safe_areas):
		for rect, pos in safe_areas:
			size = rect.size
			pygame.draw.rect(screen, (0, 255, 255, 50), (pos.x - size.x / 2, pos.y - size.y / 2, size.x, size.y))
