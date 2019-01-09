import pygame
import config
from . import text
from pygame.math import Vector2

class ScreenTitle(text.Text):
	def __init__(self, text, life):
		super().__init__(text, Vector2(config.SCREEN_SIZE) / 2, config.TEXT_SIZE, config.TEXT_COLOR, life)
