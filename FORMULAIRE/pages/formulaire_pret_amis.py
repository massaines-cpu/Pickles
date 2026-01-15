import streamlit as st
import requests
import pandas as pd

st.title("Gestion des amis & prêts")

if "amis_details" not in st.session_state:
    st.session_state.amis_details = [
        {"Nom": "Ronflex", "École": "Université du Sommeil", "Téléphone": "0601020304"},
        {"Nom": "Lebron James", "École": "NBA High", "Téléphone": "0611223344"}
    ]
st.subheader("📋 Liste des amis")
df_amis = pd.DataFrame(st.session_state.amis_details)
st.dataframe(df_amis, use_container_width=True, hide_index=True)

st.divider()
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
            # Vérifier si l'ami existe déjà
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
st.subheader("Enregistrer un prêt")

try:
    res = requests.get('http://127.0.0.1:8000/livres') #qui va changer
    livres = res.json()

    #on garde que les livres qui ont au moins 1 exemplaire
    livres_dispo = [livre for livre in livres if livre.get('Exemplaire', 0) > 0]
    options_livres = {livre['Titre']: livre for livre in livres_dispo}

    # ami = st.selectbox("Qui es tu ?", st.session_state.amis)
    noms_amis = ["Choisir un ami"] + [a['Nom'] for a in st.session_state.amis_details]
    ami = st.selectbox("Qui emprunte le livre ?", noms_amis)
    titre_choisi = st.selectbox("Livre à prêter", ["Choisir un livre"] + list(options_livres.keys()))

    if st.button("Valider le prêt"):
        if ami != "Choisir un ami" and titre_choisi != "Choisir un livre":
            livre_data = options_livres[titre_choisi]
            nouveau_stock = livre_data['Exemplaire'] - 1
            url = f"http://127.0.0.1:8000/livres/{titre_choisi}" #lien qui faudra changer????
            res = requests.put(url, json={"Exemplaire": nouveau_stock, "Emprunteur": ami})
            if res.status_code == 200:
                st.success(f"Livre prêté à {ami}! (Stock actuel de '{titre_choisi}' : {nouveau_stock})")
            else:
                st.error('erreur maj')
        else:
            st.error("sélectionne un ami.")
except Exception as e:
    st.error(f"Erreur de connexion API : {e}")

# if "amis" not in st.session_state:
#     st.session_state.amis = ['Choisir un ami', 'Ronflex', 'Xavier Dupont de Ligonnès', 'Lebron James', 'Britney Spears']
#
# # FORMULAIRE AJOUT AMI
# ami = st.selectbox("Qui es tu ?", st.session_state.amis)
# nouvel_ami = st.text_input("Ajouter un nouvel ami")