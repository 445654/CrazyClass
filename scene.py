import player
import teacher
import table
import chair
from pygame.math import Vector2

class Scene:
	def __init__(self, mouse, keyboard):
		self.mouse = mouse
		self.keyboard = keyboard
		self.row = 5
		self._generate()

	def _generate_room(self):
		self.tables = []
		self.chairs = []

		for c in range(70, 500, 360):
			for r in range(120, 800, int(700 / self.row)):
				pos = Vector2(r, c)
				t = table.Table(pos)
				self.tables.append(t)

				for i in range(2):
					cpos = pos + Vector2(-40, (i * 2 - 1) * 35)
					ch = chair.Chair(cpos)
					self.chairs.append(ch)

	def _generate(self):
		self.player = player.Player(Vector2(0, 0))
		self.teacher = teacher.Teacher(
			[[Vector2(0, 250), Vector2(800, 250)]] + 
			[[Vector2(x, 0), Vector2(x, 500)] for x in range(70, 800, int(700 / self.row))],
			Vector2(800, 250))
		self.students = [self.player]
		self.humans = [self.teacher] + self.students
		self._generate_room()
		self.objects = self.humans + self.tables + self.chairs

	def update(self):
		self._update_player()
		self._update_ai()
		self._update_motion()
		self._update_collisions()

		return False

	def _update_player(self):
		if self.mouse.click_left:
			self.player.set_target(self.mouse.click_position)

	def _update_ai(self):
		self.teacher.update()
		for student in self.students:
			student.update()

	def _update_motion(self):
		for human in self.humans:
			human.update_motion()

	def _update_collisions(self):
		for obj in self.objects:
			if obj is not self.player:
				if obj.collide(self.player):
					self.player.stop()
