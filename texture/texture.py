import shape
import pygame
from math import degrees

class Texture(shape.Shape):
	def __init__(self, texture_path):
		self.image = pygame.image.load(texture_path).convert_alpha()

	def render(self, screen, pos, size, rotation):
		corner = pos - size / 2
		image = pygame.transform.scale(self.image, (int(size.x), int(size.y)))
		image = pygame.transform.rotate(image, degrees(rotation))
		screen.blit(image, corner)


STUDENT_TEXTURES = [Texture("texture/student_{}.png".format(i)) for i in range(4)]
PLAYER_TEXTURE = Texture("texture/player.png")
TEACHER_TEXTURE = Texture("texture/teacher.png")
TABLE_TEXTURE = Texture("texture/table.png")
CHAIR_TEXTURE = Texture("texture/chaise.png")
DOOR_TEXTURE = Texture("texture/door.png")
FLOOR_TEXTURE = Texture("texture/floor.jpg")
