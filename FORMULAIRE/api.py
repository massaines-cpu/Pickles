from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import psycopg

app = FastAPI(title="API Bibliothèque Débutant Absolu")


# ----------------------------
# MODEL Pydantic (validation entrée API)
# ----------------------------
# Ce modèle définit EXACTEMENT ce que le front a le droit d’envoyer
# → FastAPI valide automatiquement (sinon erreur 422)
class LivreModel(BaseModel):
    titre: str
    resume: Optional[str] = None
    annee: Optional[int] = None
    auteurs: List[str]
    genres: List[str]
    serie: Optional[str] = None
    editions: List[str]
    etats: List[str]          # parallèle aux exemplaires
    exemplaires: int
    editeur: str
    isbn: str

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


# ----------------------------
# DB UTILS
# ----------------------------
def get_conn():
    """Crée et retourne une connexion PostgreSQL"""
    return psycopg.connect(
        host="127.0.0.1",
        dbname="PicklesBase",
        user="postgres",
        password="Dompte2024!_!"
    )


def get_or_create(cursor, table, nom):
    """
    Pattern classique :
    - si la valeur existe → retourne son id
    - sinon → l’insère et retourne l’id créé
    """
    cursor.execute("SELECT id FROM " + table + " WHERE nom = '" + nom + "'")
    row = cursor.fetchone()
    if row:
        return row[0]

    cursor.execute(
        "INSERT INTO " + table + " (nom) VALUES ('" + nom + "') RETURNING id"
    )
    return cursor.fetchone()[0]


# ----------------------------
# AJOUTER UN LIVRE
# ----------------------------
@app.post("/livres")
def ajout_livre(data: LivreModel):
    conn = get_conn()
    cursor = conn.cursor()

    try:
        # ----------------------------
        # Série (optionnelle)
        # ----------------------------
        serie_id = "NULL"
        if data.serie:
            serie_id_int = get_or_create(cursor, "serie", data.serie)
            serie_id = str(serie_id_int)

        # ----------------------------
        # Livre (table principale)
        # ----------------------------
        titre = data.titre
        resume = data.resume if data.resume else ""
        annee = str(data.annee) if data.annee else "NULL"

<<<<<<< HEAD
        # Construction SQL "à la main"
        sql_livre = (
            "INSERT INTO livre (titre, resume, annee, serie_id) VALUES ("
            + "'" + titre + "', "
            + "'" + resume + "', "
            + annee + ", "
            + serie_id
            + ") RETURNING id"
=======
        # --- Premier exemplaire (nécessaire pour Edition) ---
        cursor.execute(
            "INSERT INTO Exemplaire (etat, ami_id, edition_id) VALUES (%s, %s, NULL) RETURNING id",
            (data.etat, 1)
        )
        ex_id = cursor.fetchone()[0]

        # --- Edition --- POUR  EMPECHER DOUBLON
        cursor.execute("SELECT id FROM Edition WHERE nom = %s AND isbn = %s", (data.edition, data.isbn))
        row = cursor.fetchone()

        if row:
            edition_id = row[0]  # Elle existe, on récupère son ID
        else:
            # Elle n'existe pas, on l'insère
            cursor.execute(
                "INSERT INTO Edition (nom, annee, isbn, editeur_id, exemplaire_id) "
                "VALUES (%s, %s, %s, %s, %s) RETURNING id",
                (data.edition, data.annee, data.isbn, editeur_id, ex_id)
            )
            edition_id = cursor.fetchone()[0]
        # cursor.execute(
        #     "INSERT INTO Edition (nom, annee, isbn, editeur_id, exemplaire_id) "
        #     "VALUES (%s, %s, %s, %s, %s) RETURNING id",
        #     (data.edition, data.annee, data.isbn, editeur_id, ex_id)
        # )
        # edition_id = cursor.fetchone()[0]

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
>>>>>>> 7331947057caf2c24f6b3a2386dd7719af30e052
        )
        cursor.execute(sql_livre)
        livre_id = cursor.fetchone()[0]

        # ----------------------------
        # Auteurs (relation N–N)
        # ----------------------------
        for nom_auteur in data.auteurs:
            auteur_id = get_or_create(cursor, "auteur", nom_auteur)

            # Table de jointure
            cursor.execute(
                "INSERT INTO livre_auteur (livre_id, auteur_id) VALUES ("
                + str(livre_id) + ", "
                + str(auteur_id) + ")"
            )

        # ----------------------------
        # Genres (relation N–N)
        # ----------------------------
        for nom_genre in data.genres:
            genre_id = get_or_create(cursor, "genre", nom_genre)
            cursor.execute(
                "INSERT INTO livre_genre (livre_id, genre_id) VALUES ("
                + str(livre_id) + ", "
                + str(genre_id) + ")"
            )

        # ----------------------------
        # Éditeur
        # ----------------------------
        editeur_id = get_or_create(cursor, "editeur", data.editeur)

        # ----------------------------
        # Éditions (1 livre → N éditions)
        # ----------------------------
        edition_ids = []
        for edition_nom in data.editions:
            sql_edition = (
                "INSERT INTO edition (nom, annee, isbn, livre_id, editeur_id) VALUES ("
                + "'" + edition_nom + "', "
                + annee + ", "
                + "'" + data.isbn + "', "
                + str(livre_id) + ", "
                + str(editeur_id)
                + ") RETURNING id"
            )
            cursor.execute(sql_edition)
            edition_ids.append(cursor.fetchone()[0])

        # ----------------------------
        # Exemplaires (N lignes réelles)
        # ----------------------------
        # Répartition circulaire :
        # - si plus d’exemplaires que d’éditions
        # - ou plus d’exemplaires que d’états
        for i in range(data.exemplaires):
            edition_id = edition_ids[i % len(edition_ids)]
            etat = data.etats[i % len(data.etats)]

            cursor.execute(
                "INSERT INTO exemplaire (etat, edition_id, ami_id) VALUES ("
                + "'" + etat + "', "
                + str(edition_id) + ", NULL)"
            )

        conn.commit()
        return {"success": True, "livre_id": livre_id}

    except Exception as e:
        # Toute erreur annule la transaction
        conn.rollback()
        return {"success": False, "error": str(e)}

    finally:
        cursor.close()
        conn.close()


