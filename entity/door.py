from . import baseobject
import texture
import config
import collision
from pygame.math import Vector2

class Door(baseobject.BaseObject):
	def __init__(self, pos):
		super().__init__(pos, config.DOOR_SIZE, texture.DOOR_TEXTURE, \
			collision.Rectangle(config.DOOR_SIZE), config.DOOR_ORDER)
