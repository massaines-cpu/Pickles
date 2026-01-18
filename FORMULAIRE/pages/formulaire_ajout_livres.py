import streamlit as st
import requests
import datetime


# -----------------------------
# Fonction utilitaire API
# -----------------------------
def recup_options(endpoint):
    try:
        # Appel générique vers un endpoint (auteurs, genres, etc.)
        res = requests.get(f"http://127.0.0.1:8000/{endpoint.lower()}")
        if res.status_code == 200:
            items = res.json()

            # Compréhension de liste :
            # on extrait uniquement "nom" si la clé existe
            return [item['nom'] for item in items if 'nom' in item]

        return []
    except Exception as e:
        # Erreur visible directement dans l’UI Streamlit
        st.error(f"Erreur API sur {endpoint}: {e}")
        return []


# -----------------------------
# Initialisation Streamlit
# -----------------------------
st.markdown('# Bibliothèque de Maxime')
st.sidebar.markdown('# Bibliothèque de Maxime')

# Liste fixe (pas issue de l’API)
liste_etat = ['Choisir un état', 'Mauvais', 'Bon', 'Très Bon', 'Neuf']


# -----------------------------
# Chargement en session_state
# -----------------------------
# session_state permet de garder les données
# entre les rerun Streamlit (boutons, formulaires…)

if "auteurs" not in st.session_state:
    st.session_state.auteurs = recup_options("auteurs")

if "genres" not in st.session_state:
    st.session_state.genres = recup_options("genres")

if "series" not in st.session_state:
    # "Aucune" est un faux choix volontaire
    st.session_state.series = ['Aucune'] + recup_options("series")

if "editeurs" not in st.session_state:
    # "Choisir un éditeur" sert à forcer une sélection valide
    st.session_state.editeurs = ["Choisir un éditeur"] + recup_options("editeurs")

if "editions" not in st.session_state:
    st.session_state.editions = recup_options("editions")


# -----------------------------
# Formulaire principal
# -----------------------------
Titre = st.text_input('Titre*: ', key="id_titre")

Auteur = st.multiselect(
    "Auteur*",
    st.session_state.auteurs,
    key="id_auteurs"
)

# Ajout dynamique d’un auteur côté UI
nouvel_auteur = st.text_input("Ajouter un nouvel auteur")
if st.button("Ajouter l'auteur"):
    if nouvel_auteur.strip() != "" and nouvel_auteur not in st.session_state.auteurs:
        st.session_state.auteurs.append(nouvel_auteur)
        st.success(f"Auteur ajouté : {nouvel_auteur}")
        st.rerun()  # force le rafraîchissement de l’interface


Resume = st.text_input('Résumé: ')

Serie = st.selectbox(
    'Série: ',
    st.session_state.series,
    key="id_serie"
)

# Même logique que pour les auteurs
nouvelle_saga = st.text_input("Ajouter une nouvelle saga")
if st.button("Ajouter une saga"):
    if nouvelle_saga.strip() != "" and nouvelle_saga not in st.session_state.series:
        st.session_state.series.append(nouvelle_saga)
        st.success(f"Série ajoutée : {nouvelle_saga}")
        st.rerun()


Genre = st.multiselect(
    'Genre*: ',
    st.session_state.genres,
    key="id_genre"
)

nouveau_genre = st.text_input("Ajouter un nouveau genre")
if st.button("Ajouter un genre"):
    if nouveau_genre.strip() != "" and nouveau_genre not in st.session_state.genres:
        st.session_state.genres.append(nouveau_genre)
        st.success(f"Genre ajouté : {nouveau_genre}")
        st.rerun()


# -----------------------------
# Année sécurisée
# -----------------------------
annee_actuelle = datetime.date.today().year

Annee = st.number_input(
    "Année de publication*:",
    min_value=1450,          # Gutenberg vibes
    max_value=annee_actuelle,
    value=annee_actuelle,
    step=1,
    key="id_annee"
)


Editeur = st.selectbox(
    'Editeur*: ',
    st.session_state.editeurs,
    key="id_editeur"
)

nouvel_editeur = st.text_input("Ajouter un nouvel éditeur")
if st.button("Ajouter un éditeur"):
    if nouvel_editeur.strip() != "" and nouvel_editeur not in st.session_state.editeurs:
        st.session_state.editeurs.append(nouvel_editeur)
        st.success(f"Éditeur ajouté : {nouvel_editeur}")
        st.rerun()


Exemplaire = st.number_input(
    "Nombre d'exemplaires*:",
    min_value=1,
    value=1,
    step=1
)


# -----------------------------
# Gestion dynamique des exemplaires
# -----------------------------
editions_liste = []
etats_liste = []

# On génère autant de lignes que d’exemplaires
if st.session_state.editions:
    st.write("Détails des exemplaires")

    for i in range(Exemplaire):
        st.write(f"**Exemplaire n°{i + 1}**")

        # Colonnes Streamlit (UI uniquement)
        col_ed, col_et = st.columns(2)

        with col_ed:
            ed_val = st.selectbox(
                f"Édition n°{i + 1}",
                st.session_state.editions,
                index=i,
                key=f"edition_{i}"  # clé unique OBLIGATOIRE
            )

        with col_et:
            et_val = st.selectbox(
                f"État n°{i + 1}",
                liste_etat[1:],     # on enlève "Choisir un état"
                index=i % (len(liste_etat) - 1),
                key=f"etat_{i}"
            )

        # On stocke les choix pour l’envoi API
        editions_liste.append(ed_val)
        etats_liste.append(et_val)


# Ajout dynamique d’une édition
nouvelle_edition_nom = st.text_input(
    "Si l'édition n'est pas dans la liste, ajoutez-la ici :"
)

if st.button("Enregistrer cette nouvelle édition"):
    if nouvelle_edition_nom.strip() != "" and nouvelle_edition_nom not in st.session_state.editions:
        st.session_state.editions.append(nouvelle_edition_nom)
        st.success(f"Édition '{nouvelle_edition_nom}' ajoutée à la liste !")
        st.rerun()


ISBN = st.number_input('ISBN*: ', step=1)


# -----------------------------
# Debug / visualisation des données
# -----------------------------
st.write("Formulaire livre rempli :", {
    "Titre": Titre,
    "Auteurs": Auteur,
    "Resume": Resume,
    "Serie": Serie if Serie != "Aucune" else None,
    "Genres": Genre,
    "Année": Annee,
    "Editions": editions_liste,
    "Editeur": Editeur,
    "Etats": etats_liste,
    "Exemplaires": Exemplaire,
    "ISBN": ISBN
})


# -----------------------------
# Envoi vers l’API
# -----------------------------
if st.button('Ajouter ce livre à la bibliothèque'):
    erreurs = []

    # Validation côté front (évite 422 côté API)
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

    if erreurs:
        st.error(f"IL MANQUE DES INFOS HEHO : {', '.join(erreurs)}")
    else:
        # Payload final conforme à l’API
        data = {
            'titre': Titre,
            'auteurs': Auteur,
            'resume': Resume.strip() if Resume.strip() != "" else None,
            'annee': str(Annee),
            'editions': editions_liste,
            'genres': Genre,
            'serie': "" if Serie == "Aucune" else Serie,
            'editeur': Editeur,
            'exemplaires': int(Exemplaire),
            'etats': etats_liste,
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
