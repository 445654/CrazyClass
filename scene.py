import entity
from pygame.math import Vector2
from pygame.locals import *
import effect
import ui
import config
import collision
import random
import debugger
from math import pi, exp

def row_range(row):
	width = config.ROOM_SIZE.x * 0.8
	return enumerate(range(int(config.ROOM_SIZE.x // 10), int(width), int(width / row)))

def column_range(col):
	return enumerate(range(int(config.TABLE_SIZE.y // 2), int(config.ROOM_SIZE.y), \
		int((config.ROOM_SIZE.y - config.TABLE_SIZE.y) / (col - 1))))

class Scene:
	STATUS_PLAY = 0
	STATUS_LOST = 1
	STATUS_WON = 2

	def __init__(self, mouse, keyboard):
		self.mouse = mouse
		self.keyboard = keyboard

		self.debugger = debugger.Debugger()

		self.columns = 2
		self.rows = 5

		self.difficulty = 0
		self._generate_level(self.difficulty)
		self._generate_ui()

	def _generate_level(self, difficulty):
		# État actuel de la partie.
		self.status = self.STATUS_PLAY

		self.life = config.LIFE

		self.effects = []

		self._generate_room(difficulty)

	def _generate_ui(self):

		self.noise_bar = ui.Bar(Vector2(config.SCREEN_SIZE[0] * 0.1, config.ROOM_SIZE.y + config.UI_SIZE.y * 0.1), \
								Vector2(config.UI_SIZE.x * 0.8, config.UI_SIZE.y * 0.2), config.NOISE_COLOR)

		text_x = config.SCREEN_SIZE[0] * 0.05
		noise_text = ui.Text("Bruit :", Vector2(text_x, config.ROOM_SIZE.y + config.UI_SIZE.y * 0.2), 30)
		self.life_text = ui.Text("", Vector2(text_x, config.ROOM_SIZE.y + config.UI_SIZE.y * 0.5), 30)

		self.uis = [self.noise_bar, self.life_text, noise_text]

	def _generate_room(self, difficulty):
		self.tables = []
		self.chairs = []
		self.students = []
		self.safe_areas = []

		center_x = config.ROOM_SIZE.y / 2
		# Génération des chemins de navigation, allé centrale + tables.
		paths = [[Vector2(0, center_x), Vector2(config.ROOM_SIZE.x, center_x)]] + \
					[[Vector2(r, 0), Vector2(r, config.ROOM_SIZE.y)] for _, r in row_range(self.rows)]
		random_targets = []

		# Génération de points de navigation supplémentaire pour le tableau.
		board_x = config.ROOM_SIZE.x - config.TEACHER_SIZE.x
		for i in range(config.BOARD_POINTS):
			random_targets.append((Vector2(board_x, \
				(i + 1) / (config.BOARD_POINTS + 1) * config.ROOM_SIZE.y), config.NAV_BOARD_PROB)) # TODO diffi
		# Ajout d'un chemin pour le tableau.
		paths.append([Vector2(board_x, 0), Vector2(board_x, config.ROOM_SIZE.y)])

		# Le numéro aléatoire de la chaise du joueur.
		rand_col = random.randint(0, self.columns - 1)
		max_row = self.rows - 1
		# Choix du rang en fonction de la difficulté, plus elle augmente plus il y a de chance
		# d'être près du tableau.
		rand_row = random.randint(max_row - int(max_row * exp(-difficulty * config.PLAYER_ROW_DIFFICULTY)), max_row)
		rand_chair = random.randint(0, 1)

		# Génération des chaises, des tables et des élèves.
		for c_i, c in column_range(self.columns):
			for r_i, r in row_range(self.rows):
				pos = Vector2(r + config.CHAIR_SIZE.x + config.TEACHER_SIZE.x, c)
				t = entity.Table(pos)
				self.tables.append(t)

				# Deux chaises par table.
				for i in range(2):
					# Position de la chaise
					cpos = pos + Vector2(-42, (i * 2 - 1) * 35)
					random_targets.append(
						(Vector2(cpos.x - config.CHAIR_SIZE.x / 2 - config.TEACHER_SIZE.x / 2, cpos.y), config.NAV_CHAIR_PROB))

					ch = entity.Chair(cpos)
					self.chairs.append(ch)

					# Assignation d'un élève ou du joueur.
					if c_i == rand_col and r_i == rand_row and i == rand_chair:
						player_position = Vector2(cpos.x - config.STUDENT_SIZE.x / 2, cpos.y)
						self.player = entity.Player(paths, \
							config.PLAYER_SPEED * config.PLAYER_SPEED_DIFFICULTY ** difficulty, player_position)
						ch.student = self.player
					else:
						stud = entity.Student(cpos)
						ch.student = stud
						self.students.append(stud)

					ch.student.rotation = pi / 2

		prob_sum = sum((v for _, v in random_targets))
		random_targets = [(p, v / prob_sum) for p, v in random_targets]

		self.teacher = entity.Teacher(paths, random_targets, \
			config.TEACHER_SPEED * config.TEACHER_SPEED_DIFFICULTY ** difficulty, \
			Vector2(config.ROOM_SIZE.x, center_x))
		self.effects.append(self.teacher.view_effect)

		for i in range(self.columns):
			# Génération d'une zone saine pour se cacher.
			safe_area = collision.Rectangle(Vector2(config.ROOM_SIZE.x * 0.8, config.TABLE_SIZE.y))
			self.safe_areas.append((safe_area, Vector2(config.ROOM_SIZE.x * 0.45, \
				config.TABLE_SIZE.y / 2 + (config.ROOM_SIZE.y - config.TABLE_SIZE.y) * i)))

		# Création des portes.
		door_front = entity.Door(Vector2(config.ROOM_SIZE.x * 0.97 - config.DOOR_SIZE.x / 2, \
					config.ROOM_SIZE.y - config.DOOR_SIZE.y / 2))
		door_back = entity.Door(Vector2(config.ROOM_SIZE.x * 0.03 + config.DOOR_SIZE.x / 2, \
					config.ROOM_SIZE.y - config.DOOR_SIZE.y / 2))
		self.doors = [door_front, door_back]

		self.floor = entity.Floor()

		self.students.append(self.player)
		self.humans = [self.teacher] + self.students

		self.objects = self.humans + self.tables + self.chairs + self.doors + [self.floor]

	def _win(self):
		self.status = self.STATUS_WON

		title = ui.ScreenTitle("Vous avez fuit", config.TITLE_LIFE)
		self.uis.append(title)

	def _loose(self):
		self.status = self.STATUS_LOST

		title = ui.ScreenTitle("Vous êtes exclu", config.TITLE_LIFE)
		self.uis.append(title)

	def _catch_player(self):
		# On perd une vie et perd potentiellement.
		if self.life == 0:
			self._loose()
		self.life -= 1

		# Le joueur retourne à sa place.
		self.player.return_seat()

	def _player_caught(self):
		return self.player.status == self.player.STATUS_CAUGHT

	def update_logic(self):
		self._update_debug()
		self._update_level()
		self._update_player()
		self._update_ai()
		self._update_noise()
		self._update_effects()
		self._update_uis()

		# Test de collision et de vue seulement quand le joueur n'est pas attrapé.
		if not self._player_caught():
			self._update_collisions()
			self._update_view()

		return self.status

	def _update_debug(self):
		# Opération de debugage
		self.debug = self.keyboard.pressed(K_d)
		if self.keyboard.pressed(K_w):
			self._win()
		elif self.keyboard.pressed(K_l):
			self._loose()

	def _update_level(self):
		# Génération du niveau sivant.
		if self.status == self.STATUS_WON:
			# Augmentation de la difficulté.
			self.difficulty += 1
			self._generate_level(self.difficulty)
		elif self.status == self.STATUS_LOST:
			self._generate_level(self.difficulty)

	def _update_player(self):
		self.player.update()

		if self.mouse.click_left:
			self.player.set_target(self.mouse.click_position)

	def _update_ai(self):
		self.teacher.update()
		for student in self.students:
			student.update()

	def _update_noise(self):
		noisest, intensity = max(((obj, obj.get_noise()) for obj in self.objects), key=lambda pair: pair[1])
		self.teacher.set_noisest(noisest.position, intensity)
		self.effects.append(effect.Circle(noisest.position, 1, intensity * 5, config.NOISE_COLOR))
		self.noise_bar.value = intensity / config.MAX_NOISE

	def update_motion(self):
		for human in self.humans:
			human.update_motion()

	def _update_collisions(self):
		for obj in self.objects:
			if obj is not self.player:
				hit, normal = obj.collide(self.player)
				if hit:
					# Lorsqu'on touche une porte le jeu est fini
					if isinstance(obj, entity.Door):
						self._win()
						continue
					# On évite de faire une collision avec sa chaise ou les chaises vides.
					elif isinstance(obj, entity.Chair):
						if obj.student in (self.player, None):
							continue

					self.player.hit(obj, normal)
					self._catch_player()

	def _update_effects(self):
		effects = []
		for effect in self.effects:
			if effect.update_time():
				effects.append(effect)

		self.effects = effects

	def _update_uis(self):
		self.life_text.text = "Vie : {}/{}".format(self.life, config.LIFE)

		uis = []
		for ui in self.uis:
			if ui.update_time():
				uis.append(ui)

		self.uis = uis

	def _update_view(self):
		visible = self.teacher.test_view(self.player)
		if visible:
			in_area = False
			for rect, pos in self.safe_areas:
				hit, normal = rect.collide(self.player.collision_shape, pos, self.player.position, 0.0, self.player.rotation)
				if hit:
					in_area = True
					break

			if not in_area:
				self._catch_player()

	def render(self, renderer):
		renderer.clear()

		if self.debug:
			self._render_debug(renderer)

		self._render_objects(renderer)
		self._render_effects(renderer)
		self._render_uis(renderer)

		renderer.flush()

	def _render_objects(self, renderer):
		ordered_objects = sorted(self.objects, key=lambda obj: obj.render_order)

		for obj in ordered_objects:
			obj.shape.render(renderer.screen, obj.position, obj.size, obj.rotation)

	def _render_effects(self, renderer):
		for effect in self.effects:
			effect.render(renderer.overlay)

	def _render_uis(self, renderer):
		for ui in self.uis:
			ui.render(renderer.screen)

	def _render_debug(self, renderer):
		self.debugger.render(renderer.debug_overlay, self.teacher, self.player, self.safe_areas)
