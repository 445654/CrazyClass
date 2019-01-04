from . import baseobject
import texture
import config
import collision
from pygame.math import Vector2

class Table(baseobject.BaseObject):
	def __init__(self, pos):
		super().__init__(pos, config.TABLE_SIZE, texture.TABLE_TEXTURE, \
			collision.Rectangle(config.TABLE_SIZE), config.TABLE_ORDER)
