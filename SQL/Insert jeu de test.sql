INSERT INTO Ami (nom, telephone, ecole) VALUES
('Lucas Martin','0600000001','INSA Toulouse'),
('Emma Dupont','0600000002','UT1 Capitole'),
('Thomas Leroy','0600000003','IUT Blagnac'),
('Sarah Bernard','0600000004','Paul Sabatier'),
('Hugo Petit','0600000005','UT2J'),
('Julie Moreau','0600000006','INP ENSEEIHT'),
('Antoine Roux','0600000007','IUT Rodez'),
('Camille Fournier','0600000008','UT1 Capitole'),
('Nicolas Girard','0600000009','INSA Toulouse'),
('Laura Andre','0600000010','Paul Sabatier'),
('Maxime Garcia','0600000011','UT2J'),
('Chloe Lopez','0600000012','IUT Blagnac'),
('Julien Faure','0600000013','INP'),
('Manon Riviere','0600000014','UT1 Capitole'),
('Alexis Payet','0600000015','INSA Toulouse'),
('Lucie Colin','0600000016','Paul Sabatier'),
('Romain Vidal','0600000017','IUT Rodez'),
('Elise Brun','0600000018','UT2J'),
('Benjamin Hoarau','0600000019','INP'),
('Marine Arnaud','0600000020','UT1 Capitole');

INSERT INTO Exemplaire (etat, ami_id) VALUES
('Tres bon',1),('Bon',2),('Mauvais',3),('Tres bon',4),('Bon',5),
('Tres bon',6),('Mauvais',7),('Bon',8),('Tres bon',9),('Bon',10),
('Tres bon',11),('Mauvais',12),('Bon',13),('Tres bon',14),('Bon',15),
('Tres bon',16),('Mauvais',17),('Bon',18),('Tres bon',19),('Bon',20);

INSERT INTO Editeur (nom) VALUES
('Gallimard'),('Pocket'),('Flammarion'),('Actes Sud'),('Folio'),
('Albin Michel'),('Hachette'),('Seuil'),('Nathan'),('Plon'),
('Robert Laffont'),('Michel Lafon'),('Belfond'),('XO Editions'),
('Grasset'),('Editis'),('Bragelonne'),('Eyrolles'),('Dunod'),('Casterman');

INSERT INTO Edition (nom, annee, isbn, editeur_id, exemplaire_id) VALUES
('Edition 1',2001,'9780000000001',1,1),
('Edition 2',2002,'9780000000002',2,2),
('Edition 3',2003,'9780000000003',3,3),
('Edition 4',2004,'9780000000004',4,4),
('Edition 5',2005,'9780000000005',5,5),
('Edition 6',2006,'9780000000006',6,6),
('Edition 7',2007,'9780000000007',7,7),
('Edition 8',2008,'9780000000008',8,8),
('Edition 9',2009,'9780000000009',9,9),
('Edition 10',2010,'9780000000010',10,10),
('Edition 11',2011,'9780000000011',11,11),
('Edition 12',2012,'9780000000012',12,12),
('Edition 13',2013,'9780000000013',13,13),
('Edition 14',2014,'9780000000014',14,14),
('Edition 15',2015,'9780000000015',15,15),
('Edition 16',2016,'9780000000016',16,16),
('Edition 17',2017,'9780000000017',17,17),
('Edition 18',2018,'9780000000018',18,18),
('Edition 19',2019,'9780000000019',19,19),
('Edition 20',2020,'9780000000020',20,20);

INSERT INTO Serie (nom) VALUES
('Harry Potter'),('Le Seigneur des Anneaux'),('Fondation'),
('Dune'),('Hunger Games'),('Game of Thrones'),
('Eragon'),('Wheel of Time'),('Mistborn'),('Percy Jackson'),
('Narnia'),('The Witcher'),('Metro'),('Assassins Creed'),
('Star Wars'),('Alien'),('Blade Runner'),
('Sherlock Holmes'),('Dark Tower'),('Discworld');

INSERT INTO Auteur (nom) VALUES
('J.K. Rowling'),('J.R.R. Tolkien'),('Isaac Asimov'),
('Frank Herbert'),('Suzanne Collins'),('George R.R. Martin'),
('Christopher Paolini'),('Robert Jordan'),('Brandon Sanderson'),
('Rick Riordan'),('C.S. Lewis'),('Andrzej Sapkowski'),
('Dmitry Glukhovsky'),('Oliver Bowden'),('George Lucas'),
('Alan Dean Foster'),('Philip K. Dick'),
('Arthur Conan Doyle'),('Stephen King'),('Terry Pratchett');

INSERT INTO Genre (nom) VALUES
('Fantasy'),('Science-fiction'),('Aventure'),('Dystopie'),
('Policier'),('Thriller'),('Horreur'),('Historique'),
('Romance'),('Jeunesse'),('Epique'),('Politique'),
('Philosophie'),('Cyberpunk'),('Post-apocalyptique'),
('Mythologie'),('Steampunk'),('Satire'),('Drame'),('Classique');

INSERT INTO Livre (titre, resume, annee, serie_id, edition_id) VALUES
('Livre 1','Resume 1',2001,1,1),
('Livre 2','Resume 2',2002,2,2),
('Livre 3','Resume 3',2003,3,3),
('Livre 4','Resume 4',2004,4,4),
('Livre 5','Resume 5',2005,5,5),
('Livre 6','Resume 6',2006,6,6),
('Livre 7','Resume 7',2007,7,7),
('Livre 8','Resume 8',2008,8,8),
('Livre 9','Resume 9',2009,9,9),
('Livre 10','Resume 10',2010,10,10),
('Livre 11','Resume 11',2011,11,11),
('Livre 12','Resume 12',2012,12,12),
('Livre 13','Resume 13',2013,13,13),
('Livre 14','Resume 14',2014,14,14),
('Livre 15','Resume 15',2015,15,15),
('Livre 16','Resume 16',2016,16,16),
('Livre 17','Resume 17',2017,17,17),
('Livre 18','Resume 18',2018,18,18),
('Livre 19','Resume 19',2019,19,19),
('Livre 20','Resume 20',2020,20,20);

INSERT INTO LivreAuteur (livre_id, auteur_id) VALUES
(1,1),(2,2),(3,3),(4,4),(5,5),
(6,6),(7,7),(8,8),(9,9),(10,10),
(11,11),(12,12),(13,13),(14,14),(15,15),
(16,16),(17,17),(18,18),(19,19),(20,20);

INSERT INTO LivreGenre (livre_id, genre_id) VALUES
(1,1),(2,1),(3,2),(4,2),(5,4),
(6,1),(7,1),(8,1),(9,1),(10,10),
(11,10),(12,15),(13,3),(14,3),(15,2),
(16,2),(17,14),(18,5),(19,7),(20,18);
