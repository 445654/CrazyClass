from . import baseobject
import texture
import config
import collision
from pygame.math import Vector2

class Chair(baseobject.BaseObject):
	def __init__(self, pos):
		super().__init__(pos, config.CHAIR_SIZE, texture.CHAIR_TEXTURE, \
			collision.Rectangle(config.CHAIR_SIZE), config.CHAIR_ORDER)
