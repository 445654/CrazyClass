import pygame
import config
import effect

class ScreenTitle(effect.Effect):
	def __init__(self, text, life):
		super().__init__(self, life)
		font = pygame.font.Font(None, config.TEXT_SIZE)
		self.surface = font.render(text, 1, config.TEXT_COLOR)
		self.size = font.size(text)

	def render(self, screen):
		screen.blit(self.surface, ((config.SCREEN_SIZE[0] - self.size[0]) / 2, \
					(config.SCREEN_SIZE[1] - self.size[1]) / 2))
