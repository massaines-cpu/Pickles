import streamlit as st
import requests
st.markdown('# Bibliothèque de Maxime')
st.sidebar.markdown('# Bibliothèque de Maxime ')

liste_etat = ['Choisir un état', 'Mauvais', 'Bon', 'Très Bon', 'Neuf']
genres = ['Choisir un genre', 'Roman', 'Science-Fiction', 'Fantastique', 'Policier']

#Formulaire
Titre = st.text_input('Titre*: ')
Auteur = st.selectbox("Auteur*", st.session_state.auteurs)
#Initialisation des auteurs
if "auteurs" not in st.session_state:
    st.session_state.auteurs = ['Choisir un auteur', 'Michael McDowell', 'Dean Koontz', 'Stephen King', 'Beatrix Potter', 'Beatrice Sparks','Agatha Christie', 'Sylvie Baron', 'Satoshi Yagisawa','Dennis Lehane', 'Charles Duchaussois','Éléonore Devillepoix','Antonio Moresco']

#Ajouter un nouvel auteur
nouvel_auteur = st.text_input("Ajouter un nouvel auteur")

if st.button("Ajouter l'auteur"):
    if nouvel_auteur.strip() != "":
        if nouvel_auteur not in st.session_state.auteurs:
            st.session_state.auteurs.append(nouvel_auteur)
            st.success(f"Auteur ajouté : {nouvel_auteur}")
        else:
            st.warning("Cet auteur existe déjà.")

Resume = st.text_input('Résumé: ')
Saga = st.text_input('Saga: ')
Genre = st.selectbox('Genre*: ', genres)
Annee = st.number_input("Année: ", step=1)
Edition = st.text_input('Edition*: ')
Editeur = st.text_input('Editeur*: ')
Etat = st.selectbox('Etat*: ', liste_etat)
Exemplaire = st.number_input('Exemplaire*: ', step=1)
ISBN = st.number_input('ISBN*: ', step=1)

st.write("Formulaire rempli :", {
    "Titre": Titre,
    "Auteur": Auteur,
    "Résumé": Resume,
    "Saga": Saga,
    "Genre": Genre,
    "Année": Annee,
    "Edition": Edition,
    "Editeur": Editeur,
    "Etat": Etat,
    "Exemplaire": Exemplaire,
    "ISBN": ISBN
})

# if Auteur == "Choisir un auteur":
#     st.write("Aucun auteur sélectionné")

if st.button("Ajouter un livre", key="btn_livre"):
    if Titre == "" and Auteur == "" and Genre == "" and Edition == "" and Editeur == "" and Exemplaire == "" and ISBN == "" and Etat == "Choisir un état":
        st.warning("Champ Vide")

# if st.button("Ajouter un livre", key="btn_livre"):
#     if Auteur == "Choisir un auteur":
#         st.warning("TU N'AS PAS SELECTIONNÉ D'AUTEUR MISÉRABLE !!!")
    else:
        data = {
            'Titre': Titre,
            'Auteur': Auteur,
            'Resume': Resume,
            'Annee': int(Annee),
            'Edition': Edition,
            'Genre': Genre,
            'Saga': Saga,
            'Editeur':Editeur,
            'Exemplaire': int(Exemplaire),
            'Etat': Etat,
            'ISBN': int(ISBN)
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