# ----------------------------
# REMETTRE UN LIVRE DISPONIBLE
# ----------------------------
@app.post("/livre/{livre_id}/disponible")
def rendre_disponible(livre_id: int):
    conn = get_conn()
    cursor = conn.cursor()
    try:
        # Remet TOUS les exemplaires du livre comme disponibles
        cursor.execute(
            "UPDATE exemplaire SET ami_id = NULL "
            "WHERE edition_id IN ("
            "SELECT id FROM edition WHERE livre_id = " + str(livre_id) + ")"
        )
        conn.commit()
        return {"success": True}
    except Exception as e:
        conn.rollback()
        return {"success": False, "error": str(e)}
    finally:
        cursor.close()
        conn.close()


# ----------------------------
# GET LISTES GÉNÉRIQUES
# ----------------------------
def fetch_all(table):
    """
    Endpoint générique pour tables simples (id, nom)
    """
    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id, nom FROM " + table + " ORDER BY nom")
        rows = cursor.fetchall()
        return [{"id": r[0], "nom": r[1]} for r in rows]
    finally:
        cursor.close()
        conn.close()


# ----------------------------
# GET LIVRES (structure complète)
# ----------------------------
@app.get("/livres")
def get_livres():
    conn = get_conn()
    cursor = conn.cursor()
    try:
        # Livre + série
        cursor.execute("""
            SELECT l.id, l.titre, l.resume, l.annee, s.nom
            FROM livre l
            LEFT JOIN serie s ON l.serie_id = s.id
            ORDER BY l.titre
        """)
        livres_rows = cursor.fetchall()
        result = []

        for livre in livres_rows:
            livre_id = livre[0]

            # Auteurs
            cursor.execute(
                "SELECT a.nom FROM auteur a "
                "JOIN livre_auteur la ON a.id = la.auteur_id "
                "WHERE la.livre_id = " + str(livre_id)
            )
            auteurs = [r[0] for r in cursor.fetchall()]

            # Genres
            cursor.execute(
                "SELECT g.nom FROM genre g "
                "JOIN livre_genre lg ON g.id = lg.genre_id "
                "WHERE lg.livre_id = " + str(livre_id)
            )
            genres = [r[0] for r in cursor.fetchall()]

            # Éditions
            cursor.execute(
                "SELECT e.nom, e.annee, e.isbn, ed.nom "
                "FROM edition e "
                "JOIN editeur ed ON e.editeur_id = ed.id "
                "WHERE e.livre_id = " + str(livre_id)
            )
            editions = [{
                "edition": ed[0],
                "annee": ed[1],
                "isbn": ed[2],
                "editeur": ed[3]
            } for ed in cursor.fetchall()]

            # Exemplaires (vrais objets physiques)
            cursor.execute(
                "SELECT ex.id, ex.etat, ex.ami_id "
                "FROM exemplaire ex "
                "JOIN edition ed ON ex.edition_id = ed.id "
                "WHERE ed.livre_id = " + str(livre_id)
            )
            exemplaires = [{
                "id": ex[0],
                "etat": ex[1],
                "ami_id": ex[2]
            } for ex in cursor.fetchall()]

            result.append({
                "id": livre_id,
                "titre": livre[1],
                "resume": livre[2],
                "serie": livre[4],
                "auteurs": auteurs,
                "genres": genres,
                "editions": editions,
                "exemplaires": exemplaires
            })

        return result

    finally:
        cursor.close()
        conn.close()

