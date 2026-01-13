import streamlit as st
import requests


st.markdown('# Bibliothèque')
st.sidebar.markdown('# Bibliothèque ')

liste_auteurs = ['Choisir un auteur', 'Michael McDowell', 'Dean Koontz', 'Stephen King', 'Beatrix Potter']
Titre = st.text_input('Titre: ')
# Auteur = st.text_input('Auteur: ')
Auteur = st.selectbox("Auteur", liste_auteurs)
Resume = st.text_input('Résumé: ')
Annee = st.number_input("Année: ", step=1)
Edition = st.text_input('Edition: ')
if Auteur == "Choisir un auteur":
    st.write("Aucun auteur sélectionné")
liste_auteurs.append(Auteur)

# # left_column, right_column = st.columns(2)
# # left_column.button('Ajouter un livre')
# st.button("Ajouter un livre", key="btn_ajouter_livre")
# st.button("Ajouter un auteur", key="btn_ajouter_auteur")

if st.button("Ajouter un livre", key="btn_livre"):
    if Auteur == "Choisir un auteur":
        st.warning("Veuillez sélectionner un auteur")
    else:
        data = {
            'Titre': Titre,
            'Auteur': Auteur,
            'Resume': Resume,
            'Annee': int(Annee),
            'Edition': Edition
        }
        st.json(data)

    url = "https://.........."
    try:
        response = requests.post(url, json=data)

        if response.status_code == 200:
            st.success('Livre ajouté')
            st.json(data)
        else:
            st.error(f"Erreur {response.status_code}")
            st.text(response.text)

    except Exception as erreur:
        st.error(f"Erreur de connexion : {erreur}")

