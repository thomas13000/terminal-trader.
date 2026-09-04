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
# STYLES CSS (Zero Scroll Strict & Hud Compact)
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

        .main .block-container {
            padding: 4px 24px 0px 24px !important;
            max-width: 100vw !important;
            height: 100vh !important;
            overflow: hidden !important;
        }

        /* Viseurs 4 coins */
        .corner-reticle {
            position: fixed; width: 20px; height: 20px; z-index: 99; pointer-events: none;
            border: 2px solid rgba(240, 185, 11, 0.4);
        }
        .corner-tl { top: 6px; left: 6px; border-right: none; border-bottom: none; }
        .corner-tr { top: 6px; right: 6px; border-left: none; border-bottom: none; }
        .corner-bl { bottom: 6px; left: 6px; border-right: none; border-top: none; }
        .corner-br { bottom: 6px; right: 6px; border-left: none; border-top: none; }

        /* Header HUD */
        .hud-header {
            background: rgba(13, 17, 23, 0.90);
            border: 1px solid rgba(240, 185, 11, 0.3);
            border-radius: 10px;
            padding: 8px 16px;
            margin-bottom: 12px;
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
            font-size: 0.75rem;
            color: #848e9c;
        }

        .hud-card {
            background: rgba(13, 17, 23, 0.85);
            border: 1px solid rgba(240, 185, 11, 0.22);
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.6);
        }

        /* Bouton Néon Streamlit */
        div.stButton > button {
            width: 100% !important;
            background: linear-gradient(135deg, #f0b90b 0%, #d4a007 100%) !important;
            color: #080b10 !important;
            font-family: 'Orbitron', sans-serif !important;
            font-size: 0.95rem !important;
            font-weight: 900 !important;
            letter-spacing: 2px !important;
            border-radius: 8px !important;
            padding: 14px 18px !important;
            border: none !important;
            box-shadow: 0 0 18px rgba(240, 185, 11, 0.4) !important;
            cursor: pointer !important;
        }

        div.stButton > button:hover {
            box-shadow: 0 0 25px rgba(240, 185, 11, 0.8), 0 0 10px #00f3ff !important;
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

    # --- BARRE DU HAUT ---
    st.markdown(f"""
        <div class="hud-header">
            <div style="display:flex; align-items:center; gap:12px;">
                <div style="width:30px; height:30px; background:linear-gradient(135deg, #f0b90b, #d4a007); border-radius:6px; display:flex; align-items:center; justify-content:center; font-family:'Orbitron'; font-weight:900; color:#000; font-size:0.95rem;">⚡</div>
                <div>
                    <div class="hud-title" style="font-size:1rem; line-height:1.1;">TERMINAL TRADER <span class="hud-gold">PRO</span></div>
                    <div class="mono-text" style="font-size:0.62rem;">QUANTITATIVE MARKET INTELLIGENCE</div>
                </div>
            </div>
            <div style="display:flex; gap:18px; align-items:center;">
                <div class="mono-text" style="background:rgba(255,255,255,0.05); padding:3px 8px; border-radius:6px; border:1px solid rgba(255,255,255,0.1);">
                    MS SERVEUR : <span style="color:#00f3ff; font-weight:700;">{latency_ms} ms</span>
                </div>
                <div class="mono-text" style="color:#00f3ff; font-weight:700;">{time_utc} UTC</div>
                <div class="mono-text hud-green" style="background:rgba(14,203,129,0.1); padding:3px 8px; border-radius:20px; border:1px solid rgba(14,203,129,0.3); display:flex; align-items:center; gap:5px;">
                    <span style="width:6px; height:6px; background:#0ecb81; border-radius:50%; display:inline-block; box-shadow:0 0 6px #0ecb81;"></span>
                    ONLINE
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # --- DISPOSITION EN 2 COLONNES (Largeur restreinte à droite) ---
    col_left, col_right = st.columns([2.2, 1.0], gap="medium")

    with col_left:
        st.markdown("""
            <div class="hud-card">
                <div class="mono-text hud-gold" style="background:rgba(240,185,11,0.1); padding:3px 10px; border-radius:15px; width:fit-content; border:1px solid rgba(240,185,11,0.3); margin-bottom:10px;">
                    ● NŒUD SYSTÈME : ACTIF
                </div>
                <div class="hud-title" style="font-size:1.3rem; margin-bottom:8px;">
                    PORTAIL DE DÉCISION QUANTITATIVE
                </div>
                <div style="color:#848e9c; font-size:0.85rem; line-height:1.4; margin-bottom:20px;">
                    Initialisez le terminal pour accéder au moteur d'analyse, aux modèles de corrélation et aux outils d'exécution en temps réel.
                </div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("ENTRER DANS LE TERMINAL ➔"):
            st.session_state.page = "hub"
            st.rerun()

    with col_right:
        # Cadre compact ultra-réduit sans courbes
        market_quotes_html = """
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

                .compact-container {
                    background: rgba(13, 17, 23, 0.95);
                    border: 1.5px solid #f0b90b;
                    border-radius: 10px;
                    padding: 8px;
                    box-shadow: 0 0 15px rgba(240, 185, 11, 0.2);
                    display: flex;
                    flex-direction: column;
                    gap: 4px;
                }

                .container-header {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding-bottom: 4px;
                    margin-bottom: 2px;
                    border-bottom: 1px solid rgba(240, 185, 11, 0.2);
                }

                .title-text {
                    font-family: 'Orbitron', sans-serif;
                    font-weight: 900;
                    font-size: 0.72rem;
                    color: #f0b90b;
                    letter-spacing: 1px;
                }

                .pulse-tag {
                    display: flex;
                    align-items: center;
                    gap: 4px;
                    font-family: 'JetBrains Mono', monospace;
                    font-size: 0.58rem;
                    font-weight: 700;
                    color: #0ecb81;
                }

                .pulse-dot {
                    width: 5px;
                    height: 5px;
                    background-color: #0ecb81;
                    border-radius: 50%;
                    box-shadow: 0 0 5px #0ecb81;
                }

                .quote-row {
                    background: rgba(22, 27, 34, 0.7);
                    border: 1px solid rgba(240, 185, 11, 0.15);
                    border-radius: 6px;
                    height: 48px;
                    overflow: hidden;
                }
            </style>
        </head>
        <body>
            <div class="compact-container">
                <div class="container-header">
                    <span class="title-text">⚡ PRIX EN DIRECT</span>
                    <div class="pulse-tag">
                        <span class="pulse-dot"></span>
                        <span>LIVE</span>
                    </div>
                </div>

                <!-- 1. NASDAQ -->
                <div class="quote-row">
                    <div class="tradingview-widget-container">
                        <div class="tradingview-widget-container__widget"></div>
                        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
                        {
                          "symbol": "FOREXCOM:NSXUSD",
                          "width": "100%",
                          "colorTheme": "dark",
                          "isTransparent": true,
                          "locale": "fr"
                        }
                        </script>
                    </div>
                </div>

                <!-- 2. DXY -->
                <div class="quote-row">
                    <div class="tradingview-widget-container">
                        <div class="tradingview-widget-container__widget"></div>
                        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
                        {
                          "symbol": "CAPITALCOM:DXY",
                          "width": "100%",
                          "colorTheme": "dark",
                          "isTransparent": true,
                          "locale": "fr"
                        }
                        </script>
                    </div>
                </div>

                <!-- 3. EUR / USD -->
                <div class="quote-row">
                    <div class="tradingview-widget-container">
                        <div class="tradingview-widget-container__widget"></div>
                        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
                        {
                          "symbol": "FX:EURUSD",
                          "width": "100%",
                          "colorTheme": "dark",
                          "isTransparent": true,
                          "locale": "fr"
                        }
                        </script>
                    </div>
                </div>

                <!-- 4. GOLD -->
                <div class="quote-row">
                    <div class="tradingview-widget-container">
                        <div class="tradingview-widget-container__widget"></div>
                        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
                        {
                          "symbol": "OANDA:XAUUSD",
                          "width": "100%",
                          "colorTheme": "dark",
                          "isTransparent": true,
                          "locale": "fr"
                        }
                        </script>
                    </div>
                </div>

            </div>
        </body>
        </html>
        """
        components.html(market_quotes_html, height=250, scrolling=False)


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
