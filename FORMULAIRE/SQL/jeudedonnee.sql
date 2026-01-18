-- ---------------------------
-- Jeu de test pour la bibliothèque
-- ---------------------------

-- Auteurs
INSERT INTO public.auteur (nom) VALUES
('J.K. Rowling'),
('J.R.R. Tolkien'),
('Isaac Asimov'),
('Frank Herbert'),
('Suzanne Collins');

-- Genres
INSERT INTO public.genre (nom) VALUES
('Fantasy'),
('Science-Fiction'),
('Policier'),
('Jeunesse'),
('Aventure');

-- Éditeurs
INSERT INTO public.editeur (nom) VALUES
('Gallimard'),
('Hachette'),
('Bragelonne');

-- Séries
INSERT INTO public.serie (nom) VALUES
('Harry Potter'),
('Le Seigneur des Anneaux'),
('Fondation'),
('Dune'),
('Hunger Games');

-- Livres
INSERT INTO public.livre (titre, resume, annee, serie_id) VALUES
('Harry Potter à l’école des sorciers', 'Un jeune sorcier découvre ses pouvoirs.', 1997, 1),
('La Communauté de l’Anneau', 'Une quête pour détruire un anneau maléfique.', 1954, 2),
('Fondation', 'La chute annoncée d’un empire galactique.', 1951, 3),
('Dune', 'Une planète désertique au cœur du pouvoir.', 1965, 4),
('Hunger Games', 'Un jeu télévisé mortel dans un futur dystopique.', 2008, 5);

-- Livres <-> Auteurs
INSERT INTO public.livre_auteur (livre_id, auteur_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

-- Livres <-> Genres
INSERT INTO public.livre_genre (livre_id, genre_id) VALUES
(1, 1),
(1, 4),
(2, 1),
(2, 5),
(3, 2),
(4, 2),
(4, 5),
(5, 4),
(5, 5);

-- Éditions
INSERT INTO public.edition (nom, annee, isbn, livre_id, editeur_id) VALUES
('Edition originale', 1997, '9780747532699', 1, 1),
('Edition poche', 2001, '9782266286264', 2, 2),
('Edition collector', 1951, '9782070360536', 3, 1),
('Edition intégrale', 1965, '9782266320487', 4, 3),
('Edition jeunesse', 2008, '9782013237392', 5, 2);

-- Amis
INSERT INTO public.ami (nom, telephone, ecole) VALUES
('Alice Martin', '0600000001', 'Sorbonne'),
('Lucas Bernard', '0600000002', 'ENS'),
('Emma Dubois', '0600000003', 'Polytechnique'),
('Hugo Petit', '0600000004', 'Université Lyon');

-- Exemplaires
INSERT INTO public.exemplaire (etat, edition_id, ami_id) VALUES
('Neuf', 1, NULL),
('Bon', 1, 1),
('Très Bon', 2, NULL),
('Mauvais', 2, 2),
('Bon', 3, NULL),
('Très Bon', 4, NULL),
('Neuf', 5, 3);
