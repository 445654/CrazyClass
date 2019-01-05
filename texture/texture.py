import shape
import pygame

class Texture(shape.Shape):
	def __init__(self, texture_path):
		self.image = pygame.image.load(texture_path).convert_alpha()

	def render(self, screen, pos, size, rotation):
		corner = pos - size / 2
		image = pygame.transform.scale(self.image, (int(size.x), int(size.y)))
		screen.blit(image, corner)


STUDENT_TEXTURE = Texture("texture/perso_0.jpg")
PLAYER_TEXTURE = Texture("texture/perso_0.jpg")
TEACHER_TEXTURE = Texture("texture/perso_0.jpg")
TABLE_TEXTURE = Texture("texture/table.png")
CHAIR_TEXTURE = Texture("texture/chaise.png")
DOOR_TEXTURE = Texture("texture/door.png")
FLOOR_TEXTURE = Texture("texture/floor.jpg")
