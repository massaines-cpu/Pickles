import streamlit as st
import requests
import pandas as pd

st.title("La bibliothèque de maxime complète")

response = requests.get('http://127.0.0.1:8000/livres')
if response.status_code == 200:
    livres = response.json()
    if livres:
        df = pd.DataFrame(livres)
        #on affiche les colonnes importantes
        st.dataframe(df[['Titre', 'Auteur', 'Exemplaire', 'Emprunteur', 'Genre', 'Saga', 'Editeur', 'Edition']], use_container_width=True)

    else:
        st.write("La bibliothèque de Maxime est vide (la honte).")











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