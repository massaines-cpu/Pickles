from fastapi import FastAPI
from pydantic import BaseModel  # ← indispensable !

app = FastAPI()

class Livre(BaseModel):
    Titre: str
    Auteur: str
    Resume: str
    Annee: int
    Edition: str

@app.get("/")
def read_root():
    return {"message": "Recup OK"}

bibliotheque = []
@app.post("/livres")
def ajouter_livre(livre: Livre):
    bibliotheque.append(livre)
    return {
        "message": "Livre ajouté en mémoire",
        "total_livres": len(bibliotheque)
    }

@app.get("/livres")
def lister_livres():
    return bibliotheque