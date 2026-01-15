# view_livres.py
import streamlit as st
import requests
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Bibliothèque", layout="wide")
st.title("Ma belle bibliothèque")

# ----------------------------
# Récupérer les livres depuis l'API
# ----------------------------
def fetch_livres():
    try:
        resp = requests.get(f"{API_URL}/livres")
        if resp.status_code == 200:
            return resp.json()
        return []
    except:
        return []

livres = fetch_livres()
if not livres:
    st.info("Aucun livre trouvé dans la base.")
else:
    # Convertir en DataFrame pour AgGrid
    df_livres = pd.DataFrame(livres)

    # Ajouter colonnes pour affichage clair
    df_livres["Auteurs"] = df_livres["auteurs"].apply(lambda x: ", ".join(x))
    df_livres["Genres"] = df_livres["genres"].apply(lambda x: ", ".join(x))

    # On ne montre que les colonnes utiles
    df_display = df_livres[[
        "id", "titre", "serie", "editeur", "edition", "annee",
        "Auteurs", "Genres", "exemplaires", "isbn"
    ]]

    # ----- GridOptions -----
    gb = GridOptionsBuilder.from_dataframe(df_display)
    gb.configure_selection(selection_mode="single", use_checkbox=True)
    gb.configure_columns(["id"], editable=False, width=50)
    gb.configure_columns(["titre", "serie", "editeur", "edition", "Auteurs", "Genres"], wrapText=True, autoHeight=True)
    gb.configure_grid_options(domLayout='normal', suppressRowClickSelection=True)
    grid_options = gb.build()

    # ----- Afficher le tableau -----
    grid_response = AgGrid(
        df_display,
        gridOptions=grid_options,
        update_mode=GridUpdateMode.SELECTION_CHANGED,
        fit_columns_on_grid_load=True,
        height=500,
        allow_unsafe_jscode=True
    )

    selected_rows = grid_response.get("selected_rows", [])

    if selected_rows:
        selected = selected_rows[0]
        livre_id = selected["id"]

        # Vérifier si au moins un exemplaire est prêté (ami_id != 1)
        resp_ex = requests.get(f"{API_URL}/exemplaires/{livre_id}")
        exemplaires = resp_ex.json() if resp_ex.status_code == 200 else []
        is_prete = any(ex.get("ami_id") != 1 for ex in exemplaires)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("❌ Supprimer le livre sélectionné"):
                r = requests.delete(f"{API_URL}/livre/{livre_id}")
                if r.json().get("success"):
                    st.success("Livre supprimé !")
                    st.experimental_rerun()
                else:
                    st.error(f"Erreur : {r.json().get('message')}")
        with col2:
            if is_prete:
                if st.button("✅ Marquer exemplaires disponibles"):
                    r = requests.post(f"{API_URL}/exemplaire/disponible/{livre_id}")
                    if r.json().get("success"):
                        st.success("Exemplaires remis disponibles !")
                        st.experimental_rerun()
                    else:
                        st.error(f"Erreur : {r.json().get('message')}")
            else:
                st.button("✅ Tous disponibles", disabled=True)
