from . import baseobject
import texture
import collision

class Human(baseobject.BaseObject):
	def __init__(self, pos, size, shape):
		super().__init__(pos, size, shape, collision.Cercle(size.length() / 2), 20)
