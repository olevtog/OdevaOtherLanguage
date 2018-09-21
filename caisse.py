
class Caisse:
	"""

	"""

	def __init__(self):
		"""
		Le constructeur.

		:param self: Objet
		:type self: Stuff
		"""
		self.carte = 0

	def insererCarte(self, carte):
		self.carte = carte

	def hasCarte(self):
		if(self.carte != 0):
			return True
		return False

	def paiement(self, valeur):
		if(self.hasCarte()):
			self.carte.debiter(valeur)
		else:
			raise Exception()

	def paiementTicket(self, valeur):
		if(self.hasCarte()):
			self.carte.debiterTicket(valeur)
		else:
			raise Exception()

	def solde(self):
		if(self.hasCarte()):
			return self.carte.solde()
		else:
			raise Exception()

	def soldeTicket(self):
		if(self.hasCarte()):
			return self.carte.soldeTicket()
		else:
			raise Exception()

	def numberTicket(self):
		if(self.hasCarte()):
			return self.carte.numberTicket()
		else:
			raise Exception()
