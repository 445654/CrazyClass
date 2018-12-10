import baseobject
import texture
import rectangle
from pygame.math import Vector2

class Chair(baseobject.BaseObject):
	def __init__(self, pos):
		super().__init__(pos, Vector2(40, 40), texture.CHAIR_TEXTURE, rectangle.Rectangle(40, 40))
