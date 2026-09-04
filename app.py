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
# STYLES CSS (Zéro Scroll & Alignement Haut Max)
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

        /* Remontée maximale du conteneur haut */
        .main .block-container {
            padding: 2px 20px 0px 20px !important;
            max-width: 100vw !important;
            height: 100vh !important;
            overflow: hidden !important;
        }

        /* Viseurs 4 coins */
        .corner-reticle {
            position: fixed; width: 20px; height: 20px; z-index: 99; pointer-events: none;
            border: 2px solid rgba(240, 185, 11, 0.4);
        }
        .corner-tl { top: 4px; left: 4px; border-right: none; border-bottom: none; }
        .corner-tr { top: 4px; right: 4px; border-left: none; border-bottom: none; }
        .corner-bl { bottom: 4px; left: 4px; border-right: none; border-top: none; }
        .corner-br { bottom: 4px; right: 4px; border-left: none; border-top: none; }

        /* Header HUD */
        .hud-header {
            background: rgba(13, 17, 23, 0.90);
            border: 1px solid rgba(240, 185, 11, 0.3);
            border-radius: 10px;
            padding: 6px 16px;
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
            font-size: 0.75rem;
            color: #848e9c;
        }

        .hud-card {
            background: rgba(13, 17, 23, 0.85);
            border: 1px solid rgba(240, 185, 11, 0.22);
            border-radius: 12px;
            padding: 18px;
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
            border-radius: 8px !important;
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

    # --- BARRE DU HAUT COLLÉE EN HAUT ---
    st.markdown(f"""
        <div class="hud-header">
            <div style="display:flex; align-items:center; gap:12px;">
                <div style="width:28px; height:28px; background:linear-gradient(135deg, #f0b90b, #d4a007); border-radius:6px; display:flex; align-items:center; justify-content:center; font-family:'Orbitron'; font-weight:900; color:#000; font-size:0.9rem;">⚡</div>
                <div>
                    <div class="hud-title" style="font-size:0.95rem; line-height:1.1;">TERMINAL TRADER <span class="hud-gold">PRO</span></div>
                    <div class="mono-text" style="font-size:0.6rem;">QUANTITATIVE MARKET INTELLIGENCE</div>
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

    # --- DISPOSITION EN 2 COLONNES ---
    col_left, col_right = st.columns([1.5, 1.5], gap="medium")

    with col_left:
        # Cadre Horloges Superposées (Heures en Blanc) + Globe Or
        clock_globe_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@700;800&family=Orbitron:wght@800;900&display=swap');
                body { margin: 0; padding: 0; background: transparent; font-family: 'JetBrains Mono', monospace; }
                
                .hud-clock-card {
                    background: rgba(13, 17, 23, 0.90);
                    border: 1.5px solid #f0b90b;
                    border-radius: 12px;
                    padding: 16px 22px;
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    box-shadow: 0 0 20px rgba(240, 185, 11, 0.2);
                }

                .clocks-container {
                    display: flex;
                    flex-direction: column;
                    gap: 16px;
                }

                .clock-row {
                    display: flex;
                    align-items: center;
                    gap: 16px;
                }

                .city-badge {
                    font-family: 'Orbitron', sans-serif;
                    font-size: 0.75rem;
                    font-weight: 900;
                    color: #f0b90b;
                    letter-spacing: 1.5px;
                    width: 110px;
                }

                /* HEURES EN BLANC PUR */
                .time-val {
                    font-size: 1.5rem;
                    font-weight: 800;
                    color: #ffffff;
                    letter-spacing: 1.5px;
                    text-shadow: 0 0 10px rgba(255, 255, 255, 0.4);
                }

                .time-sub {
                    font-size: 0.6rem;
                    color: #848e9c;
                    margin-left: 8px;
                }

                .horizontal-divider {
                    width: 100%;
                    height: 1px;
                    background: rgba(240, 185, 11, 0.25);
                }

                /* GLOBE OR ANIME EN CSS */
                .globe-wrapper {
                    position: relative;
                    width: 100px;
                    height: 100px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }

                .globe-svg {
                    width: 90px;
                    height: 90px;
                    animation: spinGlobe 14s linear infinite;
                    filter: drop-shadow(0 0 8px rgba(240, 185, 11, 0.5));
                }

                @keyframes spinGlobe {
                    0% { transform: rotate(0deg); }
                    100% { transform: rotate(360deg); }
                }
            </style>
        </head>
        <body>
            <div class="hud-clock-card">
                <div class="clocks-container">
                    <!-- 1. PARIS -->
                    <div class="clock-row">
                        <div class="city-badge">🇫🇷 PARIS</div>
                        <div class="time-val" id="paris-time">--:--:--</div>
                        <div class="time-sub">CET</div>
                    </div>

                    <div class="horizontal-divider"></div>

                    <!-- 2. NEW YORK -->
                    <div class="clock-row">
                        <div class="city-badge">🇺🇸 NEW YORK</div>
                        <div class="time-val" id="ny-time">--:--:--</div>
                        <div class="time-sub">EST</div>
                    </div>
                </div>

                <!-- GLOBE ANIME OR (#f0b90b) -->
                <div class="globe-wrapper">
                    <svg class="globe-svg" viewBox="0 0 100 100">
                        <circle cx="50" cy="50" r="44" fill="none" stroke="#f0b90b" stroke-width="1.8" opacity="0.95"/>
                        <ellipse cx="50" cy="50" rx="44" ry="16" fill="none" stroke="#f0b90b" stroke-width="1.2" opacity="0.75"/>
                        <ellipse cx="50" cy="50" rx="16" ry="44" fill="none" stroke="#f0b90b" stroke-width="1.2" opacity="0.75"/>
                        <line x1="6" y1="50" x2="94" y2="50" stroke="#f0b90b" stroke-width="1" opacity="0.6"/>
                        <line x1="50" y1="6" x2="50" y2="94" stroke="#f0b90b" stroke-width="1" opacity="0.6"/>
                        <circle cx="50" cy="50" r="3" fill="#f0b90b"/>
                    </svg>
                </div>
            </div>

            <script>
                function updateClocks() {
                    const now = new Date();
                    const parisStr = now.toLocaleTimeString('fr-FR', { timeZone: 'Europe/Paris', hour: '2-digit', minute: '2-digit', second: '2-digit' });
                    const nyStr = now.toLocaleTimeString('en-US', { timeZone: 'America/New_York', hour12: false, hour: '2-digit', minute: '2-digit', second: '2-digit' });
                    
                    document.getElementById('paris-time').innerText = parisStr;
                    document.getElementById('ny-time').innerText = nyStr;
                }
                setInterval(updateClocks, 1000);
                updateClocks();
            </script>
        </body>
        </html>
        """
        components.html(clock_globe_html, height=130, scrolling=False)

        # Espace vertical pour abaisser le bouton Entrer
        st.markdown("<div style='height: 220px;'></div>", unsafe_allow_html=True)

        if st.button("ENTRER DANS LE TERMINAL ➔"):
            st.session_state.page = "hub"
            st.rerun()

    with col_right:
        # Cadre marchés encore plus allongé (Hauteur 520px)
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
                    border-radius: 12px;
                    padding: 12px;
                    box-shadow: 0 0 25px rgba(240, 185, 11, 0.25);
                    display: flex;
                    flex-direction: column;
                    gap: 12px;
                    height: 500px;
                }

                .container-header {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding-bottom: 8px;
                    border-bottom: 1px solid rgba(240, 185, 11, 0.3);
                }

                .title-text {
                    font-family: 'Orbitron', sans-serif;
                    font-weight: 900;
                    font-size: 0.8rem;
                    color: #f0b90b;
                    letter-spacing: 1.2px;
                }

                .pulse-tag {
                    display: flex;
                    align-items: center;
                    gap: 6px;
                    font-family: 'JetBrains Mono', monospace;
                    font-size: 0.65rem;
                    font-weight: 700;
                    color: #0ecb81;
                }

                .pulse-dot {
                    width: 7px;
                    height: 7px;
                    background-color: #0ecb81;
                    border-radius: 50%;
                    box-shadow: 0 0 8px #0ecb81;
                }

                .quote-row {
                    background: rgba(22, 27, 34, 0.85);
                    border: 1px solid rgba(240, 185, 11, 0.22);
                    border-radius: 8px;
                    height: 98px;
                    overflow: hidden;
                }
            </style>
        </head>
        <body>
            <div class="compact-container">
                <div class="container-header">
                    <span class="title-text">⚡ MARCHÉS EN DIRECT</span>
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
                          "symbol": "NASDAQ:NDX",
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
                          "symbol": "TVC:DXY",
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
        components.html(market_quotes_html, height=520, scrolling=False)


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
