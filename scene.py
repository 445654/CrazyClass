import player
import teacher

class Scene:
	def __init__(self, mouse, keyboard):
		self.mouse = mouse
		self.keyboard = keyboard
		self._generate()

	def _generate(self):
		self.player = player.Player((0, 0), (10, 10), "")
		self.teacher = teacher.Teacher((100, 100), (10, 10), "")
		self.students = [self.player]
		self.humans = [self.teacher] + self.students;
		self.tables = []
		self.objects = self.humans + self.tables

	def update(self):
		self._update_player()
		self._update_ai()
		self._update_motion()
		self._update_collisions()

		return False

	def _update_player(self):
		self.player.target = self.mouse.click_position

	def _update_ai(self):
		self.teacher.update()
		for student in self.students:
			student.update()

	def _update_motion(self):
		for human in self.humans:
			human.update_motion()

	def _update_collisions(self):
		pass
