import pygame
from pygame.locals import *

class Renderer:
	def __init__(self, size, overlay_size):
		self.screen = pygame.display.set_mode(size)
		self.overlay = pygame.Surface(overlay_size, flags=SRCALPHA)

	def clear(self):
		pygame.display.update()
		self.screen.fill((0, 0, 0))
		self.overlay.fill((0, 0, 0, 0))

	def flush(self):
		self.screen.blit(self.overlay, (0, 0))
