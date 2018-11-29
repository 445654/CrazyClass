import pygame
from pygame.locals import *

class Renderer:
	def __init__(self, sizes):
		self.screen = pygame.display.set_mode(sizes, RESIZABLE)

	def update(self, objects):
		pygame.display.update()
		for obj in objects:
			obj.shape.render(self.screen, obj.position, obj.size)
