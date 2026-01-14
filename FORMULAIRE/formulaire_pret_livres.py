import streamlit as st
import requests
st.markdown('# Prêt livres')
st.sidebar.markdown('# Prêt pokemon')

#Ajout d'amis
#combien d'exemplaire, compteur d'exemplaire

liste_amis = ['Choisir un ami', 'Ronflex', 'Xavier Dupont de Ligonnès', 'Francky Vincent', 'Elon Musk', 'Donald Trump']
Amis = st.selectbox("Ami*", liste_amis)


