import human
import texture
from pygame.math import Vector2

class Student(human.Human):
	def __init__(self, pos, shape=texture.STUDENT_TEXTURE):
		super().__init__(pos, Vector2(20, 20), shape)

	def update(self):
		pass

	def update_motion(self):
		pass