@app.put("/exemplaires/{exemplaire_id}/preter")
def preter_exemplaire(exemplaire_id: int, data: dict):
    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE exemplaire SET ami_id = %s WHERE id = %s",
            (data["ami_id"], exemplaire_id)
        )
        conn.commit()
        return {"success": True}
    except Exception as e:
        conn.rollback()
        return {"success": False, "error": str(e)}
    finally:
        cursor.close()
        conn.close()


@app.post("/amis")
def ajouter_ami(ami: AmiModel):
    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO Ami (nom, telephone, ecole) VALUES (%s, %s, %s) RETURNING id",
            (ami.nom, ami.telephone, ami.ecole)
        )
        new_id = cursor.fetchone()[0]
        conn.commit()
        return {"success": True, "id": new_id, "message": "Ami ajouté avec succès"}
    except Exception as e:
        conn.rollback()
        return {"success": False, "message": str(e)}
    finally:
        cursor.close()
        conn.close()


# ----------------------------
# AUTRES ENDPOINTS SIMPLES
# ----------------------------
@app.get("/amis")
def get_amis():
    conn = get_conn()
    cursor = conn.cursor()
<<<<<<< HEAD
=======
    cursor.execute("SELECT id, nom, telephone, ecole FROM Ami")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    # Retourne une liste de dictionnaires
    return [{"id": r[0], "nom": r[1], "telephone": r[2], "ecole": r[3]} for r in rows]

@app.post("/amis")
def ajouter_ami(ami: AmiModel):
    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO Ami (nom, telephone, ecole) VALUES (%s, %s, %s) RETURNING id",
            (ami.nom, ami.telephone, ami.ecole)
        )
        new_id = cursor.fetchone()[0]
        conn.commit()
        return {"success": True, "id": new_id, "message": "Ami ajouté avec succès"}
    except Exception as e:
        conn.rollback()
        return {"success": False, "message": str(e)}
    finally:
        cursor.close()
        conn.close()
# ----------------------------
# VISUALISER, SUPPRIMER, REMETTRE DISPONIBLE
# ----------------------------

@app.get("/livres")
def get_livres():
    """Retourne tous les livres avec leurs infos complètes"""
    conn = get_conn()
    cursor = conn.cursor()
>>>>>>> 7331947057caf2c24f6b3a2386dd7719af30e052
    try:
        cursor.execute("SELECT id, nom, telephone, ecole FROM ami ORDER BY nom")
        return [{
            "id": r[0],
            "nom": r[1],
            "telephone": r[2],
            "ecole": r[3]
        } for r in cursor.fetchall()]
    finally:
        cursor.close()
        conn.close()


@app.get("/auteurs")
def get_auteurs():
    return fetch_all("auteur")


@app.get("/genres")
def get_genres():
    return fetch_all("genre")


@app.get("/series")
def get_series():
    return fetch_all("serie")


@app.get("/editeurs")
def get_editeurs():
    return fetch_all("editeur")


@app.get("/editions")
def get_editions():
    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT ed.id, ed.nom, ed.isbn, e.nom, ed.livre_id "
            "FROM edition ed "
            "LEFT JOIN editeur e ON ed.editeur_id = e.id "
            "ORDER BY ed.nom"
        )
        return [{
            "id": r[0],
            "nom": r[1],
            "isbn": r[2],
            "editeur": r[3],
            "livre_id": r[4]
        } for r in cursor.fetchall()]
    finally:
        cursor.close()
        conn.close()
