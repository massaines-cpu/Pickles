# ajout_livre_front.py
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("Ajouter un livre à la bibliothèque")

# --- Récupération des listes pour les selectbox ---
def fetch_list(endpoint):
    try:
        resp = requests.get(f"{API_URL}/{endpoint}")
        if resp.status_code == 200:
            return [item["nom"] for item in resp.json()]
        return []
    except:
        return []

all_auteurs = fetch_list("auteurs")
all_genres = fetch_list("genres")
all_series = fetch_list("series")
all_editeurs = fetch_list("editeurs")

# --- Input titre avec autocomplete réactif ---
titre_input = st.text_input("Titre du livre")

# Liste des livres existants pour autocomplete
livres = []
if len(titre_input) >= 3:
    try:
        resp = requests.get(f"{API_URL}/livres")  # à créer si tu veux renvoyer tous les livres
        if resp.status_code == 200:
            livres = resp.json()
    except:
        livres = []

matching_livres = [l for l in livres if titre_input.lower() in l["titre"].lower()]

serie_default = ""
edition_default = ""
editeur_default = ""
auteurs_default = []
genres_default = []

if matching_livres:
    # On prend le premier match pour pré-remplir
    livre_match = matching_livres[0]
    serie_default = livre_match.get("serie", "")
    edition_default = livre_match.get("edition", "")
    editeur_default = livre_match.get("editeur", "")
    auteurs_default = livre_match.get("auteurs", [])
    genres_default = livre_match.get("genres", [])

if st.checkbox("Afficher suggestions de livres existants"):
    st.write([l["titre"] for l in matching_livres])

# --- Autres champs ---
resume = st.text_area("Résumé")
annee = st.number_input("Année de publication", min_value=1900, max_value=2100, value=2026)

serie = st.selectbox("Série", options=all_series + ["--Nouvelle série--"], index=all_series.index(serie_default) if serie_default in all_series else len(all_series))
if serie == "--Nouvelle série--":
    serie = st.text_input("Nom de la nouvelle série", value=serie_default)

editeur = st.selectbox("Éditeur", options=all_editeurs + ["--Nouvel éditeur--"], index=all_editeurs.index(editeur_default) if editeur_default in all_editeurs else len(all_editeurs))
if editeur == "--Nouvel éditeur--":
    editeur = st.text_input("Nom du nouvel éditeur", value=editeur_default)

edition = st.text_input("Edition", value=edition_default)
isbn = st.text_input("ISBN")

# --- Auteurs et Genres ---
selected_auteurs = st.multiselect("Auteurs", options=all_auteurs, default=auteurs_default)
if "--Nouvel auteur--" in selected_auteurs:
    new_auteur = st.text_input("Nom du nouvel auteur")
    if new_auteur:
        selected_auteurs.append(new_auteur)
    selected_auteurs.remove("--Nouvel auteur--")

selected_genres = st.multiselect("Genres", options=all_genres, default=genres_default)
if "--Nouveau genre--" in selected_genres:
    new_genre = st.text_input("Nom du nouveau genre")
    if new_genre:
        selected_genres.append(new_genre)
    selected_genres.remove("--Nouveau genre--")

etat = st.selectbox("État de l'exemplaire", ["Tres bon", "Bon", "Mauvais"])
exemplaires = st.number_input("Nombre d'exemplaires", min_value=1, value=1)

# --- Bouton d'envoi ---
if st.button("Ajouter le livre"):
    payload = {
        "titre": titre_input,
        "resume": resume,
        "annee": annee,
        "auteurs": selected_auteurs,
        "genres": selected_genres,
        "serie": serie,
        "edition": edition,
        "editeur": editeur,
        "etat": etat,
        "exemplaires": exemplaires,
        "isbn": isbn
    }

    try:
        resp = requests.post(f"{API_URL}/livre/complet", json=payload)
        if resp.status_code == 200:
            st.success(resp.json().get("message"))
        else:
            st.error(f"Erreur {resp.status_code} : {resp.text}")
    except Exception as e:
        st.error(f"Erreur de connexion à l'API : {e}")
