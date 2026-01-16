BEGIN;

-- =========================
-- SERIE (30)
-- =========================
INSERT INTO Série (Nom) VALUES
('Harry Potter'),
('Le Seigneur des Anneaux'),
('Fondation'),
('Dune'),
('Millénium'),
('Hunger Games'),
('La Roue du Temps'),
('Le Sorceleur'),
('Game of Thrones'),
('Percy Jackson'),
('Les Royaumes du Nord'),
('Assassin Royal'),
('Eragon'),
('La Tour Sombre'),
('Les Robots'),
('Le Disque-Monde'),
('La Quête d’Ewilan'),
('Le Trône de Fer'),
('Chroniques de Narnia'),
('Twilight'),
('Sherlock Holmes'),
('Arsène Lupin'),
('Alex Rider'),
('The Witcher'),
('Metro'),
('Watchmen'),
('The Expanse'),
('Mistborn'),
('Red Rising'),
('La Passe-Miroir');

-- =========================
-- GENRE (30)
-- =========================
INSERT INTO Genre (Nom) VALUES
('Fantasy'),
('Science-fiction'),
('Policier'),
('Thriller'),
('Aventure'),
('Historique'),
('Romance'),
('Jeunesse'),
('Young Adult'),
('Dystopie'),
('Horreur'),
('Fantastique'),
('Épique'),
('Mythologie'),
('Steampunk'),
('Cyberpunk'),
('Anticipation'),
('Enquête'),
('Drame'),
('Humour'),
('Classique'),
('Conte'),
('Uchronie'),
('Politique'),
('Psychologique'),
('Post-apocalyptique'),
('Space Opera'),
('Médiéval'),
('Surnaturel'),
('Espionnage');

-- =========================
-- AUTEUR (30)
-- =========================
INSERT INTO Auteur (Nom) VALUES
('J.K. Rowling'),
('J.R.R. Tolkien'),
('Isaac Asimov'),
('Frank Herbert'),
('Stieg Larsson'),
('Suzanne Collins'),
('Robert Jordan'),
('Andrzej Sapkowski'),
('George R.R. Martin'),
('Rick Riordan'),
('Philip Pullman'),
('Robin Hobb'),
('Christopher Paolini'),
('Stephen King'),
('Terry Pratchett'),
('Pierre Bottero'),
('C.S. Lewis'),
('Agatha Christie'),
('Arthur Conan Doyle'),
('Maurice Leblanc'),
('George Orwell'),
('Aldous Huxley'),
('Neil Gaiman'),
('Dan Brown'),
('Douglas Adams'),
('Andy Weir'),
('Brandon Sanderson'),
('Pierce Brown'),
('Patrick Rothfuss'),
('Margaret Atwood');

-- =========================
-- EDITEUR (30)
-- =========================
INSERT INTO Editeur (Nom) VALUES
('Gallimard'),
('Pocket'),
('Folio'),
('Flammarion'),
('Actes Sud'),
('Albin Michel'),
('Seuil'),
('Hachette'),
('Bragelonne'),
('J’ai Lu'),
('Belfond'),
('Robert Laffont'),
('Plon'),
('Grasset'),
('Michel Lafon'),
('Casterman'),
('Nathan'),
('Bayard'),
('PKJ'),
('XO Éditions'),
('HarperCollins'),
('Penguin Random House'),
('Tor Books'),
('Orbit'),
('Del Rey'),
('Minuit'),
('L’Olivier'),
('Rivages'),
('Points'),
('10/18');

