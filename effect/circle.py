from . import effect
import pygame

class Circle(effect.Effect):
	def __init__(self, position, life, radius, color):
		super().__init__(position, life)
		self.radius = radius
		self.color = color

	def render(self, screen):
		pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)
