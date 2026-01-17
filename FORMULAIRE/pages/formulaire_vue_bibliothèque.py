import streamlit as st
import requests
import pandas as pd

def recup_options(endpoint):
    try:
        # Attention : utilisez "amis" en minuscules pour correspondre à votre API @app.get("/amis")
        res = requests.get(f"http://127.0.0.1:8000/{endpoint.lower()}")
        if res.status_code == 200:
            return res.json()  # On renvoie la liste complète de dictionnaires
        return []
    except Exception as e:
        st.error(f"Erreur API sur {endpoint}: {e}")
        return []

Api_url = 'http://127.0.0.1:8000'
st.title("La bibliothèque de Maxime")

response = requests.get('http://127.0.0.1:8000/livres')
if response.status_code == 200:
    livres = response.json()

    if livres:
        df_livres = pd.DataFrame(livres)


        df_livres["Auteurs"] = df_livres["auteurs"].apply(lambda x: ", ".join(x))
        df_livres["Genres"] = df_livres["genres"].apply(lambda x: ", ".join(x))

        # On ne montre que les colonnes utiles
        colonnes_utiles = [
            "id", "titre", "serie", "editeur", "edition", "annee",
            "auteurs", "genres", "exemplaires", "isbn"
        ]
        df_display = df_livres[[c for c in colonnes_utiles if c in df_livres.columns]]


        st.dataframe(df_display, width="stretch", hide_index=True)
        # df = pd.DataFrame(livres)
        # #on affiche les colonnes importantes
        # # st.dataframe(df[['Titre', 'Auteur', 'Exemplaire', 'Etat', 'Emprunteur', 'Genre', 'Saga', 'Editeur', 'Edition']], use_container_width=True)
        # st.dataframe(df[['id', 'titre', 'resume', 'annee', 'serie', 'editeur', 'edition', 'isbn', 'exemplaire', 'auteur', 'genres']], use_container_width=True)
    else:
        st.write("La bibliothèque de Maxime est vide.")

def fetch(endpoint):
    try:
        response = requests.get(f'{Api_url}{endpoint}')
        if response.status_code == 200:
            # print([item['nom'] for item in response.json()])
            return [item['nom'] for item in response.json()]
        return []
    except:
        return []

liste_auteurs = fetch('auteurs')











# import streamlit as st
# import requests
# import pandas as pd
#
# st.title("Vue de la Bibliothèque")
#
# try:
#     response = requests.get('http://127.0.0.1:8000/livres')
#     if response.status_code == 200:
#         data = response.json()
#         if data:
#             df = pd.DataFrame(data)
#
#             #on réorganise les colonnes pour que ce soit lisible
#             colonnes_vues = ['Titre', 'Auteur', 'Exemplaire', 'Genre', 'Etat']
#             #on vérifie que les colonnes existent dans le json
#             colonnes_presentes = [c for c in colonnes_vues if c in df.columns]
#
#             st.dataframe(df[colonnes_presentes], use_container_width=True)
#
#             st.metric("Total de livres différents", len(df))
#             st.metric("Total d'exemplaires", int(df['Exemplaire'].sum()) if 'Exemplaire' in df else 0)
#         else:
#             st.warning("Aucun livre dans la base de données.")
#     else:
#         st.error("Impossible de récupérer les données.")
# except:
#     st.error("Le serveur API n'est pas lancé.")