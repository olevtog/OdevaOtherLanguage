#Defossez Gautier
#Valette Henri

import unittest
from carte import Carte

class TestCarte(unittest.TestCase):

	def test_crediter_carte(self):
		carte = Carte()
		carte.crediter(5)
		self.assertTrue(carte.solde() == 5)

	def test_crediter_carte_exception(self):
		carte = Carte()
		with self.assertRaises(Exception):
			carte.crediter(-5)

	def test_crediter_carte_tickets(self):
		carte = Carte()
		carte.crediterTicket(10)
		self.assertTrue(carte.numberTicket() == 10)

	def test_crediter_carte_tickets_exception(self):
		carte = Carte()
		with self.assertRaises(Exception):
			carte.crediterTicket(-6510)

	def test_value_tickets(self):
		carte = Carte()
		carte.setValueOfTicket(5)
		self.assertTrue(carte.soldeTicket() == 5)

	def test_value_tickets_exception(self):
		carte = Carte()
		carte.setValueOfTicket(5)
		with self.assertRaises(Exception):
			carte.soldeTicket(-5)

	def test_debiter(self):
		carte = Carte()
		carte.crediter(10)
		carte.debiter(2)
		self.assertTrue(carte.solde() == 8)

	def test_debiter_exception(self):
		carte = Carte()
		carte.crediter(10)
		with self.assertRaises(Exception):
			carte.debiter(12)

	def test_debiter_tickets_un_ticket_retire(self):
		carte = Carte()
		carte.crediter(100)
		carte.crediterTicket(2)
		carte.setValueOfTicket(10)
		carte.debiterTicket(16)
		self.assertTrue(carte.numberTicket() == 1)

	def test_debiter_tickets_verifier_solde(self):
		carte = Carte()
		carte.crediter(100)
		carte.crediterTicket(2)
		carte.setValueOfTicket(10)
		carte.debiterTicket(16)
		self.assertTrue(carte.solde() == 94)

	def test_debiter_tickets_quand_zero_tickets_sur_la_carte(self):
		carte = Carte()
		carte.crediter(100)
		carte.crediterTicket(0)
		carte.setValueOfTicket(10)
		carte.debiterTicket(12)
		self.assertTrue(carte.solde() == 88)

	def test_debiter_tickets_quand_plus_de_monnaie(self):
		carte = Carte()
		carte.crediter(10)
		carte.crediterTicket(2)
		carte.setValueOfTicket(10)
		with self.assertRaises(Exception):
			carte.debiterTicket(21)
