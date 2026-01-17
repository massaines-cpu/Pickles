import streamlit as st
import requests
import json
import os

st.markdown('# Bibliothèque de Maxime')
st.sidebar.markdown('# Bibliothèque de Maxime ')

liste_etat = ['Choisir un état', 'Mauvais', 'Bon', 'Très Bon', 'Neuf']
if "auteurs" not in st.session_state:
    st.session_state.auteurs = ['Choisir un auteur', 'Michael McDowell', 'Dean Koontz', 'Stephen King',
    'Beatrix Potter', 'Beatrice Sparks','Agatha Christie', 'Sylvie Baron', 'Satoshi Yagisawa','Dennis Lehane',
    'Charles Duchaussois','Éléonore Devillepoix','Antonio Moresco', 'Amélie Nothomb', 'Annie Ernaux', 'Antoine de Saint-Exupéry', 'Albert Camus', 'Arthur Conan Doyle',
 'Bernard Werber', 'Boris Vian', 'Colette', 'Dan Brown', 'Douglas Adams',
 'Edgar Allan Poe', 'Émile Zola', 'Ernest Hemingway', 'Françoise Sagan', 'Frank Herbert']

if "genres" not in st.session_state:
    st.session_state.genres = ['Choisir un genre', 'Roman','Science-Fiction','Fantastique','Policier','Historique','Thriller','Dystopie','Aventure','Heroic-Fantasy','Romance','Horreur','Biographie','Essai','Conte']

if "sagas" not in st.session_state:
    st.session_state.sagas = ["Ne fait pas partie d'une saga", "Harry Potter", "Le Seigneur des Anneaux", "Le Trône de Fer", "Hunger Games", "Dune", "Fondation", "Millénium", "Sherlock Holmes", "La Tour Sombre", "The Witcher", "Le Monde de Narnia", "Twilight", "Percy Jackson", "L'Amie Prodigieuse"]

if "editeurs" not in st.session_state:
    st.session_state.editeurs = ['Choisir un éditeur', 'Gallimard', 'Hachette', 'Albin Michel', 'Flammarion', 'Grasset', 'Le Seuil', 'Robert Laffont', 'Pocket', 'Folio', 'J\'ai Lu', 'Actes Sud', 'Points', 'Rivages', 'Bragelonne', 'L\'Atalante']

if "editions" not in st.session_state:
    st.session_state.editions = ['Choisir l\'édition', 'Broché', 'Poche', 'Relié', 'Collector', 'Numérique / E-book', 'Livre Audio', 'Grand Format', 'Édition Limitée', 'Intégrale', 'BD / Roman Graphique', 'Luxe', 'Fac-similé']

#Formulaire
Titre = st.text_input('Titre*: ', key="id_titre")
Auteur = st.multiselect("Auteur*", st.session_state.auteurs, key="id_auteurs")
#ajouter un nouvel auteur
nouvel_auteur = st.text_input("Ajouter un nouvel auteur")

if st.button("Ajouter l'auteur"):
    if nouvel_auteur.strip() != "":
        if nouvel_auteur not in st.session_state.auteurs:
            st.session_state.auteurs.append(nouvel_auteur)
            st.success(f"Auteur ajouté : {nouvel_auteur}")
            st.rerun()
        else:
            st.warning("Cet auteur existe déjà.")
Resume = st.text_input('Résumé: ')
Saga = st.selectbox('Saga: ', st.session_state.sagas, key="id_saga")
nouvelle_saga = st.text_input("Ajouter une nouvelle saga")
if st.button("Ajouter une saga"):
    if nouvelle_saga.strip() != "":
        if nouvelle_saga not in st.session_state.sagas:
            st.session_state.saga.append(nouvelle_saga)
            st.success(f"Saga ajoutée : {nouvelle_saga}")
            st.rerun()
        else:
            st.warning("Cette saga existe déjà.")
Genre = st.multiselect('Genre*: ', st.session_state.genres, key="id_genre")
#ajouter un nouveau genre
nouveau_genre = st.text_input("Ajouter un nouveau genre")
if st.button("Ajouter un genre"):
    if nouveau_genre.strip() != "":
        if nouveau_genre not in st.session_state.genres:
            st.session_state.genres.append(nouveau_genre)
            st.success(f"Genre ajouté : {nouveau_genre}")
            st.rerun()
        else:
            st.warning("Ce genre existe déjà.")

