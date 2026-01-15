import streamlit as st
import requests


st.markdown('# Bibliothèque de Maxime')
st.sidebar.markdown('# Bibliothèque de Maxime ')

liste_auteurs = ['Choisir un auteur', 'Michael McDowell', 'Dean Koontz', 'Stephen King', 'Beatrix Potter', 'Beatrice Sparks','Agatha Christie', 'Sylvie Baron', 'Satoshi Yagisawa','Dennis Lehane', 'Charles Duchaussois','Éléonore Devillepoix','Antonio Moresco' ]
# liste_auteurs = [liste_auteurs[0]] + sorted(liste_auteurs[1:]) #ordre alaphabetique mais prenom..
liste_auteurs_tri = [liste_auteurs[0]] + sorted(liste_auteurs[1:], key=lambda x: x.split()[-1]) #ordre alphabetique nom

liste_etat = ['Choisir un état', 'Bon', 'Très Bon', 'Neuf']

Titre = st.text_input('Titre*: ')
Auteur = st.selectbox("Auteur*", liste_auteurs)
Resume = st.text_input('Résumé: ')
Saga = st.text_input('Saga: ')
Genre = st.text_input('Genre*: ')
Annee = st.number_input("Année: ", step=1)
Edition = st.text_input('Edition*: ')
Editeur = st.text_input('Editeur*: ')
Etat = st.selectbox('Etat*: ', liste_etat)
Exemplaire = st.text_input('Exemplaire*: ')
ISBN = st.text_input('ISBN*: ')

if Auteur == "Choisir un auteur":
    st.write("Aucun auteur sélectionné")
liste_auteurs.append(Auteur)

if st.button("Ajouter un livre", key="btn_livre"):
    if Titre == "" and Genre == "" and Edition == "" and Exemplaire == "" and ISBN == "" and Etat == "Choisir un état":
        st.warning("Champ Vide")

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
        # st.json(data)

    url = 'http://127.0.0.1:8000/livres'
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

