# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 09:13:59 2021

@author: Arnaud
"""

import mysql.connector

connexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="Runtrack1"
    )

curseur = connexion.cursor()

request = "INSERT INTO Auteur (nom, prenom) VALUES ('Chancellor', 'Henry')"
curseur.execute(request)
request = "INSERT INTO Auteur (nom, prenom) VALUES ('Egémar', 'Béatrice')"
curseur.execute(request)
request = "INSERT INTO Auteur (nom, prenom) VALUES ('Harrison', 'Lisi')"
curseur.execute(request)
request = "INSERT INTO Auteur (nom, prenom) VALUES ('Ibbotson', 'Eva')"
curseur.execute(request)
request = "INSERT INTO Auteur (nom, prenom) VALUES ('Cluzeau', 'Nicolas')"
curseur.execute(request)

request = "INSERT INTO Livre (titre, auteur_id) VALUES ('extraordinaires aventures de Tom Scatterhorn (Les)', '1')"
curseur.execute(request)
request = "INSERT INTO Livre (titre, auteur_id) VALUES ('L'eau des anges', '2')"
curseur.execute(request)
request = "INSERT INTO Livre (titre, auteur_id) VALUES ('Lucas et les Krapouillos', '2')"
curseur.execute(request)
request = "INSERT INTO Livre (titre, auteur_id) VALUES ('fard et le poison (Le)', '2')"
curseur.execute(request)
request = "INSERT INTO Livre (titre, auteur_id) VALUES ('Quand on parle du loup', '3')"
curseur.execute(request)
request = "INSERT INTO Livre (titre, auteur_id) VALUES ('Monster high', '3')"
curseur.execute(request)
request = "INSERT INTO Livre (titre, auteur_id) VALUES ('Radicalement vôtre', '3')"
curseur.execute(request)
request = "INSERT INTO Livre (titre, auteur_id) VALUES ('L'étoile de Kazan', '4')"
curseur.execute(request)
request = "INSERT INTO Livre (titre, auteur_id) VALUES ('Un chien pour toujours', '4')"
curseur.execute(request)
request = "INSERT INTO Livre (titre, auteur_id) VALUES ('Recherche sorcière désespérément', '4')"
curseur.execute(request)
request = "INSERT INTO Livre (titre, auteur_id) VALUES ('Avant les ténèbres', '5')"
curseur.execute(request)
request = "INSERT INTO Livre (titre, auteur_id) VALUES ('Lame de corsaire', '5')"
curseur.execute(request)
request = "INSERT INTO Livre (titre, auteur_id) VALUES ('Chasses olympiques', '5')"
curseur.execute(request)


# personnes = curseur.fetchall()

# for personne in personnes:
#     print(personne)
    
connexion.close()
curseur.close()