-- =========================
-- AMI (30)
-- =========================
INSERT INTO Ami (Nom, Téléphone, Ecole) VALUES
('Alice Martin','0600000001','Sorbonne'),
('Lucas Bernard','0600000002','ENS'),
('Emma Dubois','0600000003','Polytechnique'),
('Hugo Petit','0600000004','Université Lyon'),
('Chloé Robert','0600000005','Université Lille'),
('Louis Richard','0600000006','Sciences Po'),
('Manon Durand','0600000007','Université Nantes'),
('Nathan Leroy','0600000008','Université Bordeaux'),
('Léa Moreau','0600000009','Université Toulouse'),
('Noah Simon','0600000010','Université Strasbourg'),
('Camille Laurent','0600000011','Université Rennes'),
('Paul Lefèvre','0600000012','Université Grenoble'),
('Sarah Michel','0600000013','Université Paris Cité'),
('Tom Garcia','0600000014','Université Montpellier'),
('Roberto Lopez','0600000015','Université Nice'),
('Maxime Roux','0600000016','Université Angers'),
('Julie Fontaine','0600000017','Université Amiens'),
('Alexandre Muller','0600000018','Université Reims'),
('Clara Nguyen','0600000019','Université Tours'),
('Antoine Perez','0600000020','Université Poitiers'),
('Sophie Bonnet','0600000021','Université Metz'),
('Julien Colin','0600000022','Université Nancy'),
('Marine Fabre','0600000023','Université Avignon'),
('Victor Gauthier','0600000024','Université Pau'),
('Laura Chevalier','0600000025','Université Limoges'),
('Théo Marchand','0600000026','Université Besançon'),
('Eva Perrot','0600000027','Université Troyes'),
('Benjamin Lemoine','0600000028','Université Arras'),
('Océane Renault','0600000029','Université Caen'),
('Romain Blanchard','0600000030','Université Rouen');

-- =========================
-- EXEMPLAIRE (30)
-- =========================
INSERT INTO Exemplaire (Etat, Ami) VALUES
('Très bon',1),('Bon',2),('Mauvais',3),('Très bon',4),('Bon',5),
('Mauvais',6),('Très bon',7),('Bon',8),('Mauvais',9),('Très bon',10),
('Bon',11),('Mauvais',12),('Très bon',13),('Bon',14),('Mauvais',15),
('Très bon',16),('Bon',17),('Mauvais',18),('Très bon',19),('Bon',20),
('Mauvais',21),('Très bon',22),('Bon',23),('Mauvais',24),('Très bon',25),
('Bon',26),('Mauvais',27),('Très bon',28),('Bon',29),('Mauvais',30);

-- =========================
-- EDITION (30)
-- =========================
INSERT INTO Edition (Nom, Année, ISBN, Editeur, Exemplaire) VALUES
('Harry Potter à l’école des sorciers',1998,'9782070584628',1,1),
('La Chambre des secrets',1999,'9782070584642',1,2),
('Le Prisonnier d’Azkaban',2000,'9782070584925',1,3),
('La Coupe de feu',2001,'9782070585205',1,4),
('Les Deux Tours',2002,'9782266286265',2,5),
('Le Retour du Roi',2003,'9782266286272',2,6),
('Fondation',1951,'9782070360536',3,7),
('Dune',1965,'9782266320488',4,8),
('L’Homme bicentenaire',1976,'9782290312357',5,9),
('1984',1949,'9782070368228',6,10),
('Le Meilleur des mondes',1932,'9782253006329',7,11),
('Fahrenheit 451',1953,'9782070415731',8,12),
('Le Trône de fer',1996,'9782290317246',9,13),
('La Voie des rois',2010,'9782811218984',10,14),
('Mistborn',2006,'9782253081821',11,15),
('Red Rising',2014,'9782266265000',12,16),
('Le Nom du vent',2007,'9782352942659',13,17),
('American Gods',2001,'9782290079861',14,18),
('De bons présages',1990,'9782290357815',15,19),
('Le Guide du voyageur galactique',1979,'9782070460557',16,20),
('La Servante écarlate',1985,'9782221249949',17,21),
('Sherlock Holmes',1892,'9782253003175',18,22),
('Arsène Lupin',1907,'9782253006328',19,23),
('Da Vinci Code',2003,'9782709624930',20,24),
('Metro 2033',2005,'9782266260302',21,25),
('Watchmen',1986,'9782809401907',22,26),
('The Expanse',2011,'9782330069993',23,27),
('La Passe-Miroir',2013,'9782070643026',24,28),
('Hunger Games',2008,'9782266182697',25,29),
('Percy Jackson',2005,'9782013226822',26,30);

