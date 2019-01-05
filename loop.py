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

		status = self.scene.update_logic()

		# Continuer si en jeu.
		if status == self.scene.STATUS_PLAY:
			start = time.time()
			while (time.time() - start) < config.FRAME_TIME:
				self.scene.update_motion()
				self.scene.render(self.renderer)
		else:
			# TODO affichage
			quit = True

		return quit
