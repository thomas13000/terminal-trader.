import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Terminal Trader Pro",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "page" not in st.session_state:
    st.session_state.page = "welcome"

# ==========================================
# PAGE 1 : WELCOME / AUTH SCREEN
# ==========================================
if st.session_state.page == "welcome":
    st.markdown("""
        <style>
        html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
            overflow: hidden !important;
            height: 100vh !important;
            background-color: #0d1117;
        }
        header {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        .block-container { 
            padding-top: 0.5rem !important; 
            padding-bottom: 0.2rem !important;
            padding-left: 2rem !important;
            padding-right: 2rem
