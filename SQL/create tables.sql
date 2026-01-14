CREATE TABLE Serie (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(255) NOT NULL
);

CREATE TABLE Genre (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(255) NOT NULL
);

CREATE TABLE Auteur (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(255) NOT NULL
);

CREATE TABLE Editeur (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(255) NOT NULL
);

CREATE TABLE Ami (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    telephone VARCHAR(10) NOT NULL,
    ecole VARCHAR(255) NOT NULL
);

CREATE TABLE Exemplaire (
    id SERIAL PRIMARY KEY,
    etat VARCHAR(20) NOT NULL CHECK (etat IN ('Tres bon', 'Bon', 'Mauvais')),
    ami_id INTEGER NOT NULL,
    FOREIGN KEY (ami_id) REFERENCES Ami(id)
);

CREATE TABLE Edition (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    annee INTEGER NOT NULL,
    isbn VARCHAR(13) NOT NULL,
    editeur_id INTEGER NOT NULL,
    exemplaire_id INTEGER NOT NULL,
    FOREIGN KEY (editeur_id) REFERENCES Editeur(id),
    FOREIGN KEY (exemplaire_id) REFERENCES Exemplaire(id)
);

CREATE TABLE Livre (
    id SERIAL PRIMARY KEY,
    titre VARCHAR(255) NOT NULL,
    resume VARCHAR(255) NOT NULL,
    annee INTEGER,
    serie_id INTEGER,
    edition_id INTEGER NOT NULL,
    FOREIGN KEY (serie_id) REFERENCES Serie(id),
    FOREIGN KEY (edition_id) REFERENCES Edition(id)
);

CREATE TABLE LivreAuteur (
    livre_id INTEGER NOT NULL,
    auteur_id INTEGER NOT NULL,
    PRIMARY KEY (livre_id, auteur_id),
    FOREIGN KEY (livre_id) REFERENCES Livre(id) ON DELETE CASCADE,
    FOREIGN KEY (auteur_id) REFERENCES Auteur(id) ON DELETE CASCADE
);

CREATE TABLE LivreGenre (
    livre_id INTEGER NOT NULL,
    genre_id INTEGER NOT NULL,
    PRIMARY KEY (livre_id, genre_id),
    FOREIGN KEY (livre_id) REFERENCES Livre(id) ON DELETE CASCADE,
    FOREIGN KEY (genre_id) REFERENCES Genre(id) ON DELETE CASCADE
);
