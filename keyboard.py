from pygame.locals import *

class Keyboard:
	def __init__(self):
		self.keys = {}

	def reset(self):
		pass

	def dispatch(self, event):
		self.keys[event.key] = (event.type == KEYDOWN)

	def pressed(self, key):
		return self.keys.get(key, False)
