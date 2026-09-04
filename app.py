import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo
import pandas as pd
import numpy as np

# ==========================================
# 0. CONFIGURATION DE LA PAGE (À mettre en TOUT PREMIER)
# ==========================================
st.set_page_config(
    page_title="Terminal Trader Pro",
    page_icon="⚡",
    layout="wide", # Mode plein écran (indispensable pour un dashboard)
    initial_sidebar_state="collapsed"
)

# ==========================================
# 1. GESTION DE L'ÉTAT (SESSION STATE)
# ==========================================
def init_session():
    """Initialise les variables de session si elles n'existent pas."""
    if "page" not in st.session_state:
        st.session_state.page = "welcome"

# ==========================================
# 2. PAGE 1 : ACCUEIL
# ==========================================
def show_welcome_page():
    # Centrer le contenu de l'accueil
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.title("⚡ Accueil - Terminal Pro")
        st.write("Bienvenue dans votre espace de trading quantitatif.")
        
        st.write("") # Espace
        if st.button("ENTRER DANS LE TERMINAL 🚀", use_container_width=True):
            st.session_state.page = "hub"
            st.rerun()

# ==========================================
# 3. PAGE 2 : HUB / WORKSPACE
# ==========================================
def show_hub_page():
    # --- Calcul des vraies heures (Paris et NY) ---
    try:
        paris_time = datetime.now(ZoneInfo("Europe/Paris")).strftime('%H:%M:%S')
        ny_time = datetime.now(ZoneInfo("America/New_York")).strftime('%H:%M:%S')
    except Exception:
        # Sécurité si le système ne supporte pas zoneinfo
        paris_time = datetime.now().strftime('%H:%M:%S')
        ny_time = datetime.now().strftime('%H:%M:%S')

    latency_ms = 42 # Simulation de latence

    # --- CSS pour le style Cyber/Terminal ---
    st.markdown("""
        <style>
        .gold-text { color: #f0b90b; font-weight: 900; letter-spacing: 1px;}
        .blue-text { color: #00f3ff; font-weight: bold; }
        .sub-text { font-size: 0.8rem; color: #848e9c; }
        
        /* Personnalisation du bouton retour */
        [data-testid="stButton"] > button {
            background-color: transparent;
            color: #f0b90b;
            border: 1px solid #f0b90b;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        [data-testid="stButton"] > button:hover {
            background-color: #f0b90b;
            color: #000000;
            box-shadow: 0 0 15px rgba(240, 185, 11, 0.4);
        }
        </style>
    """, unsafe_allow_html=True)

    # --- Barre d'en-tête ---
    col_logo, col_clocks, col_status, col_btn = st.columns([3, 3, 2, 2], vertical_alignment="center")

    with col_logo:
        st.markdown("### ⚡ TERMINAL TRADER <span class='gold-text'>PRO</span>", unsafe_allow_html=True)
        st.markdown("<div class='sub-text' style='margin-top:-15px;'>QUANTITATIVE WORKSPACE // V.2.0</div>", unsafe_allow_html=True)

    with col_clocks:
        st.markdown(f"**🇫🇷 PARIS:** {paris_time} &nbsp;&nbsp;|&nbsp;&nbsp; **🇺🇸 NY:** {ny_time}")

    with col_status:
        st.markdown(f"<span class='sub-text'>LATENCE SERVER:</span> <span class='blue-text'>{latency_ms} ms</span><br>🟢 <span style='color:#0ecb81; font-weight:bold; font-size:0.9rem;'>SYSTEM ONLINE</span>", unsafe_allow_html=True)

    with col_btn:
        if st.button("← QUITTER LE TERMINAL", use_container_width=True):
            st.session_state.page = "welcome"
            st.rerun()

    st.divider() # Ligne de séparation élégante

    # --- Contenu du Dashboard (Exemple réaliste) ---
    st.markdown("#### 📊 Aperçu du Marché")
    
    # 1. Ligne de métriques (KPIs)
    m1, m2, m3, m4 = st.columns(4)
    m1.metric(label="BTC/USD", value="$64,230.50", delta="+2.5%")
    m2.metric(label="ETH/USD", value="$3,450.10", delta="-0.8%")
    m3.metric(label="PNL Latent", value="+$1,240.00", delta="+12%")
    m4.metric(label="Risque Portefeuille", value="Modéré", delta="Stable", delta_color="off")

    st.write("") # Espace

    # 2. Graphiques et Tableaux
    col_chart, col_logs = st.columns([2, 1]) # Le graphique prend 2/3 de l'espace, les logs 1/3
    
    with col_chart:
        st.caption("📈 Évolution du PNL (Simulation 7 jours)")
        # Génération de fausses données pour l'exemple
        chart_data = pd.DataFrame(np.random.randn(20, 3) * 100 + 1000, columns=["Algo 1", "Algo 2", "Algo 3"])
        st.line_chart(chart_data, height=300)

    with col_logs:
        st.caption("🤖 Logs du Bot en direct")
        # Faux logs dans un cadre d'alerte ou dataframe
        logs = pd.DataFrame({
            "Heure": ["10:45", "10:42", "10:30", "10:15"],
            "Action": ["ACHAT BTC", "VENTE ETH", "SCAN MARCHÉ", "DÉMARRAGE"],
            "Statut": ["Succès", "Succès", "En cours", "OK"]
        })
        st.dataframe(logs, hide_index=True, use_container_width=True, height=300)


# ==========================================
# 4. POINT D'ENTRÉE DU SCRIPT (ROUTAGE)
# ==========================================
init_session()

# On affiche la page correspondante à l'état de la session
if st.session_state.page == "welcome":
    show_welcome_page()
elif st.session_state.page == "hub":
    show_hub_page()
