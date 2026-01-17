import streamlit as st
import requests
import datetime

# def recup_options(endpoint):
#     try:
#         res = requests.get(f"http://127.0.0.1:8000/{endpoint}")
#         if res.status_code == 200:
#             items = res.json()
#
#             return [item['nom'] for item in items]
#         return []
#     except Exception as e:
#         print(f"Erreur API sur {endpoint}: {e}")
#         return []
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

st.markdown('# Bibliothèque de Maxime')
st.sidebar.markdown('# Bibliothèque de Maxime ')
# Affiche ce que l'API renvoie réellement dans la barre latérale
if st.sidebar.button("Debug API"):
    st.sidebar.write("Auteurs:", recup_options("auteurs"))
    st.sidebar.write("Editions:", recup_options("edition"))

liste_etat = ['Choisir un état', 'Mauvais', 'Bon', 'Très bon', 'Neuf']
if "auteurs" not in st.session_state:
    st.session_state.auteurs = recup_options("auteurs")

if "genres" not in st.session_state:
    st.session_state.genres  = recup_options("genres")

    # st.session_state.genres = ['Choisir un genre', 'Roman','Science-Fiction','Fantastique','Policier','Historique','Thriller','Dystopie','Aventure','Heroic-Fantasy','Romance','Horreur','Biographie','Essai','Conte']

if "series" not in st.session_state:
    les_series = recup_options("series")
    st.session_state.series = ['Aucune'] + les_series
    # st.session_state.sagas = ["Ne fait pas partie d'une saga", "Harry Potter", "Le Seigneur des Anneaux", "Le Trône de Fer", "Hunger Games", "Dune", "Fondation", "Millénium", "Sherlock Holmes", "La Tour Sombre", "The Witcher", "Le Monde de Narnia", "Twilight", "Percy Jackson", "L'Amie Prodigieuse"]

if "editeurs" not in st.session_state:
    st.session_state.editeurs = recup_options("editeurs")
    # st.session_state.editeurs = ['Choisir un éditeur', 'Gallimard', 'Hachette', 'Albin Michel', 'Flammarion', 'Grasset', 'Le Seuil', 'Robert Laffont', 'Pocket', 'Folio', 'J\'ai Lu', 'Actes Sud', 'Points', 'Rivages', 'Bragelonne', 'L\'Atalante']


if "editions" not in st.session_state:
    st.session_state.editions = recup_options("edition")
    # st.session_state.editions = ['Choisir l\'édition', 'Broché', 'Poche', 'Relié', 'Collector', 'Numérique / E-book', 'Livre Audio', 'Grand Format', 'Édition Limitée', 'Intégrale', 'BD / Roman Graphique', 'Luxe', 'Fac-similé']

#Formulaire
Titre = st.text_input('Titre*: ', key="id_titre")
Auteur = st.multiselect("Auteur*", st.session_state.auteurs, key="id_auteurs")
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
Serie = st.selectbox('Série: ', st.session_state.series, key="id_serie")
nouvelle_saga = st.text_input("Ajouter une nouvelle saga")
if st.button("Ajouter une saga"):
    if nouvelle_saga.strip() != "":
        if nouvelle_saga not in st.session_state.series:
            st.session_state.series.append(nouvelle_saga) # Ajoute le S ici aussi
            st.success(f"Série ajoutée : {nouvelle_saga}")
            st.rerun()

Genre = st.multiselect('Genre*: ', st.session_state.genres, key="id_genre")
nouveau_genre = st.text_input("Ajouter un nouveau genre")
if st.button("Ajouter un genre"):
    if nouveau_genre.strip() != "":
        if nouveau_genre not in st.session_state.genres:
            st.session_state.genres.append(nouveau_genre)
            st.success(f"Genre ajouté : {nouveau_genre}")
            st.rerun()
        else:
            st.warning("Ce genre existe déjà.")
