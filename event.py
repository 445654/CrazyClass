import pygame
from pygame.options import *

class Handler:
	def __init__(self, mouse, keyboard):
		self.mouse = mouse
		self.keyboard = keyboard

	def update(self):
		for event in pygame.event.get():
			if event.type in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONUP):
				self.mouse.dispatch(event)
			elif event.type in (KEYDOWN, KEYUP):
				self.keyboard.dispatch(event)
