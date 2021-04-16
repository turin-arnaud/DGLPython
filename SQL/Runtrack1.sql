CREATE DATABASE runtrack1;

USE runtrack1

CREATE TABLE Auteur(
    
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(30),
    prenom VARCHAR(30),
    
    )
	
CREATE TABLE Livre(

	id INT PRIMARY KEY AUTO_INCREMENT,
	titre VARCHAR(100)
	auteur_id INT
	
	)