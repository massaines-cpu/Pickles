import uvicorn
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import psycopg

app = FastAPI(debug=True)

#se que je recois du formulaire livre
class LivreCreate(BaseModel):
    titre: str                                # Titre *
    auteur: str                                # Auteur *
    Genre: str                                # Genre *
    serie: Optional[str] = None               # serie
    edition: int                              # Edition *
    annee: int                                # Année (de publication) *
    Editeur: str                              # Editeur *
    Etat: str                                 # Etat *
    Exemplaire: int                           # Exemplaire *
    ISBN: int                                 # ISBN *
    resume: Optional[str] = None              # Résumé
    
    #CE QUE JE RECOIS DU FORMUALIRE cree un amie
    class Amis(BaseModel):
        nom: str
        telephone: int
        ecole: str

    #formulaire preté un livre

#CONEXION A LA BASE
def get_conn():
    return psycopg.connect(
        dbname="ma_db",
        user="postgres",
        password="sandy30",
        host="127.0.0.1",
        port=5432
    )
    
def get_or_create(cursor, table, nom):
    #"""Cherche une entrée dans table par nom, sinon l'insère et retourne l'id"""
    cursor.execute(f"SELECT id FROM {table} WHERE nom = %s", (nom,))
    row = cursor.fetchone()
    if row:
        return row[0]
    cursor.execute(f"INSERT INTO A {table} (nom) VALUES (%s) RETURNING id", (nom,))
    return cursor.fetchone()[0]




##########POST#####


@app.post("/livreS")
async def ajouter_livre(livre: LivreCreate):
    conn = get_conn()
    cursor = conn.cursor()
    # convertir livre en sql et l'ajouter à la base de données
    edition_id = get_or_create(cursor , "edition" ,livre.edition)
    
    data = livre.model_dump()

    sql1 = """
    INSERT INTO livre
    (titre, serie_id, edition_id, annee, resume)
    VALUES
    (%(titre)s,  %(serie_id)s, %(edition_id)s,
     %(annee)s, %(resume)s)
    RETURNING id;
    """
   
   








################GET#############


    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute(sql1, data)
        new_id = cur.fetchone()[0]
        conn.commit()  
        conn.close()
    return {"id": new_id, **data}

@app.get("/auteurs")
def get_auteurs():
    conn = get_conn()
    with conn.cursor() as cur:
        cur.execute("SELECT nom FROM Auteur")
        
        res = cur.fetchall()
        conn.commit()
        conn.close()
        print("voici la liste", res)
    return [{"nom": r[0]} for r in res]

@app.get("/EDITION")
def get_edition():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Edition")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{"id": r[0], "nom": r[1]} for r in rows]

@app.get("/Ami")
def get_ami():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT nom FROM ")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{"id": r[0], "nom": r[1]} for r in rows]

