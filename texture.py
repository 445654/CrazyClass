import shape
import pygame

class Texture(shape.Shape):
	def __init__(self, texture_path):
		self.image = pygame.image.load(texture_path).convert()

	def render(self, screen, pos, size):
		corner = pos - size / 2
		image = pygame.transform.scale(self.image, (int(size.x), int(size.y)))
		screen.blit(image, corner)
		#pygame.draw.rect(screen, (255, 255, 255, 255), rect)


STUDENT_TEXTURE = Texture("textures/perso_0.jpg")
PLAYER_TEXTURE = Texture("textures/perso_0.jpg")
TEACHER_TEXTURE = Texture("textures/perso_0.jpg")
TABLE_TEXTURE = Texture("textures/perso_0.jpg")
CHAIR_TEXTURE = Texture("textures/perso_0.jpg")
