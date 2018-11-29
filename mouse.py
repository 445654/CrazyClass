from pygame.math import Vector2
from pygame.locals import *

class Mouse:
	def __init__(self):
		self.position = Vector2(0, 0)
		self.click_position = Vector2(0, 0)
		self.click_left = False
		self.click_right = False

	def reset(self):
		# Remise à zero des évenements.
		self.click_left = False
		self.click_right = False

	def dispatch(self, event):
		if event.type == MOUSEMOTION:
			self.position = event.pos

		if event.type == MOUSEBUTTONDOWN:
			if event.button == 1:
				self.click_left = True
				self.click_position = self.position
			elif event.button == 3:
				self.click_right = True
				self.click_position = self.position
