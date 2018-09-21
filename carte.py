
class Carte:
	"""

	"""

	def __init__(self):
		"""
		Le constructeur.

		:param self: Objet
		:type self: Stuff
		"""
		self.credit = 0
		self.nbTicket = 0
		self.valueTicket = 0

	def crediter(self, value):
		if(value < 0):
			raise Exception()
		else:
			self.credit += value

	def solde(self):
		return self.credit

	def crediterTicket(self, value):
		if(value < 0):
			raise Exception()
		else:
			self.nbTicket += value

	def soldeTicket(self):
		return self.valueTicket

	def numberTicket(self):
		return self.nbTicket

	def setValueOfTicket(self, value):
		if(value < 0):
			raise Exception()
		else:
			self.valueTicket = value

	def debiter(self, value):
		if(value > self.solde() or value < 0):
			raise Exception()
		else:
			self.credit -= value

	def debiterTicket(self, value):
		if(self.numberTicket() > 0):
			self.nbTicket -= 1
			value -= self.soldeTicket()
		self.debiter(value)

