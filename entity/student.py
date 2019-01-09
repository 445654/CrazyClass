from . import human
import texture
import config
import random
from pygame.math import Vector2

class Student(human.Human):
	def __init__(self, pos):
		shape = texture.STUDENT_TEXTURES[random.randint(0, len(texture.STUDENT_TEXTURES) - 1)]
		super().__init__(pos, config.STUDENT_SIZE, shape)

	def update(self):
		pass

	def update_motion(self):
		pass

	def get_noise(self):
		return random.randint(0, config.MAX_STUDENT_NOISE)
