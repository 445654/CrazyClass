import pygame
import effect

class Bar(effect.Effect):
	def __init__(self, position, size, color, value=0.0):
		super().__init__(self, None)
		self.position = position
		self.size = size
		self.color = color
		self.value = value

	def render(self, screen):
		pygame.draw.rect(screen, self.color, \
			(int(self.position.x), int(self.position.y), int(self.size.x * self.value), int(self.size.y)))
