from pygame.math import Vector2

class Rectangle:
	# Corner pour un rectangle centré normalisé.
	corners = (
		Vector2(-0.5, -0.5),
		Vector2(0.5, -0.5),
		Vector2(0.5, 0.5),
		Vector2(-0.5, 0.5)
	)

	def __init__(self, size):
		self.size = size

	def collide(self, other, pos1, pos2, rot1, rot2):
		normal = Vector2(0, 0)

		# Ne gère pour le moment que les cercles.
		for i in range(4):
			# Optention du vecteur de la droite d'un coté.
			dir = (self.corners[(i + 1) % 4] - self.corners[i])
			# Corner en position absolue.
			corner = self.corners[i].elementwise() * self.size + pos1
			# Vecteur centre cercle vers corner.
			d = (pos2 - corner)
			# Determinant
			side = dir.x * d.y - dir.y * d.x

			# À l'exterieur pour un côté.
			if (side + other.radius) < 0.0:
				return False, Vector2(0, 0)

			# Potentielle intersection avec un côté.
			if abs(side) <= other.radius:
				# On enrgistre seulement la normale.
				normal = -Vector2(-dir.y, dir.x)

		return True, normal