-- =========================
-- LIVRE (30)
-- =========================
INSERT INTO Livre (Titre, Résumé, Année, Série, Genre, Auteur, Edition) VALUES
('Harry Potter 1','Un jeune sorcier découvre la magie',1997,1,1,1,1),
('Harry Potter 2','La chambre des secrets est ouverte',1998,1,1,1,2),
('Harry Potter 3','Un prisonnier s’évade d’Azkaban',1999,1,1,1,3),
('Harry Potter 4','Un tournoi dangereux',2000,1,1,1,4),
('Les Deux Tours','La communauté est divisée',1954,2,13,2,5),
('Le Retour du Roi','La fin de la guerre',1955,2,13,2,6),
('Fondation','Un empire en déclin',1951,3,2,3,7),
('Dune','Une planète désertique',1965,4,2,4,8),
('1984','Un monde totalitaire',1949,NULL,10,21,10),
('Fahrenheit 451','Brûler les livres',1953,NULL,10,22,12),
('Le Trône de fer','Jeux de pouvoir',1996,9,13,9,13),
('Mistborn','Un empire tyrannique',2006,28,2,27,15),
('Red Rising','Révolte sociale',2014,29,10,28,16),
('Le Nom du vent','La vie d’un magicien',2007,NULL,1,29,17),
('American Gods','Anciens dieux modernes',2001,NULL,12,23,18),
('De bons présages','Fin du monde imminente',1990,NULL,20,15,19),
('Guide galactique','Humour SF',1979,NULL,20,25,20),
('La Servante écarlate','Dictature religieuse',1985,NULL,10,30,21),
('Sherlock Holmes','Enquêtes célèbres',1892,21,18,19,22),
('Arsène Lupin','Gentleman cambrioleur',1907,22,18,20,23),
('Da Vinci Code','Thriller religieux',2003,NULL,4,24,24),
('Metro 2033','Survie post-apo',2005,25,26,26,25),
('Watchmen','Super-héros réalistes',1986,NULL,24,27,26),
('The Expanse','Conflits spatiaux',2011,27,27,28,27),
('La Passe-Miroir','Monde fragmenté',2013,30,1,16,28),
('Hunger Games','Jeux mortels',2008,6,10,6,29),
('Percy Jackson','Mythologie moderne',2005,10,14,10,30),
('Les Robots','IA et éthique',1950,15,2,3,9),
('Assassin Royal','Apprentissage royal',1995,12,1,12,14),
('Chroniques de Narnia','Monde magique',1950,19,22,17,11);

-- =========================
-- LIVREAUTEUR (30)
-- =========================
INSERT INTO LivreAuteur (idLivre, idAuteur) VALUES
(1, 1),(2, 1),(3, 1),(4, 1),(5, 2),(6, 2),(7, 3),(8, 4),
(9, 21),(10, 22),(11, 9),(12, 27),(13, 28),(14, 29),(15, 23),
(16, 15),(17, 25),(18, 30),(19, 19),(20, 20),(21, 24),(22, 26),
(23, 27),(24, 28),(25, 16),(26, 6),(27, 10),(28, 3),(29, 12),(30, 17);

-- =========================
-- LIVREGENRE (30)
-- =========================
INSERT INTO LivreGenre (idLivre, idGenre) VALUES
(1,1),(2,1),(3,1),(4,1),(5,13),(6,13),(7,2),(8,2),(9,10),(10,10),
(11,13),(12,2),(13,10),(14,1),(15,12),(16,20),(17,20),(18,10),(19,18),
(20,18),(21,4),(22,26),(23,24),(24,27),(25,1),(26,10),(27,14),(28,2),(29,1),(30,22);

COMMIT;
