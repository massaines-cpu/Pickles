import streamlit as st
import requests


st.markdown('# Bibliothèque')
st.sidebar.markdown('# Bibliothèque ')

liste_auteurs = ['Choisir un auteur', 'Michael McDowell', 'Dean Koontz', 'Stephen King', 'Beatrix Potter', 'Beatrice Sparks','Agatha Christie', 'Sylvie Baron', 'Satoshi Yagisawa','Dennis Lehane', 'Charles Duchaussois','Éléonore Devillepoix','Antonio Moresco' ]
# liste_auteurs = [liste_auteurs[0]] + sorted(liste_auteurs[1:]) #ordre alaphabetique mais prenom..
liste_auteurs_tri = [liste_auteurs[0]] + sorted(liste_auteurs[1:], key=lambda x: x.split()[-1]) #ordre alphabetique nom

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
        st.warning("TU N'AS PAS SELECTIONNÉ D'AUTEUR MISÉRABLE !!!")
    else:
        data = {
            'Titre': Titre,
            'Auteur': Auteur,
            'Resume': Resume,
            'Annee': int(Annee),
            'Edition': Edition
        }
        #st.json(data)

    url = "http://127.0.0.1:8000/genres"
    try:
        response = requests.get(url)  #
        resp_json = response.json()

        if response.status_code == 200:
            if resp_json.get("success"):
                st.success(resp_json.get("message"))
                #st.json(resp_json.get("livres"))
            else:
                st.error(resp_json.get("message"))
        else:
            st.error(f"Erreur {response.content}")
            st.error(f"Erreur {response.status_code}")
            st.text(response.text)

    except Exception as erreur:
        st.error(f"Erreur de connexion : {erreur}")

