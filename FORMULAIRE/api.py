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
    Emprunteur: Optional[str] = "Personne"


# base de données tempo
bibliotheque = []


@app.get("/")
def read_root():
    return {"status": "Serveur Bibliothèque Opérationnel"}


# ajout livre
@app.post("/livres")
def ajouter_livre(livre: Livre):
    bibliotheque.append(livre)
    return {
        "message": "Livre ajouté avec succès",
        "total": len(bibliotheque)
    }


#LISTER LES LIVRES
@app.get("/livres", response_model=List[Livre])
def lister_livres():
    return bibliotheque


# maj stock emprunteur
#
@app.put("/livres/{titre}")
def update_livre(titre: str, update_data: dict):
    for livre in bibliotheque:
        # On compare les titres
        if livre.Titre.strip().lower() == titre.strip().lower():

            # Mmaj stock dans json
            if "Exemplaire" in update_data:
                livre.Exemplaire = update_data["Exemplaire"]

            # Maj eprunter
            if "Emprunteur" in update_data:
                livre.Emprunteur = update_data["Emprunteur"]

            return {
                "status": "success",
                "livre": livre.Titre,
                "nouveau_stock": livre.Exemplaire,
                "emprunteur": livre.Emprunteur
            }

    return {"status": "error", "message": "Livre non trouvé"}