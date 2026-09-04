import streamlit as st
from datetime import datetime

# ==========================================
# 1. INITIALISATION DE LA SESSION
# ==========================================
# On vérifie si la variable "page" existe. Sinon, on la crée sur "welcome".
if "page" not in st.session_state:
    st.session_state.page = "welcome"

# ==========================================
# PAGE 1 : ACCUEIL (WELCOME)
# ==========================================
if st.session_state.page == "welcome":
    st.title("Bienvenue sur l'Accueil")
    
    # Bouton pour aller vers le Hub
    if st.button("ENTRER DANS LE TERMINAL 🚀"):
        st.session_state.page = "hub"
        st.rerun()

# ==========================================
# PAGE 2 : HUB / WORKSPACE (100% PYTHON)
# ==========================================
elif st.session_state.page == "hub":

    # --- 1. Variables de la page ---
    latency_ms = 42
    paris_time = datetime.now().strftime('%H:%M:%S')
    ny_time = datetime.now().strftime('%H:%M:%S') # (Remarque: sans pytz/zoneinfo l'heure NY sera la même que ton PC)

    # --- 2. CSS pour embellir les composants Streamlit ---
    st.markdown("""
        <style>
        .gold-text { color: #f0b90b; font-weight: 900; }
        .blue-text { color: #00f3ff; font-weight: bold; }
        .sub-text { font-size: 0.8rem; color: #848e9c; }
        
        /* Design du bouton de retour */
        [data-testid="stButton"] > button {
            background-color: #f0b90b;
            color: #000000;
            border: none;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        [data-testid="stButton"] > button:hover {
            background-color: #d4a007;
            box-shadow: 0 0 10px rgba(240, 185, 11, 0.5);
        }
        </style>
    """, unsafe_allow_html=True)

    # --- 3. Barre d'en-tête en colonnes Streamlit ---
    col1, col2, col3, col4 = st.columns([3, 3, 2, 2], vertical_alignment="center")

    with col1:
        st.markdown("#### ⚡ TERMINAL TRADER <span class='gold-text'>PRO</span>", unsafe_allow_html=True)
        st.markdown("<div class='sub-text' style='margin-top:-10px;'>QUANTITATIVE WORKSPACE</div>", unsafe_allow_html=True)

    with col2:
        st.markdown(f"**🇫🇷 PARIS:** {paris_time} &nbsp;|&nbsp; **🇺🇸 NY:** {ny_time}")

    with col3:
        st.markdown(f"<span class='sub-text'>LATENCE:</span> <span class='blue-text'>{latency_ms} ms</span><br>🟢 <span style='color:#0ecb81; font-weight:bold; font-size:0.9rem;'>ONLINE</span>", unsafe_allow_html=True)

    with col4:
        # BOUTON NATIF STREAMLIT
        if st.button("← RETOUR ACCUEIL", use_container_width=True):
            st.session_state.page = "welcome"
            st.rerun()

    st.divider()

    # --- 4. Le contenu de ton Hub ---
    st.success("🚀 WORKSPACE QUANTITATIF PRÊT - Zéro HTML, 100% Python")
    
    dash_col1, dash_col2 = st.columns(2)
    with dash_col1:
        st.info("Graphique du marché ici")
    with dash_col2:
        st.warning("Logs du bot de trading ici")
