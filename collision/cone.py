from pygame.math import Vector2
from math import cos, sin, acos, pi

class Cone:
	def __init__(self, radius, angle):
		self.radius = radius
		self.half_angle = angle / 2

	def collide(self, other, pos1, pos2, rot1, rot2):
		d = (pos2 - pos1)
		dn = d.normalize()
		dir = Vector2(cos(rot1), sin(rot1))
		dot = min(dn * dir, 1.0)

		hit = (d.length() <= (other.radius + self.radius)) and \
				(acos(dot) <= self.half_angle)
		normal = dn
		return hit, normal
