import pygame
from pygame.locals import *

class Handler:
	def __init__(self, mouse, keyboard):
		self.mouse = mouse
		self.keyboard = keyboard

	def update(self):
		self.mouse.reset()
		self.keyboard.reset()

		quit = False

		for event in pygame.event.get():
			if event.type in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN):
				self.mouse.dispatch(event)
			elif event.type in (KEYDOWN, KEYUP):
				self.keyboard.dispatch(event)

			if event.type == QUIT:
				quit = True

		return quit
