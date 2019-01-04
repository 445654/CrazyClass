from . import baseobject
import texture
import config
import collision

class Human(baseobject.BaseObject):
	def __init__(self, pos, size, shape):
		super().__init__(pos, size, shape, collision.Cercle(size.length() / 2), config.HUMAN_ORDER)
