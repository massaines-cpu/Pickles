# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional, Literal
import psycopg

app = FastAPI(title="API Bibliothèque")


# ----------------------------
# MODELS (Pydantic)
# ----------------------------

class SerieModel(BaseModel):
    nom: str


class GenreModel(BaseModel):
    nom: str


class AuteurModel(BaseModel):
    nom: str


class EditeurModel(BaseModel):
    nom: str


class AmiModel(BaseModel):
    nom: str
    telephone: str
    ecole: str


class LivreModel(BaseModel):
    """
    Modèle complet pour ajouter un livre depuis le front
    """
    titre: str
    resume: str
    annee: int
    auteurs: List[str]
    genres: List[str]
    serie: str
    edition: str
    editeur: str
    etat: Literal['Tres bon', 'Bon', 'Mauvais']
    exemplaires: int
    isbn: str


# ----------------------------
# FONCTIONS UTILITAIRES
# ----------------------------

def get_conn():
    """Crée une connexion à la base PostgreSQL (psycopg3)"""
    return psycopg.connect(
        host="127.0.0.1",
        dbname="PicklesBase",
        user="postgres",
        password="Dompte2024!_!"
    )


def get_or_create(cursor, table, nom):
    """Cherche une entrée dans table par nom, sinon l'insère et retourne l'id"""
    cursor.execute(f"SELECT id FROM {table} WHERE nom = %s", (nom,))
    row = cursor.fetchone()
    if row:
        return row[0]
    cursor.execute(f"INSERT INTO {table} (nom) VALUES (%s) RETURNING id", (nom,))
    return cursor.fetchone()[0]


# ----------------------------
# AJOUTER UN LIVRE COMPLET
# ----------------------------

@app.post("/livre/complet")
def ajout_livre(data: LivreModel):
    """Ajoute un livre avec tous ses liens et exemplaires"""
    conn = get_conn()
    cursor = conn.cursor()

    try:
        # --- Série ---
        serie_id = get_or_create(cursor, "Serie", data.serie)

        # --- Editeur ---
        editeur_id = get_or_create(cursor, "Editeur", data.editeur)

        # --- Premier exemplaire (nécessaire pour Edition) ---
        cursor.execute(
            "INSERT INTO Exemplaire (etat, ami_id, edition_id) VALUES (%s, %s, NULL) RETURNING id",
            (data.etat, 1)  # ami_id = 1 par défaut pour test
        )
        ex_id = cursor.fetchone()[0]

        # --- Edition ---
        cursor.execute(
            "INSERT INTO Edition (nom, annee, isbn, editeur_id, exemplaire_id) "
            "VALUES (%s, %s, %s, %s, %s) RETURNING id",
            (data.edition, data.annee, data.isbn, editeur_id, ex_id)
        )
        edition_id = cursor.fetchone()[0]

        # --- Mise à jour du premier exemplaire pour pointer sur l'édition ---
        cursor.execute(
            "UPDATE Exemplaire SET edition_id = %s WHERE id = %s",
            (edition_id, ex_id)
        )

        # --- Livre ---
        cursor.execute(
            "INSERT INTO Livre (titre, resume, annee, serie_id, edition_id) "
            "VALUES (%s, %s, %s, %s, %s) RETURNING id",
            (data.titre, data.resume, data.annee, serie_id, edition_id)
        )
        livre_id = cursor.fetchone()[0]

        # --- Auteurs ---
        for nom_auteur in data.auteurs:
            auteur_id = get_or_create(cursor, "Auteur", nom_auteur)
            cursor.execute(
                "INSERT INTO LivreAuteur (livre_id, auteur_id) VALUES (%s, %s) ON CONFLICT DO NOTHING",
                (livre_id, auteur_id)
            )

        # --- Genres ---
        for nom_genre in data.genres:
            genre_id = get_or_create(cursor, "Genre", nom_genre)
            cursor.execute(
                "INSERT INTO LivreGenre (livre_id, genre_id) VALUES (%s, %s) ON CONFLICT DO NOTHING",
                (livre_id, genre_id)
            )

        # --- Exemplaires supplémentaires ---
        for _ in range(data.exemplaires - 1):  # -1 car le premier exemplaire déjà créé
            cursor.execute(
                "INSERT INTO Exemplaire (etat, ami_id, edition_id) VALUES (%s, %s, %s)",
                (data.etat, 1, edition_id)
            )

        conn.commit()
        return {"success": True, "livre_id": livre_id, "message": "Livre ajouté avec tous les liens !"}

    except Exception as e:
        conn.rollback()
        return {"success": False, "message": str(e)}

    finally:
        cursor.close()
        conn.close()


