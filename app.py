import streamlit as st
import streamlit.components.v1 as components

# Configuration de la page Streamlit en plein écran
st.set_page_config(
    page_title="Terminal Trader Pro",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Suppression des marges et du menu par défaut de Streamlit
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {
            padding: 0rem !important;
            max-width: 100% !important;
        }
        iframe {
            display: block;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

# Lecture du fichier HTML 3D
with open("welcome.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# Rendu de la page 3D interactive
components.html(html_code, height=950, scrolling=False)
      
