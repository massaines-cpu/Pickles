import streamlit as st
import requests
import pandas as pd

st.title("Gestion des amis & prêts")

# 1. INITIALISATION DE L'ANNUAIRE
if "amis_details" not in st.session_state:
    st.session_state.amis_details = [
        {"Nom": "Ronflex", "École": "Université du Sommeil", "Téléphone": "0601020304"},
        {"Nom": "Lebron James", "École": "NBA High", "Téléphone": "0611223344"}
    ]

#2 LISTE DES AMIS
st.subheader("Liste des amis")
df_amis = pd.DataFrame(st.session_state.amis_details)
st.dataframe(df_amis, use_container_width=True, hide_index=True)

st.divider()

#3 AJOUTER UN AMI
st.subheader("Ajouter un nouvel ami dans l'annuaire")
col1, col2, col3 = st.columns(3)
with col1:
    new_nom = st.text_input("Nom de l'ami")
with col2:
    new_ecole = st.text_input("École / Établissement")
with col3:
    new_tel = st.text_input("Numéro de téléphone")

if st.button("Enregistrer dans l'annuaire"):
    if new_nom.strip() != "":
        if any(a['Nom'].lower() == new_nom.lower() for a in st.session_state.amis_details):
            st.warning("Cet ami est déjà dans la liste.")
        else:
            st.session_state.amis_details.append({
                "Nom": new_nom,
                "École": new_ecole,
                "Téléphone": new_tel
            })
            st.success(f"{new_nom} a été ajouté !")
            st.rerun()
    else:
        st.error("Le nom est obligatoire.")

st.divider()

# 4. ENREGISTRER UN PRÊT
st.subheader("Enregistrer un prêt")

try:
    # Récupération des livres via l'API
    res = requests.get('http://127.0.0.1:8000/livres')
    livres = res.json()
    options_livres = {livre['Titre']: livre for livre in livres if livre.get('Exemplaire', 0) > 0}

    col_a, col_b = st.columns(2)

    with col_a:
        noms_amis = ["Choisir un ami"] + [a['Nom'] for a in st.session_state.amis_details]
        ami_choisi = st.selectbox("Qui emprunte le livre ?", noms_amis)

    with col_b:
        titre_choisi = st.selectbox("Livre à prêter", ["Choisir un livre"] + list(options_livres.keys()))

    if titre_choisi != "Choisir un livre":
        livre_data = options_livres[titre_choisi]
        etats_bruts = livre_data.get('Etat', "")
        etats_possibles = [e.strip() for e in etats_bruts.split(",") if e.strip()]

        if etats_possibles:
            etat_prete = st.selectbox("Choisissez l'état de l'exemplaire prêté", etats_possibles)

            if st.button("Valider le prêt"):
                if ami_choisi != "Choisir un ami":
                    # --- LOGIQUE DE MISE À JOUR ---
                    # 1. Calcul du nouveau stock
                    nouveau_stock = livre_data['Exemplaire'] - 1

                    # 2. Retirer l'état prêté de la liste
                    etats_possibles.remove(etat_prete)
                    nouveaux_etats_str = ", ".join(etats_possibles)

                    # 3. Préparation des données pour l'API
                    url = f"http://127.0.0.1:8000/livres/{titre_choisi}"
                    payload = {
                        "Exemplaire": nouveau_stock,
                        "Emprunteur": ami_choisi,
                        "Etat": nouveaux_etats_str
                    }

                    # 4. Envoi de la requête PUT
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