import player
import student
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

	def _generate(self):
		self.tables = []
		self.chairs = []
		self.students = []

		# Génération des chemins du prof, allé centrale + tables.
		paths = [[Vector2(0, 250), Vector2(800, 250)]] + \
			[[Vector2(r, 0), Vector2(r, 500)] for r in range(70, 800, int(700 / self.row))]

		# Génération des chaises, des tables et des élèves.
		for c in range(70, 500, 360):
			for r in range(120, 800, int(700 / self.row)):

				pos = Vector2(r, c)
				t = table.Table(pos)
				self.tables.append(t)

				# Deux chaises par table.
				for i in range(2):
					# Position de la chaise
					cpos = pos + Vector2(-40, (i * 2 - 1) * 35)

					ch = chair.Chair(cpos)
					self.chairs.append(ch)

					stud = student.Student(cpos)
					self.students.append(stud)

		self.teacher = teacher.Teacher(paths, Vector2(800, 250))
		self.player = player.Player(Vector2(0, 0))
		self.students.append(self.player)
		self.humans = [self.teacher] + self.students
		self.objects = self.humans + self.tables + self.chairs

	def update(self):
		self._update_player()
		self._update_ai()
		self._update_noise()
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

	def _update_noise(self):
		noisest, intensity = max(((obj, obj.get_noise()) for obj in self.objects), key=lambda pair: pair[1])
		self.teacher.set_noisest(noisest, intensity)

	def _update_motion(self):
		for human in self.humans:
			human.update_motion()

	def _update_collisions(self):
		for obj in self.objects:
			if obj is not self.player:
				if obj.collide(self.player):
					self.player.stop()
