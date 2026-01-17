import requests
import streamlit as st
import sys
import os

def recup_options(endpoint):
    try:
        res = requests.get(f"http://127.0.0.1:8000/{endpoint}")
        if res.status_code == 200:
            items = res.json()
            # On s'adapte au format de Noémie (liste de dict avec une clé 'nom')
            return [item['nom'] for item in items]
        return []
    except Exception as e:
        print(f"Erreur API sur {endpoint}: {e}")
        return []