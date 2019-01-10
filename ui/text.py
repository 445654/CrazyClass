import pygame
import effect
import config

class Text(effect.Effect):
	def __init__(self, text, position, size, color=config.TEXT_COLOR, life=None):
		super().__init__(self, life)
		self.size = size
		self.position = position
		self.color = color
		self.text = text

	def render(self, screen):
		font = pygame.font.Font(None, self.size)
		surface = font.render(self.text, 1, self.color)
		size = font.size(self.text)

		screen.blit(surface, (self.position.x - size[0] / 2, \
					self.position.y - size[1] / 2))
