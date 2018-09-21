#TDD : avec dépendances

##Authors
Defossez Gautier
Valette Henri

###Question 1


###Question 2
Caisse : 
	- insererCarte(carte)		//on insere la carte dans la caisse
	- paiement(valeur)		//on paye le repas
	- paiementTicket(valeur)	//on paye le repas par ticket
	- solde()					//on consulte le solde sur la carte
	- soldeTicket()	//on consulte le solde d'un ticket sur la carte
	- numberTicket()	//on souhaite obtenir le nombre de tickets sur la carte
Une exeption apparait lorsqu'aucune carte n'est insérée dans la caisse

###Question 3

cf : `test_caisse.py` et `caisse.py`

###Question 4
Carte :
	- crediter(valeur)	//ajouter argent sur la carte
	- solde()	//solde sur la carte
	- crediterTicket(valeur) //ajouter tickets sur la carte
	- numberTicket()	//nombre de tickets sur la carte
	- setValueOfTicket(valeur) //met la valeur d'un ticket
	- soldeTicket()		//solde d'un ticket sur la carte
	- debiter(valeur)	//débiter de l'argent sur la carte
	- debiterTicket(valeur)	//debiter des tickets sur la carte


###Question 5

cf : `test_integration.py`