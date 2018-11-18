import pygame
from pygame.options import *

class Renderer:
	def __init__(self, sizes):
		self.screen = pygame.display.set_mode(sizes, RESIZABLE);

	def update(self, objects):
		pygame.display.update()
