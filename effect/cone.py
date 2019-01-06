from . import effect
import pygame
import config
from pygame.math import Vector2
from math import cos, sin, degrees

class Cone(effect.Effect):
	def __init__(self, position, life, radius, angle, color):
		super().__init__(position, life)
		self.radius = radius
		self.angle = angle
		self.color = color
		self.rotation = 0.0

		# Création d'un cone centré sans rotation.
		self.points = [Vector2(0, 0)]
		da = angle / config.CONE_RESOLUTION
		for i in range(config.CONE_RESOLUTION + 1):
			a = (-angle / 2) + da * i
			point = Vector2(cos(a), sin(a)) * self.radius
			self.points.append(point)


	def render(self, screen):
		pygame.draw.polygon(screen, self.color, \
			[point.rotate(degrees(self.rotation)) + self.position for point in self.points])
