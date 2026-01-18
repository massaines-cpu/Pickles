import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:8000"

# -----------------------------
# FONCTION POUR RÉCUPÉRER L’API
# -----------------------------
def recup_options(endpoint):
    try:
        url = API_URL + "/" + endpoint.lower()
        res = requests.get(url)

        if res.status_code == 200:
            return res.json()
        else:
            return []
    except Exception as e:
        st.error("Erreur API sur " + endpoint + " : " + str(e))
        return []


# ---------------------------------
# INITIALISATION DE LA LISTE D’AMIS
# ---------------------------------
if "amis_details" not in st.session_state:
    st.session_state.amis_details = recup_options("amis")


# ------------------
# LISTE DES AMIS
# ------------------
st.subheader("Liste des ami.es")

if st.session_state.amis_details and isinstance(st.session_state.amis_details[0], dict):

    df_amis = pd.DataFrame(st.session_state.amis_details)

    # Colonnes à afficher si elles existent
    colonnes = ["nom", "telephone", "ecole"]
    colonnes_existantes = []

    for col in colonnes:
        if col in df_amis.columns:
            colonnes_existantes.append(col)

    df_amis = df_amis[colonnes_existantes]

    # Renommage pour affichage
    df_amis = df_amis.rename(columns={
        "nom": "Nom",
        "telephone": "Téléphone",
        "ecole": "École / Établissement"
    })

    st.dataframe(df_amis, width="stretch", hide_index=True)

else:
    st.info("Aucun.e ami.e trouvé.e ou données incorrectes.")

st.divider()


# -------------------------
# AJOUT D’UN NOUVEL AMI
# -------------------------
st.subheader("Ajouter un nouvel ami dans l'annuaire")

col1, col2, col3 = st.columns(3)

with col1:
    new_nom = st.text_input("Nom de l'ami.e")

with col2:
    new_ecole = st.text_input("École / Établissement")

with col3:
    new_tel = st.text_input("Numéro de téléphone")

if st.button("Enregistrer dans l'annuaire"):

    # Dictionnaire envoyé à l’API
    nouveau_pote = {
        "nom": new_nom,
        "telephone": new_tel,
        "ecole": new_ecole
    }

    url_post = API_URL + "/amis"
    reponse = requests.post(url_post, json=nouveau_pote)

    if reponse.status_code == 200:
        st.success("Ami.e ajouté.e dans la BDD")

        # Forcer le rechargement des amis
        if "amis_details" in st.session_state:
            del st.session_state.amis_details

        st.rerun()

st.divider()


# -------------------------
# ENREGISTRER UN PRÊT
# -------------------------
st.subheader("Enregistrer un prêt")

try:
    livres = recup_options("livres")

    if not livres:
        st.info("Aucun livre disponible.")
    else:
        # Dictionnaire : titre → livre complet
        options_livres = {}
        for livre in livres:
            options_livres[livre["titre"]] = livre

        col_a, col_b = st.columns(2)

        # Choix de l’ami
        with col_a:
            liste_amis = ["Choisir un ami"]
            for ami in st.session_state.amis_details:
                liste_amis.append(ami["nom"])
            ami_choisi = st.selectbox("Qui emprunte ?", liste_amis)

        # Choix du livre
        with col_b:
            titres = list(options_livres.keys())
            titres.insert(0, "Choisir un livre")
            titre_choisi = st.selectbox("Livre à prêter", titres)

        if titre_choisi != "Choisir un livre":

            livre_data = options_livres[titre_choisi]

            # On garde uniquement les exemplaires disponibles
            exemplaires_dispos = []
            for ex in livre_data["exemplaires"]:
                if ex["ami_id"] is None:
                    exemplaires_dispos.append(ex)

            if not exemplaires_dispos:
                st.warning("Aucun exemplaire disponible pour ce livre.")
            else:
                # Création de listes pour l'affichage et récupération de l'exemplaire réel
                noms_exemplaires = []
                exemplaires_mapping = []

                for ex in exemplaires_dispos:
                    texte = "Exemplaire #" + str(ex["id"]) + " - État : " + ex["etat"]
                    noms_exemplaires.append(texte)
                    exemplaires_mapping.append(ex)

                # Sélection de l'exemplaire via son index
                choix_index = st.selectbox("Choisissez l’exemplaire", range(len(noms_exemplaires)),
                                           format_func=lambda i: noms_exemplaires[i])
                exemplaire_choisi = exemplaires_mapping[choix_index]

                if st.button("Valider le prêt"):

                    if ami_choisi == "Choisir un ami":
                        st.error("Veuillez choisir un ami.")
                    else:
                        # Récupération de l’id de l’ami
                        ami_id = None
                        for ami in st.session_state.amis_details:
                            if ami["nom"] == ami_choisi:
                                ami_id = ami["id"]

                        payload = {"ami_id": ami_id}

                        url_put = API_URL + "/exemplaires/" + str(exemplaire_choisi["id"]) + "/preter"
                        res = requests.put(url_put, json=payload)

                        if res.status_code == 200:
                            st.success("Livre prêté : " + titre_choisi + " à " + ami_choisi)
                            st.rerun()
                        else:
                            st.error("Erreur lors de l’enregistrement du prêt.")

except Exception as e:
    st.error("Erreur de connexion API : " + str(e))


    # st.session_state.amis_details = [
    # #     {"Nom": "Ronflex", "École": "Université du Sommeil", "Téléphone": "0601020304"},
    #     {"Nom": "Xavier Dupont de Ligonnès", "École": "Family school", "Téléphone": "0666666666"},
    #     {"Nom": "Lebron James", "École": "NBA High", "Téléphone": "0611223344"}
    # ]

#3 AJOUTER UN AMI
# st.subheader("Ajouter un nouvel ami dans l'annuaire")
# col1, col2, col3 = st.columns(3)
# with col1:
#     new_nom = st.text_input("Nom de l'ami")
# with col2:
#     new_ecole = st.text_input("École / Établissement")
# with col3:
#     new_tel = st.text_input("Numéro de téléphone")

# if st.button("Enregistrer dans l'annuaire"):
#     if new_nom.strip() != "":
#         if any(a['Nom'].lower() == new_nom.lower() for a in st.session_state.amis_details):
#             st.warning("Cet ami est déjà dans la liste.")
#         else:
#             st.session_state.amis_details.append({
#                 "Nom": new_nom,
#                 "École": new_ecole,
#                 "Téléphone": new_tel
#             })
#             st.success(f"{new_nom} a été ajouté !")
#             st.rerun()
#     else:
#         st.error("Le nom est obligatoire.")
#
# st.divider()