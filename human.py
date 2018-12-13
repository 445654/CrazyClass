import baseobject
import texture
import cercle

class Human(baseobject.BaseObject):
	def __init__(self, pos, size, shape):
		super().__init__(pos, size, shape, cercle.Cercle(size.length() / 2), 20)
