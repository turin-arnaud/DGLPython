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

request = "INSERT INTO Auteur (nom, prenom) VALUES (%s, %s)"
val = [
       ('Chancellor', 'Henry'),
       ('Egémar', 'Béatrice'),
       ('Harrison', 'Lisi'),
       ('Ibbotson', 'Eva'),
       ('Cluzeau', 'Nicolas')
       ]

curseur.executemany(request, val)

request = "INSERT INTO Livre (titre, auteur_id) VALUES (%s, %s)"
val = [
       ('extraordinaires aventures de Tom Scatterhorn (Les)', '1'),
       ('Lucas et les Krapouillos', '2'),
       ('fard et le poison (Le)', '2'),
       ('Quand on parle du loup', '3'),
       ('Monster high', '3'),
       ('Radicalement vôtre', '3'),
       ('Un chien pour toujours', '4'),
       ('Recherche sorcière désespérément', '4'),
       ('Avant les ténèbres', '5'),
       ('Lame de corsaire', '5'),
       ('Chasses olympiques', '5')
       ]
curseur.executemany(request, val)

connexion.commit()
    
connexion.close()
curseur.close()
