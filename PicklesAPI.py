import uvicorn
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import psycopg

app = FastAPI()

class LivreCreate(BaseModel):
    titre: str                                # Titre *
    #auteur: str                           # Auteur *
    #Genre: str                                # Genre *
    serie_id: Optional[int] = None               # Série
    edition_id: int                              # Edition *
    annee: int                    # Année (de publication) *
    #Editeur: str                              # Editeur *
    #Etat: str                                 # Etat *
    #Exemplaire: int                           # Exemplaire *
    #ISBN: int                                 # ISBN *
    resume: Optional[str] = None              # Résumé
    #class Auteurs (BaseModel):
   # Auteur: str 

def get_conn():
    return psycopg.connect(
        dbname="ma-mb",
        user="postgres",
        password="sandy30",
        host="127.0.0.1",
        port=5432
    )


#@app.post("/auteurs"])
#async def lister_auteurs():
@app.post("/livreS")
async def ajouter_livre(livre: LivreCreate):
    # convertir livre en sql et l'ajouter à la base de données
    
    data = livre.model_dump()

    sql = """
    INSERT INTO livre
    (titre, serie_id, edition_id, annee, resume)
    VALUES
    (%(titre)s,  %(serie_id)s, %(edition_id)s,
     %(annee)s, %(resume)s)
    RETURNING id;
    """
   
   
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute(sql, data)
        new_id = cur.fetchone()[0]
        conn.commit()  
        conn.close()
    return {"id": new_id, **data}

@app.get("/auteurs")
def get_auteurs():
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM Auteur")
        res = cur.fetchall()
    conn.close()
    return res