Annee = st.number_input("Année: ", step=1)
# Edition = st.multiselect('Edition*: ', st.session_state.editions, key="id_edition")
# nouvelle_edition = st.text_input("Ajouter une nouvelle édition")
# if st.button("Ajouter une édition"):
#     if nouvelle_edition.strip() != "":
#         if nouvelle_edition not in st.session_state.editions:
#             st.session_state.editions.append(nouvelle_edition)
#             st.success(f"Edition ajoutée : {nouvelle_edition}")
#             st.rerun()
#         else:
#             st.warning("Cette édition existe déjà.")
Editeur = st.selectbox('Editeur*: ', st.session_state.editeurs, key="id_editeur")
nouvel_editeur = st.text_input("Ajouter un nouvel éditeur")
if st.button("Ajouter un éditeur"):
    if nouvel_editeur.strip() != "":
        if nouvel_editeur not in st.session_state.editeurs:
            st.session_state.editeurs.append(nouvel_editeur)
            st.success(f"Edition ajoutée : {nouvel_editeur}")
            st.rerun()
        else:
            st.warning("Cet éditeur existe déjà.")

Exemplaire = st.number_input('Nombre d\'exemplaires*:', min_value=1, value=1, step=1)
etats_exemplaires = []

if Exemplaire > 0:
    st.write("Détails des exemplaires")
    for i in range(int(Exemplaire)):
        st.write(f"**Exemplaire n°{i + 1}**")
        col_ed, col_et = st.columns(2)

        with col_ed:
            # ID unique grâce à key=f"edition_{i}"
            ed_val = st.selectbox(f"Édition n°{i + 1}", st.session_state.editions, key=f"edition_{i}")
        with col_et:
            # ID unique grâce à key=f"etat_{i}"
            et_val = st.selectbox(f"État n°{i + 1}", liste_etat, key=f"etat_{i}")

        # On enregistre la combinaison
        etats_exemplaires.append(f"{ed_val} ({et_val})")

# etats_exemplaires = []
# if Exemplaire > 0:
#     st.write("États des exemplaires")
#     cols = st.columns(2) #2 colonnes pour gagner de la place
#     for i in range(int(Exemplaire)):
#         # On utilise l'index i pour créer une clé unique par exemplaire
#         with cols[i % 2]:
#             etat = st.selectbox(
#                 f"État de l'exemplaire n°{i+1}*",
#                 liste_etat,
#                 key=f"etat_{i}"
#             )
#             etats_exemplaires.append(etat)
ISBN = st.number_input('ISBN*: ', step=1)

st.write("Formulaire livre rempli :", {
    "Titre": Titre,
    "Auteur": Auteur,
    'Saga': Saga if Saga != "Ne fait pas partie d'une saga" else None,
    'Resume': Resume if Resume.strip() != "" else None,
    "Genre": Genre,
    "Année": Annee,
    "Edition": etats_exemplaires,
    "Editeur": Editeur,
    "Etat": etats_exemplaires,
    "Exemplaire": Exemplaire,
    "ISBN": ISBN
})
if st.button('Ajouter ce livre à la bibliothèque'):
    erreurs = []
    if not Titre.strip(): erreurs.append("Titre")
    if Auteur == "Choisir un auteur": erreurs.append("Auteur")
    if Genre == "Choisir un genre": erreurs.append("Genre")
    if Editeur == 'Choisir un éditeur': erreurs.append("Editeur")
    if Edition == 'Choisir une édition': erreurs.append("Editeur")
    # if Etat == "Choisir un état": erreurs.append("Etat")
    if "Choisir un état" in etats_exemplaires:
        erreurs.append("État (un ou plusieurs exemplaires n'ont pas d'état)")

    if erreurs:
        st.error(f"Non mais écris quelque chose merde...: {', '.join(erreurs)}")
    else:
        # sauvegarder dans ma base de données ou ton fichier JSON
        auteur_str = ", ".join(Auteur)
        genre_str = ", ".join(Genre)
        etat_str = ", ".join(etats_exemplaires)
        st.success(f"Le livre '{Titre}' a bien été ajouté !")
        data = {
            'titre': Titre,
            'auteurs': Auteur,
            'resume': Resume.strip() if Resume.strip() != "" else None,
            'annee': int(Annee),
            'edition': etats_exemplaires[0].split(" (")[0] if Exemplaire == 1 else "Editions multiples",
            'genres': Genre,
            'saga': None if Saga == "Ne fait pas partie d'une saga" else Saga,
            'editeur': Editeur,
            'exemplaires': int(Exemplaire),
            'etat': ", ".join(etats_exemplaires),
            'isbn': str(ISBN) #avant javais mis int
        }
        # st.json(data)

    url = 'http://127.0.0.1:8000/livres'
    try:
        response = requests.post(url, json=data)
        # resp_json = response.json() #pourrecup

        if response.status_code == 200:
            st.success('Livre ajouté')
            st.json(data)
        else:
            st.error(f"Erreur {response.status_code}")
            st.text(response.text)

    except Exception as erreur:
        st.error(f"Erreur de connexion : {erreur}")

