SELECT * FROM Livre;

SELECT nom, telephone FROM Ami;

SELECT titre, annee FROM Livre
WHERE annee > 2010;

SELECT l.titre, a.nom AS auteur
FROM Livre l
JOIN LivreAuteur la ON l.id = la.livre_id
JOIN Auteur a ON la.auteur_id = a.id;

SELECT l.titre, g.nom AS genre
FROM Livre l
JOIN LivreGenre lg ON l.id = lg.livre_id
JOIN Genre g ON lg.genre_id = g.id;

SELECT a.nom AS auteur, COUNT(la.livre_id) AS nb_livres
FROM Auteur a
JOIN LivreAuteur la ON a.id = la.auteur_id
GROUP BY a.nom
ORDER BY nb_livres DESC;

SELECT g.nom AS genre, COUNT(lg.livre_id) AS nb_livres
FROM Genre g
JOIN LivreGenre lg ON g.id = lg.genre_id
GROUP BY g.nom
ORDER BY nb_livres DESC;

SELECT l.titre
FROM Livre l
LEFT JOIN Serie s ON l.serie_id = s.id
WHERE s.id IS NULL;

SELECT l.titre, am.nom AS possesseur
FROM Livre l
JOIN Edition e ON l.edition_id = e.id
JOIN Exemplaire ex ON e.exemplaire_id = ex.id
JOIN Ami am ON ex.ami_id = am.id
WHERE ex.etat = 'Tres bon';

WITH livres_amis AS (
    SELECT am.id AS ami_id, g.id AS genre_id
    FROM Ami am
    JOIN Exemplaire ex ON am.id = ex.ami_id
    JOIN Edition e ON ex.id = e.exemplaire_id
    JOIN Livre l ON e.id = l.edition_id
    JOIN LivreGenre lg ON l.id = lg.livre_id
    JOIN Genre g ON lg.genre_id = g.id
)
SELECT ami_id, COUNT(DISTINCT genre_id) AS nb_genres
FROM livres_amis
GROUP BY ami_id;


SELECT nom
FROM Auteur
WHERE id = (
    SELECT auteur_id
    FROM LivreAuteur
    GROUP BY auteur_id
    ORDER BY COUNT(livre_id) DESC
    LIMIT 1
);

SELECT
    l.titre,
    string_agg(DISTINCT a.nom, ', ') AS auteurs,
    string_agg(DISTINCT g.nom, ', ') AS genres,
    ed.nom AS editeur,
    e.annee
FROM Livre l
JOIN LivreAuteur la ON l.id = la.livre_id
JOIN Auteur a ON la.auteur_id = a.id
JOIN LivreGenre lg ON l.id = lg.livre_id
JOIN Genre g ON lg.genre_id = g.id
JOIN Edition e ON l.edition_id = e.id
JOIN Editeur ed ON e.editeur_id = ed.id
GROUP BY l.titre, ed.nom, e.annee
ORDER BY e.annee DESC;


SELECT
    g.nom AS genre,
    COUNT(lg.livre_id) AS nb_livres
FROM Genre g
JOIN LivreGenre lg ON g.id = lg.genre_id
GROUP BY g.nom
HAVING COUNT(lg.livre_id) >= 2
ORDER BY nb_livres DESC;


SELECT DISTINCT
    a.nom AS auteur
FROM Auteur a
JOIN LivreAuteur la ON a.id = la.auteur_id
JOIN LivreGenre lg ON la.livre_id = lg.livre_id
JOIN Genre g ON lg.genre_id = g.id
WHERE g.nom = 'Fantasy'
ORDER BY a.nom;


SELECT
    l.titre,
    am.nom AS ami,
    ex.etat
FROM Livre l
JOIN Edition ed ON l.edition_id = ed.id
JOIN Exemplaire ex ON ed.exemplaire_id = ex.id
JOIN Ami am ON ex.ami_id = am.id
WHERE ex.etat <> 'Tres bon'
ORDER BY am.nom;


SELECT
    ed.nom AS editeur,
    ROUND(AVG(EXTRACT(YEAR FROM CURRENT_DATE) - e.annee), 1) AS age_moyen
FROM Edition e
JOIN Editeur ed ON e.editeur_id = ed.id
GROUP BY ed.nom
ORDER BY age_moyen DESC;


WITH stats AS (
    SELECT
        a.nom,
        COUNT(la.livre_id) AS nb_livres
    FROM Auteur a
    JOIN LivreAuteur la ON a.id = la.auteur_id
    GROUP BY a.nom
)
SELECT *
FROM stats
WHERE nb_livres = (SELECT MAX(nb_livres) FROM stats);


SELECT
    am.nom AS ami,
    COUNT(l.id) AS nb_livres
FROM Ami am
LEFT JOIN Exemplaire ex ON am.id = ex.ami_id
LEFT JOIN Edition e ON ex.id = e.exemplaire_id
LEFT JOIN Livre l ON e.id = l.edition_id
GROUP BY am.nom
ORDER BY nb_livres DESC;

WITH livres_par_ami AS (
    SELECT
        am.id AS ami_id,
        am.nom AS ami,
        l.id AS livre_id,
        l.titre,
        e.annee AS annee_edition,
        g.id AS genre_id
    FROM Ami am
    LEFT JOIN Exemplaire ex ON am.id = ex.ami_id
    LEFT JOIN Edition e ON ex.id = e.exemplaire_id
    LEFT JOIN Livre l ON e.id = l.edition_id
    LEFT JOIN LivreGenre lg ON l.id = lg.livre_id
    LEFT JOIN Genre g ON lg.genre_id = g.id
),
stats AS (
    SELECT
        ami_id,
        ami,
        COUNT(DISTINCT livre_id) AS nb_livres,
        COUNT(DISTINCT genre_id) AS nb_genres,
        ROUND(AVG(annee_edition), 1) AS annee_moyenne
    FROM livres_par_ami
    GROUP BY ami_id, ami
),
livre_plus_recent AS (
    SELECT DISTINCT ON (ami_id)
        ami_id,
        titre AS livre_recent
    FROM livres_par_ami
    WHERE annee_edition IS NOT NULL
    ORDER BY ami_id, annee_edition DESC
)
SELECT
    s.ami,
    s.nb_livres,
    s.nb_genres,
    s.annee_moyenne,
    lpr.livre_recent
FROM stats s
LEFT JOIN livre_plus_recent lpr ON s.ami_id = lpr.ami_id
ORDER BY s.nb_livres DESC, s.ami;
