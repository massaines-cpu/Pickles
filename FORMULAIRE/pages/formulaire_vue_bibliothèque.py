import streamlit as st
import requests
import pandas as pd


def recup_options(endpoint):
    try:
        # Appel dynamique vers une route de l’API (ex: /auteurs, /genres)
        res = requests.get("http://127.0.0.1:8000/" + endpoint.lower())

        if res.status_code == 200:
            items = res.json()  # JSON → objets Python
            noms = []

            # On récupère uniquement le champ "nom" s’il existe
            for item in items:
                if 'nom' in item:
                    noms.append(item['nom'])

            return noms
        return []

    except Exception as e:
        # Affiche l’erreur directement dans Streamlit
        st.error("Erreur API sur " + endpoint + " : " + str(e))
        return []


Api_url = 'http://127.0.0.1:8000'
st.title("La bibliothèque de Maxime")


# --- Récupère tous les livres ---
response = requests.get(Api_url + '/livres')
if response.status_code == 200:
    livres = response.json()

    if livres:
        livres_liste = []

        for livre in livres:

            # Transformation liste → texte (affichage)
            auteurs_text = ""
            for a in livre['auteurs']:
                if auteurs_text != "":
                    auteurs_text += ", "
                auteurs_text += a

            genres_text = ""
            for g in livre['genres']:
                if genres_text != "":
                    genres_text += ", "
                genres_text += g

            # Aplatissement d’une structure complexe (édition)
            editions_text = ""
            for ed in livre['editions']:
                if editions_text != "":
                    editions_text += ", "
                editions_text += (
                    ed['edition']
                    + " (" + str(ed['annee'])
                    + ", " + str(ed['isbn'])
                    + ", " + ed['editeur'] + ")"
                )

            exemplaires_text = ""
            for ex in livre['exemplaires']:
                if exemplaires_text != "":
                    exemplaires_text += ", "
                exemplaires_text += "id:" + str(ex['id']) + " (" + ex['etat'] + ")"

            # Dictionnaire "plat" adapté à Pandas / Streamlit
            livres_liste.append({
                "id": livre['id'],
                "titre": livre['titre'],
                "serie": livre.get('serie', ""),  # évite une KeyError
                "Auteurs": auteurs_text,
                "Genres": genres_text,
                "Editions": editions_text,
                "Exemplaires": exemplaires_text
            })

        df_livres = pd.DataFrame(livres_liste)

        # Colonnes réellement utiles à l’affichage
        df_display = df_livres[
            ["id", "titre", "serie", "Auteurs", "Genres", "Editions", "Exemplaires"]
        ]

        st.dataframe(df_display, use_container_width=True, hide_index=True)

    else:
        st.write("La bibliothèque de Maxime est vide.")


# --- Récupération simple des auteurs (pour selectbox par ex.) ---
def fetch(endpoint):
    try:
        response = requests.get(Api_url + endpoint)
        if response.status_code == 200:
            noms = []
            for item in response.json():
                if 'nom' in item:
                    noms.append(item['nom'])
            return noms
        return []
    except:
        return []


liste_auteurs = fetch('/auteurs')
