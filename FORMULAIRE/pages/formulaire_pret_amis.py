import streamlit as st
import requests
import pandas as pd

def recup_options(endpoint):
    try:
        res = requests.get(f"http://127.0.0.1:8000/{endpoint.lower()}")
        if res.status_code == 200:
            # items = res.json()
            return res.json()  #dico complet
        return []
    except Exception as e:
        st.error(f"Erreur API sur {endpoint}: {e}")
        return []

# 1. INITIALISATION DE L'ANNUAIRE
if "amis_details" not in st.session_state:
    st.session_state.amis_details= recup_options("amis")

#2 LISTE DES AMIS
st.subheader("Liste des ami.es")
if st.session_state.amis_details and isinstance(st.session_state.amis_details[0], dict):
    df_amis = pd.DataFrame(st.session_state.amis_details)
    cols_to_show = ["nom", "telephone", "ecole"]
    df_amis = df_amis[[c for c in cols_to_show if c in df_amis.columns]]

    df_amis = df_amis.rename(columns={
        "nom": "Nom",
        "telephone": "Téléphone",
        "ecole": "École / Établissement"
    })
    st.dataframe(df_amis, width="stretch", hide_index=True)
else:
    st.info("Aucun.e ami.e trouvé.e ou format de données incorrect.")

st.divider()

st.subheader("Ajouter un nouvel ami dans l'annuaire")
col1, col2, col3 = st.columns(3)
with col1:
    new_nom = st.text_input("Nom de l'ami.e")
with col2:
    new_ecole = st.text_input("École / Établissement")
with col3:
    new_tel = st.text_input("Numéro de téléphone")

if st.button("Enregistrer dans l'annuaire"):
    # On crée le dictionnaire avec les clés exactes du AmiModel
    nouveau_pote = {
        "nom": new_nom,
        "telephone": new_tel,
        "ecole": new_ecole
    }
    # ON ENVOIE À L'API
    reponse = requests.post("http://127.0.0.1:8000/amis", json=nouveau_pote)
    if reponse.status_code == 200:
        st.success("Ami.e ajouté.e dans la BDD")
        if "amis_details" in st.session_state:
            del st.session_state.amis_details

        st.rerun()

st.divider()

# 4. ENREGISTRER UN PRÊT
st.subheader("Enregistrer un prêt")

try:
    res = requests.get('http://127.0.0.1:8000/livres')
    livres = res.json()
    options_livres = {livre['titre']: livre for livre in livres} #{livre['titre']: livre for livre in livres if livre.get('exemplaires', 0) > 0}

    col_a, col_b = st.columns(2)

    with col_a:
        noms_list = ["Choisir un ami"]
        if isinstance(st.session_state.amis_details, list):
            for ami in st.session_state.amis_details:
                if isinstance(ami, dict):
                    noms_list.append(ami.get('nom'))
                else:
                    noms_list.append(str(ami))
        ami_choisi = st.selectbox("Qui emprunte le livre ?", noms_list)

    with col_b:
        titre_choisi = st.selectbox("Livre à prêter", ["Choisir un livre"] + list(options_livres.keys()))

    if titre_choisi != "Choisir un livre":
        livre_data = options_livres[titre_choisi]
        etats_bruts = livre_data['etats'].split(', ')#livre_data.get('etat', "")
        etats_possibles = [e.strip() for e in etats_bruts.split(",") if e.strip()]

        if etats_possibles:
            etat_prete = st.selectbox("Choisissez l'état de l'exemplaire prêté", etats_possibles)

            if st.button("Valider le prêt"):
                if ami_choisi != "Choisir un ami":
                    nouveau_stock = livre_data['exemplaires'] - 1
                    etats_possibles.remove(etat_prete)
                    nouveaux_etats_str = ", ".join(etats_possibles)

                    url = f"http://127.0.0.1:8000/livres/{livre_data['id']}"
                    payload = {
                        "exemplaires": nouveau_stock,
                        "emprunteur": ami_choisi,
                        "etat": nouveaux_etats_str
                    }

                    res_put = requests.put(url, json=payload)

                    if res_put.status_code == 200:
                        st.success(f"Prêt enregistré ! {titre_choisi} ({etat_prete}) est chez {ami_choisi}.")
                    else:
                        st.error("Erreur lors de la mise à jour du serveur.")
                else:
                    st.error("Veuillez sélectionner un ami dans la liste.")
        else:
            st.warning("Aucun exemplaire disponible n'a d'état renseigné.")

except Exception as e:
    st.error(f"Erreur de connexion API : {e}")

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
