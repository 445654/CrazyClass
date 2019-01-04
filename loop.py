import time
import config

class Loop:
	def __init__(self, renderer, handler, scene):
		self.renderer = renderer
		self.handler = handler
		self.scene = scene

	def update(self):
		quit = False
		quit |= self.handler.update()
		quit |= self.scene.update_logic()

		start = time.time()
		while (time.time() - start) < config.FRAME_TIME:
			self.scene.update_motion()
			self.scene.render(self.renderer)

		return quit
