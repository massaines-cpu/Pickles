from uvicorn import run
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import psycopg

app = FastAPI()

class LivreCreate(BaseModel):
    Titre: str                                # Titre *
    Auteur: str                           # Auteur *
    Genre: str                                # Genre *
    Serie: Optional[str] = None               # Série
    Edition: str                              # Edition *
    Année: int                    # Année (de publication) *
    Editeur: str                              # Editeur *
    Etat: str                                 # Etat *
    Exemplaire: int                           # Exemplaire *
    ISBN: int                                 # ISBN *
    Résumé: Optional[str] = None              # Résumé
#class Auteurs (BaseModel):
   # Auteur: str 

DB_DSN = "postgresql://postgres:sandy30@localhost:5432/ma_db"


#@app.post("/auteurs"])
#async def lister_auteurs():
@app.post("/livres")
async def ajouter_livre(livre: LivreCreate):
    # convertir livre en sql et l'ajouter à la base de données
    
    data = livre.model_dump()

    sql = """
    INSERT INTO livres
    (titre, auteur, genre, serie, edition, annee_publication, editeur, etat, exemplaire, isbn, resume)
    VALUES
    (%(titre)s, %(auteur)s, %(genre)s, %(serie)s, %(edition)s,
     %(annee_publication)s, %(editeur)s, %(etat)s, %(exemplaire)s,
     %(isbn)s, %(resume)s)
    RETURNING id;
    """
    with psycopg.connect(DB_DSN) as conn:
        with conn.cursor() as cur:
            cur.execute(sql, data)
            new_id = cur.fetchone()[0]
            conn.commit()

    return {"id": new_id, **data}