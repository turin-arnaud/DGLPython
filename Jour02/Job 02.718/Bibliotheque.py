# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 11:14:46 2021

@author: Arnaud
"""

from Livre import Livre, Auteur
from Personne import Personne

class Bibliotheque:
    
    def __init__(self, nom, catalogue = {}):
        self.nom = nom
        self.catalogue = catalogue # un dictionnaire {Livre : quantité (int)}
        
    def inventaire(self):
        for chaqueLivre in self.catalogue:
            print(chaqueLivre.titre, ":", self.catalogue[chaqueLivre])
            
        
    def acheterLivre(self, auteur, titreLivre, quantité):
        # Si le livre existe bien dans l’oeuvre de l’auteur
        if auteur.existe_dans_oeuvre(titreLivre): 
            nouveauLivre = Livre(titreLivre, auteur)
            # S'il existe déja des exemplaire de ce livre dans la biblioteque
            # on ajoute la quantité acheté
            if nouveauLivre in self.catalogue:
                 self.catalogue[nouveauLivre] += quantité

            # sinon on ajoute le livre au catalogue
            else:
                self.catalogue[nouveauLivre] = quantité
                
    def louer(self, client, titreLivre):
        for livre in self.catalogue:
            # Si le livre est en stock 
            if livre.titre == titreLivre and self.catalogue[livre] > 0:
                #ajouter ce livre à la collection de livre du client
                client.collection.append(livre)
                # mettre à jour la quantité de ce livre dans la bibliothèque
                self.catalogue[livre] -= 1
                break
            
    def rendreLivres(self, client):
        for livre in client.collection :
            self.catalogue[livre] += 1
        client.collection = []
            
            
    
            
class Client(Personne):
    
    def __init__(self, nom, prenom):
        Personne.__init__(self, nom, prenom)
        self.collection = [] # Une liste de livre
    
    # affiche dans le terminal les titres des livres en possession du client
    def inventaire(self): 
        print([livre.titre for livre in self.collection])


A1 = Auteur("Rolling", "J. K.")
for i in range(1, 8):
    A1.ecrireUnLivre("Harry Potter " + str(i))

# A1.listerOeuvre()
# print(A1.existe_dans_oeuvre("Harry Potter 1"))
# print(A1.existe_dans_oeuvre("Harry Potter 8"))

maBibliotheque = Bibliotheque("Alexandrie")
maBibliotheque.acheterLivre(A1, "Harry Potter 1", 12)
#B1.afficher_catalogue()
maBibliotheque.acheterLivre(A1, "Harry Potter 2", 6)
#B1.afficher_catalogue()
maBibliotheque.acheterLivre(A1, "Harry Potter 1", 1)
maBibliotheque.inventaire()

client1 = Client("Honnold", "Alex")
maBibliotheque.louer(client1, "Harry Potter 1")
maBibliotheque.inventaire()
client1.inventaire()

maBibliotheque.louer(client1, "Harry Potter 2")
maBibliotheque.inventaire()
client1.inventaire()

maBibliotheque.rendreLivres(client1)
maBibliotheque.inventaire()
client1.inventaire()