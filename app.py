import streamlit as st
import streamlit.components.v1 as components
import time
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

start_time = time.time()
latency_ms = round((time.time() - start_time) * 1000 + 12, 1)

# ==========================================
# STYLES CSS GLOBAL HUD (Positionnement Haut Max)
# ==========================================
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&family=JetBrains+Mono:wght@500;700;800&family=Orbitron:wght@600;800;900&display=swap');

        header[data-testid="stHeader"], footer, [data-testid="stToolbar"] {
            display: none !important;
            visibility: hidden !important;
        }

        html, body, .stApp, [data-testid="stAppViewContainer"], .main {
            height: 100vh !important;
            max-height: 100vh !important;
            overflow: hidden !important;
            background-color: #080b10 !important;
            color: #eaecef !important;
            font-family: 'Inter', sans-serif !important;
        }

        /* Remontée au sommet de la page */
        .main .block-container {
            padding: 2px 20px 10px 20px !important;
            max-width: 100vw !important;
            height: 100vh !important;
        }

        /* Viseurs 4 coins */
        .corner-reticle {
            position: fixed; width: 24px; height: 24px; z-index: 99; pointer-events: none;
            border: 2px solid rgba(240, 185, 11, 0.4);
        }
        .corner-tl { top: 6px; left: 6px; border-right: none; border-bottom: none; }
        .corner-tr { top: 6px; right: 6px; border-left: none; border-bottom: none; }
        .corner-bl { bottom: 6px; left: 6px; border-right: none; border-top: none; }
        .corner-br { bottom: 6px; right: 6px; border-left: none; border-top: none; }

        /* Header HUD collé en haut */
        .hud-header {
            background: rgba(13, 17, 23, 0.90);
            border: 1px solid rgba(240, 185, 11, 0.3);
            border-radius: 10px;
            padding: 8px 18px;
            margin-top: 0px;
            margin-bottom: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            backdrop-filter: blur(15px);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.7);
        }

        .hud-title {
            font-family: 'Orbitron', sans-serif;
            font-weight: 900;
            color: #ffffff;
            letter-spacing: 2px;
        }

        .hud-gold { color: #f0b90b; }
        .hud-green { color: #0ecb81; }

        .mono-text {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.78rem;
            color: #848e9c;
        }

        .hud-card {
            background: rgba(13, 17, 23, 0.85);
            border: 1px solid rgba(240, 185, 11, 0.22);
            border-radius: 14px;
            padding: 22px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.6);
        }

        /* Bouton Néon Streamlit */
        div.stButton > button {
            width: 100% !important;
            background: linear-gradient(135deg, #f0b90b 0%, #d4a007 100%) !important;
            color: #080b10 !important;
            font-family: 'Orbitron', sans-serif !important;
            font-size: 1rem !important;
            font-weight: 900 !important;
            letter-spacing: 2px !important;
            border-radius: 10px !important;
            padding: 16px 20px !important;
            border: none !important;
            box-shadow: 0 0 20px rgba(240, 185, 11, 0.4) !important;
            cursor: pointer !important;
        }

        div.stButton > button:hover {
            box-shadow: 0 0 30px rgba(240, 185, 11, 0.8), 0 0 12px #00f3ff !important;
            color: #000000 !important;
        }
    </style>

    <div class="corner-reticle corner-tl"></div>
    <div class="corner-reticle corner-tr"></div>
    <div class="corner-reticle corner-bl"></div>
    <div class="corner-reticle corner-br"></div>
""", unsafe_allow_html=True)


# ==========================================
# PAGE 1 : WELCOME SCREEN
# ==========================================
if st.session_state.page == "welcome":

    now = datetime.utcnow()
    time_utc = now.strftime("%H:%M:%S")

    # --- BARRE DU HAUT (Tout en haut) ---
    st.markdown(f"""
        <div class="hud-header">
            <div style="display:flex; align-items:center; gap:14px;">
                <div style="width:32px; height:32px; background:linear-gradient(135deg, #f0b90b, #d4a007); border-radius:8px; display:flex; align-items:center; justify-content:center; font-family:'Orbitron'; font-weight:900; color:#000; font-size:1rem;">⚡</div>
                <div>
                    <div class="hud-title" style="font-size:1.05rem; line-height:1.1;">TERMINAL TRADER <span class="hud-gold">PRO</span></div>
                    <div class="mono-text" style="font-size:0.65rem;">QUANTITATIVE MARKET INTELLIGENCE</div>
                </div>
            </div>
            <div style="display:flex; gap:20px; align-items:center;">
                <div class="mono-text" style="background:rgba(255,255,255,0.05); padding:3px 8px; border-radius:6px; border:1px solid rgba(255,255,255,0.1);">
                    MS SERVEUR : <span style="color:#00f3ff; font-weight:700;">{latency_ms} ms</span>
                </div>
                <div class="mono-text" style="color:#00f3ff; font-weight:700;">{time_utc} UTC</div>
                <div class="mono-text hud-green" style="background:rgba(14,203,129,0.1); padding:4px 10px; border-radius:20px; border:1px solid rgba(14,203,129,0.3); display:flex; align-items:center; gap:6px;">
                    <span style="width:7px; height:7px; background:#0ecb81; border-radius:50%; display:inline-block; box-shadow:0 0 8px #0ecb81;"></span>
                    SYSTEM ONLINE
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # --- DISPOSITION EN 2 COLONNES ---
    col_left, col_right = st.columns([1.6, 1.4], gap="medium")

    with col_left:
        st.markdown("""
            <div class="hud-card">
                <div class="mono-text hud-gold" style="background:rgba(240,185,11,0.1); padding:3px 10px; border-radius:15px; width:fit-content; border:1px solid rgba(240,185,11,0.3); margin-bottom:12px;">
                    ● NŒUD SYSTÈME : ACTIF
                </div>
                <div class="hud-title" style="font-size:1.4rem; margin-bottom:10px;">
                    PORTAIL DE DÉCISION QUANTITATIVE
                </div>
                <div style="color:#848e9c; font-size:0.88rem; line-height:1.5; margin-bottom:24px;">
                    Initialisez le terminal pour accéder au moteur d'analyse, aux modèles de corrélation et aux outils d'exécution en temps réel.
                </div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("ENTRER DANS LE TERMINAL ➔"):
            st.session_state.page = "hub"
            st.rerun()

    with col_right:
        # Cadre Jaune verticallisé et agrandi avec les 4 actifs empilés
        market_cards_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Orbitron:wght@700;900&family=JetBrains+Mono:wght@500;700&display=swap');
                
                * { box-sizing: border-box; }
                body {
                    margin: 0;
                    padding: 0;
                    background-color: transparent;
                    font-family: 'Inter', sans-serif;
                }

                .yellow-container {
                    background: rgba(13, 17, 23, 0.95);
                    border: 2px solid #f0b90b;
                    border-radius: 14px;
                    padding: 10px;
                    box-shadow: 0 0 25px rgba(240, 185, 11, 0.25);
                    display: flex;
                    flex-direction: column;
                    gap: 8px;
                }

                .container-header {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding-bottom: 6px;
                    border-bottom: 1px solid rgba(240, 185, 11, 0.25);
                }

                .title-text {
                    font-family: 'Orbitron', sans-serif;
                    font-weight: 900;
                    font-size: 0.82rem;
                    color: #f0b90b;
                    letter-spacing: 1.5px;
                }

                .pulse-tag {
                    display: flex;
                    align-items: center;
                    gap: 6px;
                    background: rgba(14,203,129,0.1);
                    padding: 2px 7px;
                    border-radius: 12px;
                    border: 1px solid rgba(14,203,129,0.3);
                    font-family: 'JetBrains Mono', monospace;
                    font-size: 0.6rem;
                    font-weight: 700;
                    color: #0ecb81;
                }

                .pulse-dot {
                    width: 5px;
                    height: 5px;
                    background-color: #0ecb81;
                    border-radius: 50%;
                    box-shadow: 0 0 6px #0ecb81;
                    animation: pulse-animation 1.2s infinite ease-in-out;
                }

                @keyframes pulse-animation {
                    0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(14, 203, 129, 0.7); }
                    70% { transform: scale(1.15); box-shadow: 0 0 0 5px rgba(14, 203, 129, 0); }
                    100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(14, 203, 129, 0); }
                }

                .asset-card {
                    background: rgba(22, 27, 34, 0.85);
                    border: 1px solid rgba(240, 185, 11, 0.2);
                    border-radius: 8px;
                    height: 115px;
                    overflow: hidden;
                }

                .asset-card:hover {
                    border-color: rgba(240, 185, 11, 0.6);
                }
            </style>
        </head>
        <body>
            <div class="yellow-container">
                <div class="container-header">
                    <div style="display:flex; align-items:center; gap:8px;">
                        <span style="color:#f0b90b; font-size:0.9rem;">⚡</span>
                        <span class="title-text">MARCHÉS EN DIRECT (1D INTRADAY)</span>
                    </div>
                    <div class="pulse-tag">
                        <span class="pulse-dot"></span>
                        <span>LIVE</span>
                    </div>
                </div>

                <!-- 1. NASDAQ -->
                <div class="asset-card">
                    <div class="tradingview-widget-container" style="height:100%; width:100%;">
                        <div class="tradingview-widget-container__widget" style="height:100%; width:100%;"></div>
                        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>
                        {
                          "symbol": "FOREXCOM:NSXUSD",
                          "width": "100%",
                          "height": "100%",
                          "locale": "fr",
                          "dateRange": "1D",
                          "colorTheme": "dark",
                          "isTransparent": true,
                          "autosize": true,
                          "largeChartUrl": ""
                        }
                        </script>
                    </div>
                </div>

                <!-- 2. DXY -->
                <div class="asset-card">
                    <div class="tradingview-widget-container" style="height:100%; width:100%;">
                        <div class="tradingview-widget-container__widget" style="height:100%; width:100%;"></div>
                        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>
                        {
                          "symbol": "CAPITALCOM:DXY",
                          "width": "100%",
                          "height": "100%",
                          "locale": "fr",
                          "dateRange": "1D",
                          "colorTheme": "dark",
                          "isTransparent": true,
                          "autosize": true,
                          "largeChartUrl": ""
                        }
                        </script>
                    </div>
                </div>

                <!-- 3. EUR / USD -->
                <div class="asset-card">
                    <div class="tradingview-widget-container" style="height:100%; width:100%;">
                        <div class="tradingview-widget-container__widget" style="height:100%; width:100%;"></div>
                        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>
                        {
                          "symbol": "FX:EURUSD",
                          "width": "100%",
                          "height": "100%",
                          "locale": "fr",
                          "dateRange": "1D",
                          "colorTheme": "dark",
                          "isTransparent": true,
                          "autosize": true,
                          "largeChartUrl": ""
                        }
                        </script>
                    </div>
                </div>

                <!-- 4. GOLD -->
                <div class="asset-card">
                    <div class="tradingview-widget-container" style="height:100%; width:100%;">
                        <div class="tradingview-widget-container__widget" style="height:100%; width:100%;"></div>
                        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>
                        {
                          "symbol": "OANDA:XAUUSD",
                          "width": "100%",
                          "height": "100%",
                          "locale": "fr",
                          "dateRange": "1D",
                          "colorTheme": "dark",
                          "isTransparent": true,
                          "autosize": true,
                          "largeChartUrl": ""
                        }
                        </script>
                    </div>
                </div>

            </div>
        </body>
        </html>
        """
        components.html(market_cards_html, height=530, scrolling=False)


# ==========================================
# PAGE 2 : HUB / WORKSPACE
# ==========================================
elif st.session_state.page == "hub":

    if st.button("← RETOUR AU MENU PRINCIPAL"):
        st.session_state.page = "welcome"
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
        <div class="hud-card">
            <div class="hud-title">🚀 PAGE 2 : HUB DU TERMINAL</div>
            <p style="color:#848e9c; margin-top:8px;">
                Interface prête pour l'intégration des modules de trading de la Page 2.
            </p>
        </div>
    """, unsafe_allow_html=True)
