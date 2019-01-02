from . import baseobject
import texture
import collision
from pygame.math import Vector2

class Table(baseobject.BaseObject):
	def __init__(self, pos):
		super().__init__(pos, Vector2(60, 140), texture.TABLE_TEXTURE, collision.Rectangle(60, 140), 10)
