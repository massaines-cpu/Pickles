from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Livre(BaseModel):
    Titre: str
    Auteur: str
    Resume: Optional[str] = ""
    Saga: Optional[str] = ""
    Genre: str
    Annee: int
    Edition: str
    Editeur: str
    Etat: str
    Exemplaire: int
    ISBN: int

bibliotheque = []

@app.get("/")
def read_root():
    return {"status": "Serveur Bibliothèque Opérationnel"}

# POST : Pour recevoir les données de Streamlit
@app.post("/livres")
def ajouter_livre(livre: Livre):
    bibliotheque.append(livre)
    return {
        "message": "Livre ajouté avec succès",
        "livre_recu": livre,
        "total": len(bibliotheque)
    }

# GET : Pour renvoyer la liste à Streamlit
@app.get("/livres", response_model=List[Livre])
def lister_livres():
    return bibliotheque