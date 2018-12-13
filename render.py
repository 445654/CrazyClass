import pygame
from pygame.locals import *

class Renderer:
	def __init__(self, sizes):
		self.screen = pygame.display.set_mode(sizes)

	def update(self, objects):
		ordered_objects = sorted(objects, key=lambda obj: obj.render_order)

		pygame.display.update()
		self.screen.fill((0, 0, 0))
		for obj in ordered_objects:
			obj.shape.render(self.screen, obj.position, obj.size)
