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
 'Edgar Allan Poe', 'Émile Zola', 'Ernest Hemingway', 'Françoise Sagan', 'Frank Herbert',
 'Frédéric Beigbeder', 'Gabriel García Márquez', 'George Orwell', 'Georges Simenon', 'Gilles Legardinier',
 'Guillaume Musso', 'Guy de Maupassant', 'H.P. Lovecraft', 'Haruki Murakami', 'Harlan Coben',
 'Isaac Asimov', 'J.K. Rowling', 'J.R.R. Tolkien', 'Jane Austen', 'Jean d\'Ormesson',
 'Jean-Christophe Grangé', 'Joël Dicker', 'Ken Follett', 'Leïla Slimani', 'Marcel Proust',
 'Margaret Atwood', 'Mary Shelley', 'Maxime Chattam', 'Michel Bussi', 'Michel Houellebecq',
 'Molière', 'Oscar Wilde', 'Paulo Coelho', 'Philip K. Dick', 'Pierre Lemaitre',
 'René Goscinny', 'Roald Dahl', 'Romain Gary', 'Stendhal', 'Victor Hugo', 'Alain Damasio', 'Alexandre Dumas', 'Andrzej Sapkowski', 'Anne Rice', 'Barjavel',
 'Baudelaire', 'Céline', 'Christian Bobin', 'Cizia Zykë', 'Colson Whitehead',
 'Daniel Pennac', 'Don Winslow', 'Elena Ferrante', 'Ellroy James', 'Enki Bilal',
 'Fred Vargas', 'George R.R. Martin', 'Gustave Flaubert', 'Hervé Bazin', 'Honoré de Balzac',
 'Ian McEwan', 'Irvine Welsh', 'Jack Kerouac', 'Jack London', 'James Baldwin',
 'Jean Teulé', 'Jean-Paul Sartre', 'John Steinbeck', 'Julien Gracq', 'Jules Verne',
 'Katherine Pancol', 'Lao She', 'Laurent Gaudé', 'Lewis Carroll', 'Marlen Haushofer',
 'Mary Higgins Clark', 'Maurice Druon', 'Maya Angelou', 'Michael Connelly', 'Michel Tournier',
 'Milan Kundera', 'Neil Gaiman', 'Patrick Modiano', 'Philippe Djian', 'Pierre Bottero',
 'Robin Hobb', 'Stephenie Meyer', 'Sylvain Tesson', 'Toni Morrison', 'Virginie Despentes']

if "genres" not in st.session_state:
    st.session_state.genres = ['Choisir un genre', 'Roman','Science-Fiction','Fantastique','Policier','Historique','Thriller','Dystopie','Aventure','Heroic-Fantasy','Romance','Horreur','Biographie','Essai','Conte']

if "sagas" not in st.session_state:
    st.session_state.sagas = ['Choisir une saga', "Harry Potter", "Le Seigneur des Anneaux", "Le Trône de Fer", "Hunger Games", "Dune", "Fondation", "Millénium", "Sherlock Holmes", "La Tour Sombre", "The Witcher", "Le Monde de Narnia", "Twilight", "Percy Jackson", "L'Amie Prodigieuse"]

if "editeurs" not in st.session_state:
    st.session_state.editeurs = ['Choisir un éditeur', 'Gallimard', 'Hachette', 'Albin Michel', 'Flammarion', 'Grasset', 'Le Seuil', 'Robert Laffont', 'Pocket', 'Folio', 'J\'ai Lu', 'Actes Sud', 'Points', 'Rivages', 'Bragelonne', 'L\'Atalante']

if "editions" not in st.session_state:
    st.session_state.editions = ['Choisir l\'édition', 'Broché', 'Poche', 'Relié', 'Collector', 'Numérique / E-book', 'Livre Audio', 'Grand Format', 'Édition Limitée', 'Intégrale', 'BD / Roman Graphique', 'Luxe', 'Fac-similé']

#Formulaire
Titre = st.text_input('Titre*: ')
Auteur = st.selectbox("Auteur*", st.session_state.auteurs)
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
Saga = st.text_input('Saga: ')
nouvelle_saga = st.text_input("Ajouter une nouvelle saga")
if st.button("Ajouter une saga"):
    if nouvelle_saga.strip() != "":
        if nouvelle_saga not in st.session_state.sagas:
            st.session_state.saga.append(nouvelle_saga)
            st.success(f"Saga ajoutée : {nouvelle_saga}")
            st.rerun()
        else:
            st.warning("Cette saga existe déjà.")
Genre = st.selectbox('Genre*: ', st.session_state.genres)
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
Edition = st.text_input('Edition*: ')
nouvelle_edition = st.text_input("Ajouter une nouvelle édition")
if st.button("Ajouter une édition"):
    if nouvelle_edition.strip() != "":
        if nouvelle_edition not in st.session_state.editions:
            st.session_state.editions.append(nouvelle_edition)
            st.success(f"Edition ajoutée : {nouvelle_edition}")
            st.rerun()
        else:
            st.warning("Cette édition existe déjà.")
Editeur = st.text_input('Editeur*: ')
nouvel_editeur = st.text_input("Ajouter un nouvel éditeur")
if st.button("Ajouter un éditeur"):
    if nouvel_editeur.strip() != "":
        if nouvel_editeur not in st.session_state.editeurs:
            st.session_state.editeurs.append(nouvel_editeur)
            st.success(f"Edition ajoutée : {nouvel_editeur}")
            st.rerun()
        else:
            st.warning("Cet éditeur existe déjà.")
Etat = st.selectbox('Etat*: ', liste_etat)
Exemplaire = st.number_input('Exemplaire*: ', step=1)
ISBN = st.number_input('ISBN*: ', step=1)

st.write("Formulaire livre rempli :", {
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
if st.button('Ajouter ce livre à la bibliothèque'):
    erreurs = []
    if not Titre.strip(): erreurs.append("Titre")
    if Auteur == "Choisir un auteur": erreurs.append("Auteur")
    if Genre == "Choisir un genre": erreurs.append("Genre")
    if Editeur == 'Choisir un éditeur': erreurs.append("Editeur")
    if Edition == 'Choisir une édition': erreurs.append("Edition")
    if Etat == "Choisir un état": erreurs.append("Etat")

    if erreurs:
        st.error(f"Non mais écris quelque chose merde...: {', '.join(erreurs)}")
    else:
        # sauvegarder dans ma base de données ou ton fichier JSON
        st.success(f"Le livre '{Titre}' a bien été ajouté !")
        data = {
            'Titre': Titre,
            'Auteur': Auteur,
            'Resume': Resume,
            'Annee': int(Annee),
            'Edition': Edition,
            'Genre': Genre,
            'Saga': Saga,
            'Editeur': Editeur,
            'Exemplaire': int(Exemplaire),
            'Etat': Etat,
            'ISBN': int(ISBN)
        }
        # st.json(data)

    url = 'http://127.0.0.1:8000/livres'
    try:
        response = requests.post(url, json=data)
        resp_json = response.json() #pourrecup

        if response.status_code == 200:
            st.success('Livre ajouté')
            st.json(data)
        else:
            st.error(f"Erreur {response.status_code}")
            st.text(response.text)

    except Exception as erreur:
        st.error(f"Erreur de connexion : {erreur}")

