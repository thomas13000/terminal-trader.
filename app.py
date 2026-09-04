import streamlit as st
from datetime import datetime

# 1. Configuration de la page
st.set_page_config(
    page_title="TERMINAL TRADER PRO",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. État de la navigation
if "page" not in st.session_state:
    st.session_state.page = "welcome"

# 3. CSS Global HUD / Trading Terminal
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&family=JetBrains+Mono:wght@400;600;700;800&family=Orbitron:wght@600;800;900&display=swap');

        /* Masquage des éléments par défaut Streamlit */
        header[data-testid="stHeader"], footer, [data-testid="stToolbar"] {
            display: none !important;
            visibility: hidden !important;
        }

        /* Style global du body */
        .stApp {
            background-color: #080b10 !important;
            color: #eaecef !important;
            font-family: 'Inter', sans-serif !important;
        }

        .main .block-container {
            padding: 20px 40px !important;
            max-width: 100vw !important;
        }

        /* Overlays HUD : Viseurs dans les 4 coins */
        .corner-reticle {
            position: fixed; width: 30px; height: 30px; z-index: 99; pointer-events: none;
            border: 2px solid rgba(240, 185, 11, 0.4);
        }
        .corner-tl { top: 15px; left: 15px; border-right: none; border-bottom: none; }
        .corner-tr { top: 15px; right: 15px; border-left: none; border-bottom: none; }
        .corner-bl { bottom: 15px; left: 15px; border-right: none; border-top: none; }
        .corner-br { bottom: 15px; right: 15px; border-left: none; border-top: none; }

        /* Cartes et Panneaux HUD */
        .hud-card {
            background: rgba(13, 17, 23, 0.85);
            border: 1px solid rgba(240, 185, 11, 0.25);
            border-radius: 14px;
            padding: 20px 24px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.6);
            backdrop-filter: blur(12px);
            margin-bottom: 16px;
        }

        .hud-title {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.4rem;
            font-weight: 900;
            color: #ffffff;
            letter-spacing: 2px;
        }

        .hud-gold { color: #f0b90b; }
        .hud-cyan { color: #00f3ff; }
        .hud-green { color: #0ecb81; }
        .hud-red { color: #f6465d; }

        .mono-text {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.8rem;
            color: #848e9c;
        }

        /* Cartes de Tickers de Marché */
        .ticker-card {
            background: rgba(18, 24, 38, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 10px;
            padding: 12px 16px;
            margin-bottom: 10px;
        }

        /* Style du Bouton Streamlit Natif (Bouton Néon Dové) */
        div.stButton > button {
            width: 100% !important;
            background: linear-gradient(135deg, #f0b90b 0%, #d4a007 100%) !important;
            color: #080b10 !important;
            font-family: 'Orbitron', sans-serif !important;
            font-size: 1.05rem !important;
            font-weight: 900 !important;
            letter-spacing: 2px !important;
            border-radius: 12px !important;
            padding: 16px 24px !important;
            border: none !important;
            box-shadow: 0 0 25px rgba(240, 185, 11, 0.45) !important;
            cursor: pointer !important;
            transition: all 0.25s ease-in-out !important;
        }

        div.stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 0 35px rgba(240, 185, 11, 0.75), 0 0 15px #00f3ff !important;
            color: #000000 !important;
        }
    </style>

    <!-- Overlay Viseurs HUD -->
    <div class="corner-reticle corner-tl"></div>
    <div class="corner-reticle corner-tr"></div>
    <div class="corner-reticle corner-bl"></div>
    <div class="corner-reticle corner-br"></div>
""", unsafe_allow_html=True)


# ==========================================
# PAGE 1 : WELCOME / TERMINAL DASHBOARD
# ==========================================
if st.session_state.page == "welcome":

    # Horloge et date du système
    now = datetime.utcnow()
    time_utc = now.strftime("%H:%M:%S")
    date_str = now.strftime("%d %b %Y").upper()

    # --- HEADER HUD ---
    st.markdown(f"""
        <div class="hud-card" style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 24px;">
            <div style="display:flex; align-items:center; gap:16px;">
                <div style="width:42px; height:42px; background:linear-gradient(135deg, #f0b90b, #d4a007); border-radius:10px; display:flex; align-items:center; justify-content:center; font-family:'Orbitron'; font-weight:900; color:#000; font-size:1.3rem;">⚡</div>
                <div>
                    <div class="hud-title">TERMINAL TRADER <span class="hud-gold">PRO</span></div>
                    <div class="mono-text">QUANTITATIVE MARKET INTELLIGENCE — v5.5</div>
                </div>
            </div>
            <div style="display:flex; gap:30px; align-items:center;">
                <div style="text-align:right;">
                    <div class="mono-text" style="color:#00f3ff; font-weight:700;">{time_utc} UTC</div>
                    <div class="mono-text">{date_str}</div>
                </div>
                <div class="mono-text hud-green" style="background:rgba(14,203,129,0.1); padding:6px 14px; border-radius:20px; border:1px solid rgba(14,203,129,0.3); display:flex; align-items:center; gap:8px;">
                    <span style="width:8px; height:8px; background:#0ecb81; border-radius:50%; display:inline-block; box-shadow:0 0 8px #0ecb81;"></span>
                    SYSTEM ONLINE
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # --- CONTENU PRINCIPAL (2 COLONNES) ---
    col_left, col_right = st.columns([2.2, 1], gap="medium")

    with col_left:
        # Bloc d'accès central
        st.markdown("""
            <div class="hud-card">
                <div class="mono-text hud-gold" style="background:rgba(240,185,11,0.1); padding:4px 12px; border-radius:20px; width:fit-content; border:1px solid rgba(240,185,11,0.3); margin-bottom:12px;">
                    ● NOEUD ACTIF : LONDON-01
                </div>
                <div class="hud-title" style="font-size:1.6rem; margin-bottom:8px;">
                    PORTAIL DE DÉCISION QUANTITATIVE
                </div>
                <div style="color:#848e9c; font-size:0.9rem; line-height:1.5; margin-bottom:20px;">
                    Accès sécurisé aux flux multi-actifs, modèles d'arbitrage et métriques d'exécution à faible latence. 
                    Cliquez sur le bouton ci-dessous pour initialiser l'environnement de travail.
                </div>
            </div>
        """, unsafe_allow_html=True)

        # Bouton Natif Streamlit (100% fiable)
        if st.button("ENTRER DANS LE TERMINAL ➔"):
            st.session_state.page = "hub"
            st.rerun()

        # Métriques réseau / système sous le bouton
        st.markdown("<br>", unsafe_allow_html=True)
        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric(label="Latence Réseau", value="12.4 ms", delta="-1.2 ms")
        with m2:
            st.metric(label="Flux Prix / sec", value="4 850", delta="+320")
        with m3:
            st.metric(label="Statut Moteur Algo", value="NOMINAL", delta="100 %")

    with col_right:
        # Panneau des marchés / Tickers en direct
        st.markdown("""
            <div class="hud-card">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
                    <div class="mono-text hud-gold" style="font-weight:800;">⚡ MARCHÉS EN DIRECT</div>
                    <div class="mono-text">REALTIME</div>
                </div>
                
                <div class="ticker-card">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span style="font-weight:700; color:#fff;">BTC / USDT</span>
                        <span class="hud-green" style="font-family:'JetBrains Mono'; font-weight:700;">+2.45 %</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-top:4px;">
                        <span class="mono-text">$ 94 250,10</span>
                        <span class="mono-text" style="font-size:0.7rem;">Vol: 2.1B</span>
                    </div>
                </div>

                <div class="ticker-card">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span style="font-weight:700; color:#fff;">ETH / USDT</span>
                        <span class="hud-green" style="font-family:'JetBrains Mono'; font-weight:700;">+3.12 %</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-top:4px;">
                        <span class="mono-text">$ 3 480,50</span>
                        <span class="mono-text" style="font-size:0.7rem;">Vol: 1.4B</span>
                    </div>
                </div>

                <div class="ticker-card">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span style="font-weight:700; color:#fff;">NASDAQ (US100)</span>
                        <span class="hud-red" style="font-family:'JetBrains Mono'; font-weight:700;">-0.18 %</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-top:4px;">
                        <span class="mono-text">21 240,10 pts</span>
                        <span class="mono-text" style="font-size:0.7rem;">NY-CLOSE</span>
                    </div>
                </div>

                <div class="ticker-card">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span style="font-weight:700; color:#fff;">OR (XAU / USD)</span>
                        <span class="hud-green" style="font-family:'JetBrains Mono'; font-weight:700;">+0.84 %</span>
                    </div>
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-top:4px;">
                        <span class="mono-text">$ 2 688,30</span>
                        <span class="mono-text" style="font-size:0.7rem;">COMEX</span>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)


# ==========================================
# PAGE 2 : HUB / WORKSPACE (PAGE VIERGE)
# ==========================================
elif st.session_state.page == "hub":

    if st.button("← RETOUR AU MENU PRINCIPAL"):
        st.session_state.page = "welcome"
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
        <div class="hud-card">
            <div class="hud-title">🚀 HUB DU TERMINAL <span class="hud-gold">(PAGE 2)</span></div>
            <p style="color:#848e9c; margin-top:8px;">
                Espace de travail prêt. La transition s'est faite de manière 100 % fluide et instantanée.
            </p>
        </div>
    """, unsafe_allow_html=True)
