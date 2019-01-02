import pygame
from pygame.locals import *

class Renderer:
	def __init__(self, sizes):
		self.screen = pygame.display.set_mode(sizes)

	def clear(self):
		pygame.display.update()
		self.screen.fill((0, 0, 0))
