class Loop:
	def __init__(self, renderer, handler, scene):
		self.renderer = renderer
		self.handler = handler
		self.scene = scene

	def update(self):
		quit = False
		if self.handler.update():
			quit = True

		if self.scene.update():
			quit = True

		self.renderer.update(self.scene.objects)

		return quit