annee_actuelle = datetime.date.today().year
Annee = st.number_input(
    "Année de publication*:",
    min_value=1450,
    max_value=annee_actuelle,
    value=annee_actuelle,
    step=1,
    key="id_annee"
)
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

ISBN = st.number_input('ISBN*: ', step=1)

st.write("Formulaire livre rempli :", {
    "Titre": Titre,
    "Auteur": Auteur,
    'Serie': Serie if Serie != "Ne fait pas partie d'une série" else None,
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
    if not Titre.strip():
        erreurs.append("Titre")
    if not Auteur:
        erreurs.append("Auteur")
    if not Genre:
        erreurs.append("Genre")
    if Editeur == 'Choisir un éditeur':
        erreurs.append("Editeur")
    if Annee < 1450 or Annee > annee_actuelle:
        erreurs.append("Année invalide")
    if any("Choisir" in s for s in etats_exemplaires):
        erreurs.append("État/Édition non sélectionné.e(s)")

    if erreurs:
        st.error(f"IL MANQUE DES INFOS HEHO : {', '.join(erreurs)}")
    else:
        etat_brut = etats_exemplaires[0].split("(")[-1].replace(")", "").strip()
        mapping_etats = {
            "mauvais": "Mauvais",
            "bon": "Bon",
            "très bon": "Très bon",
            "neuf": "Neuf"
        }
        etat_final = mapping_etats.get(etat_brut.lower(), etat_brut)
        data = {
            'titre': Titre,
            'auteurs': Auteur,
            'resume': Resume.strip() if Resume.strip() != "" else None,
            'annee': str(Annee),
            'edition': etats_exemplaires[0].split(" (")[0],  # Juste "Poche"
            'genres': Genre,
            'serie': "" if Serie == "Aucune" else Serie,
            'editeur': Editeur,
            'exemplaires': int(Exemplaire),
            'etat': etat_final,
            'isbn': str(ISBN)
        }

        url = 'http://127.0.0.1:8000/livres'
        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
                st.success(f"Le livre '{Titre}' a bien été ajouté !")
                st.json(data)
            else:
                st.error(f"Erreur API {response.status_code}: {response.text}")
        except Exception as erreur:
            st.error(f"Erreur de connexion au serveur : {erreur}")


 #    st.session_state.auteurs = ['Choisir un auteur', 'Michael McDowell', 'Dean Koontz', 'Stephen King',
 #    'Beatrix Potter', 'Beatrice Sparks','Agatha Christie', 'Sylvie Baron', 'Satoshi Yagisawa','Dennis Lehane',
 #    'Charles Duchaussois','Éléonore Devillepoix','Antonio Moresco', 'Amélie Nothomb', 'Annie Ernaux', 'Antoine de Saint-Exupéry', 'Albert Camus', 'Arthur Conan Doyle',
 # 'Bernard Werber', 'Boris Vian', 'Colette', 'Dan Brown', 'Douglas Adams',
 # 'Edgar Allan Poe', 'Émile Zola', 'Ernest Hemingway', 'Françoise Sagan', 'Frank Herbert']

# ajouter un nouvel auteur

#ajouter un nouveau genre

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


 #    st.session_state.auteurs = ['Choisir un auteur', 'Michael McDowell', 'Dean Koontz', 'Stephen King',
 #    'Beatrix Potter', 'Beatrice Sparks','Agatha Christie', 'Sylvie Baron', 'Satoshi Yagisawa','Dennis Lehane',
 #    'Charles Duchaussois','Éléonore Devillepoix','Antonio Moresco', 'Amélie Nothomb', 'Annie Ernaux', 'Antoine de Saint-Exupéry', 'Albert Camus', 'Arthur Conan Doyle',
 # 'Bernard Werber', 'Boris Vian', 'Colette', 'Dan Brown', 'Douglas Adams',
 # 'Edgar Allan Poe', 'Émile Zola', 'Ernest Hemingway', 'Françoise Sagan', 'Frank Herbert']

# ajouter un nouvel auteur

#ajouter un nouveau genre

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