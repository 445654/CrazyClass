class Loop:
	def __init__(self, renderer, handler, scene):
		self.renderer = renderer
		self.handler = handler
		self.scene = scene

	def update(self):
		quit = False
		quit |= self.handler.update()
		quit |= self.scene.update()

		self.scene.render(self.renderer)

		return quit