# ----------------------------
# ROUTES GET POUR LE FRONT / DOCS
# ----------------------------

@app.get("/auteurs")
def get_auteurs():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Auteur")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{"id": r[0], "nom": r[1]} for r in rows]


@app.get("/genres")
def get_genres():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Genre")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{"id": r[0], "nom": r[1]} for r in rows]


@app.get("/series")
def get_series():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Serie")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{"id": r[0], "nom": r[1]} for r in rows]


@app.get("/editeurs")
def get_editeurs():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Editeur")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{"id": r[0], "nom": r[1]} for r in rows]


# ----------------------------
# VISUALISER, SUPPRIMER, REMETTRE DISPONIBLE
# ----------------------------

@app.get("/livres")
def get_livres():
    """Retourne tous les livres avec leurs infos complètes"""
    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.execute("""
                       SELECT l.id,
                              l.titre,
                              l.resume,
                              l.annee,
                              s.nom        AS serie,
                              e.nom        AS editeur,
                              ed.nom       AS edition,
                              ed.isbn,
                              COUNT(ex.id) AS exemplaires
                       FROM Livre l
                                LEFT JOIN Serie s ON l.serie_id = s.id
                                LEFT JOIN Edition ed ON l.edition_id = ed.id
                                LEFT JOIN Editeur e ON ed.editeur_id = e.id
                                LEFT JOIN Exemplaire ex ON ex.edition_id = ed.id
                       GROUP BY l.id, s.nom, e.nom, ed.nom, ed.isbn
                       ORDER BY l.titre
                       """)
        livres_rows = cursor.fetchall()

        livres_list = []
        for r in livres_rows:
            livre_id = r[0]
            # Auteurs
            cursor.execute("""
                           SELECT a.nom
                           FROM LivreAuteur la
                                    JOIN Auteur a ON la.auteur_id = a.id
                           WHERE la.livre_id = %s
                           """, (livre_id,))
            auteurs = [a[0] for a in cursor.fetchall()]

            # Genres
            cursor.execute("""
                           SELECT g.nom
                           FROM LivreGenre lg
                                    JOIN Genre g ON lg.genre_id = g.id
                           WHERE lg.livre_id = %s
                           """, (livre_id,))
            genres = [g[0] for g in cursor.fetchall()]

            livres_list.append({
                "id": livre_id,
                "titre": r[1],
                "resume": r[2],
                "annee": r[3],
                "serie": r[4],
                "editeur": r[5],
                "edition": r[6],
                "isbn": r[7],
                "exemplaires": r[8],
                "auteurs": auteurs,
                "genres": genres
            })
        return livres_list
    finally:
        cursor.close()
        conn.close()


@app.delete("/livre/{livre_id}")
def delete_livre(livre_id: int):
    """Supprime un livre et ses relations"""
    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM Livre WHERE id = %s", (livre_id,))
        conn.commit()
        return {"success": True, "message": "Livre supprimé"}
    except Exception as e:
        conn.rollback()
        return {"success": False, "message": str(e)}
    finally:
        cursor.close()
        conn.close()


@app.post("/exemplaire/disponible/{livre_id}")
def set_exemplaires_disponibles(livre_id: int):
    """Marque tous les exemplaires d'un livre comme disponibles (ami_id = 1)"""
    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT edition_id FROM Livre WHERE id = %s", (livre_id,))
        row = cursor.fetchone()
        if not row:
            return {"success": False, "message": "Livre non trouvé"}
        edition_id = row[0]

        cursor.execute(
            "UPDATE Exemplaire SET ami_id = 1 WHERE edition_id = %s",
            (edition_id,)
        )
        conn.commit()
        return {"success": True, "message": "Tous les exemplaires sont maintenant disponibles"}
    except Exception as e:
        conn.rollback()
        return {"success": False, "message": str(e)}
    finally:
        cursor.close()
        conn.close()
