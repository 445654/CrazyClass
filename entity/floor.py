from . import baseobject
import texture
import config
import collision
from pygame.math import Vector2

class Floor(baseobject.BaseObject):
	def __init__(self):
		size = Vector2(config.ROOM_SIZE)
		super().__init__(size / 2, size, texture.FLOOR_TEXTURE, \
			collision.InnerRectangle(size), config.FLOOR_ORDER)
