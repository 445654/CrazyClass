import player
import teacher

class Scene:
	def __init__(self, mouse, keyboard):
		self.mouse = mouse
		self.keyboard = keyboard
		self._generate()

	def _generate(self):
		self.player = Player()
		self.teacher = Teacher()
		self.students = []
		self.humans = []
		self.objects = []

	def update(self):
		self._update_player()
		self._update_ai()
		self._update_motion()
		self._update_collisions()

	def _update_player(self):
		self.player.update(self.mouse, self.keyboard)

	def _update_ai(self):
		self.teacher.update()
		for student in self.students:
			student.update()

	def _update_motion(self):
		for human in self.humans:
			human.update_motion()

	def _update_collisions(self):
		pass
