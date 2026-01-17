import requests
import streamlit as st

class LienApi:
    def __init__(self):
        self = self
    def recup_options(self, endpoint):
        try:
            res = requests.get(f"http://127.0.0.1:8000/{endpoint}")
            if res.status_code == 200:
                items = res.json()

                return [item['nom'] for item in items]
            return []
        except Exception as e:
            print(f"Erreur API sur {endpoint}: {e}")
            return []
