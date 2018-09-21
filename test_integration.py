#Defossez Gautier
#Valette Henri

import unittest
from carte import Carte
from caisse import Caisse

class TestIntegration(unittest.TestCase):

	def test_init(self):
		caisse = Caisse()
		carte = Carte()
		caisse.insererCarte(carte)
		self.assertTrue(caisse.hasCarte())

	def test_paiement(self):
		caisse = Caisse()
		carte = Carte()
		carte.crediter(6)
		caisse.insererCarte(carte)
		caisse.paiement(5)
		self.assertTrue(carte.solde() == 1)

	def test_paiement_exception(self):
		caisse = Caisse()
		carte = Carte()
		with self.assertRaises(Exception):
			caisse.paiement(5)

	def test_paiement_ticket_sans_ticket(self):
		caisse = Caisse()
		carte = Carte()
		carte.crediter(6)
		caisse.insererCarte(carte)
		caisse.paiementTicket(5)
		self.assertTrue(carte.solde() == 1)

	def test_paiement_ticket_avec_ticket(self):
		caisse = Caisse()
		carte = Carte()
		carte.crediterTicket(2)
		carte.setValueOfTicket(5)
		carte.crediter(6)
		caisse.insererCarte(carte)
		caisse.paiementTicket(5)
		self.assertTrue(carte.solde() == 6)

	def test_paiement_ticket_exception(self):
		caisse = Caisse()
		carte = Carte()
		with self.assertRaises(Exception):
			caisse.paiementTicket(5)

	def test_consulter_solde(self):
		caisse = Caisse()
		carte = Carte()
		caisse.insererCarte(carte)
		carte.crediter(12)
		self.assertTrue(caisse.solde() == 12)


	def test_consulter_solde_nombre_ticket(self):
		caisse = Caisse()
		carte = Carte()
		carte.crediterTicket(5)
		caisse.insererCarte(carte)
		self.assertTrue(caisse.numberTicket() == 5)

	def test_consulter_solde_ticket(self):
		caisse = Caisse()
		carte = Carte()
		caisse.insererCarte(carte)
		carte.setValueOfTicket(5)
		self.assertTrue(caisse.soldeTicket() == 5)

