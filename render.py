import pygame
from pygame.locals import *

class Renderer:
	def __init__(self, sizes):
		self.screen = pygame.display.set_mode(sizes)

	def update(self, objects):
		pygame.display.update()
		self.screen.fill((0, 0, 0))
		for obj in objects:
			obj.shape.render(self.screen, obj.position, obj.size)
