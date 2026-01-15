import streamlit as st
import requests

st.title("Gestion des Amis & Prêts")

if "amis" not in st.session_state:
    st.session_state.amis = ['Choisir un ami', 'Ronflex', 'Xavier Dupont de Ligonnès', 'Lebron James', 'Britney Spears']

# FORMULAIRE AJOUT AMI
Ami = st.selectbox('Mon ami', st.session_state.amis)
# with st.expander("Ajouter un nouvel ami"):
#     nom = st.text_input("Nom de l'ami")
#     if st.button("Enregistrer l'ami"):
#         if nom and nom not in st.session_state.amis:
#             st.session_state.amis.append(nom)
#             st.success(f"{nom} ajouté !")
#             st.rerun()
# FORMULAIRE PRÊT
st.subheader("Enregistrer un prêt")

#on récupère les livres via l'API pour connaître les exemplaires
try:
    res = requests.get('http://127.0.0.1:8000/livres') #qui va changer
    livres = res.json()

    #on garde que les livres qui ont au moins 1 exemplaire
    livres_dispo = [livre for livre in livres if livre.get('Exemplaire', 0) > 0]
    options_livres = {livre['Titre']: livre for livre in livres_dispo}

    ami = st.selectbox("Qui es tu ?", st.session_state.amis)
    titre_choisi = st.selectbox("Livre à prêter", ["Choisir un livre"] + list(options_livres.keys()))

    if st.button("Valider le prêt"):
        if ami != "Choisir un ami" and titre_choisi != "Choisir un livre":
            livre_data = options_livres[titre_choisi]

            #on appelle API pour dire "Prêt effectué"
            #API devra faire Exemplaire = Exemplaire - 1
            st.success(f"Livre prêté à {ami} ! (Stock restant : {livre_data['Exemplaire'] - 1})")
        else:
            st.error("Sélectionne un ami et un livre.")
except Exception as e:
    st.error(f"Erreur de connexion API : {e}")