#Defossez Gautier
#Valette Henri

import unittest
from caisse import Caisse
from mockito import *

class TestCaisse(unittest.TestCase):

	def test_init(self):
		caisse = Caisse()
		carte = mock()
		caisse.insererCarte(carte)
		self.assertTrue(caisse.hasCarte())

	def test_paiement(self):
		caisse = Caisse()
		carte = mock()
		caisse.insererCarte(carte)
		caisse.paiement(5)
		verify(carte).debiter(5)

	def test_paiement_exception(self):
		caisse = Caisse()
		carte = mock()
		with self.assertRaises(Exception):
			caisse.paiement(5)

	def test_paiement_ticket(self):
		caisse = Caisse()
		carte = mock()
		caisse.insererCarte(carte)
		caisse.paiementTicket(5)
		verify(carte).debiterTicket(5)

	def test_paiement_ticket_exception(self):
		caisse = Caisse()
		carte = mock()
		with self.assertRaises(Exception):
			caisse.paiementTicket(5)

	def test_consulter_solde(self):
		caisse = Caisse()
		carte = mock()
		caisse.insererCarte(carte)
		self.assertTrue(caisse.solde() == carte.solde())

	def test_consulter_solde_exception(self):
		caisse = Caisse()
		carte = mock()
		with self.assertRaises(Exception):
			caisse.solde()

	def test_consulter_solde_ticket(self):
		caisse = Caisse()
		carte = mock()
		caisse.insererCarte(carte)
		self.assertTrue(caisse.soldeTicket() == carte.soldeTicket())

	def test_consulter_solde_ticket_exception(self):
		caisse = Caisse()
		carte = mock()
		with self.assertRaises(Exception):
			caisse.soldeTicket()
		
	def test_consulter_solde_number_tickets(self):
		caisse = Caisse()
		carte = mock()
		caisse.insererCarte(carte)
		self.assertTrue(caisse.numberTicket() == carte.numberTicket())

	def test_consulter_number_ticket_exception(self):
		caisse = Caisse()
		carte = mock()
		with self.assertRaises(Exception):
			caisse.numberTicket()
		

