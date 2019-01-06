import pygame

class Debugger:
	def __init__(self):
		pass

	def render(self, screen, teacher, player):
		for p1, p2 in teacher.paths:
			pygame.draw.line(screen, (255, 0, 0, 255), p1, p2)

		if len(teacher.nav_points) != 0:
			nav = [point for point, dist in teacher.nav_points]

			if len(teacher.nav_points) == 1:
				nav.insert(0, teacher.position)

			pygame.draw.lines(screen, (0, 255, 0, 255), False, nav)
