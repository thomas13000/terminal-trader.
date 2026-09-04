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
# STYLES CSS (VERROUILLAGE SCROLL + GLOBE VIF)
# ==========================================
st.markdown("""
    <style>
        /* Masquage des éléments Streamlit natifs */
        header[data-testid="stHeader"], footer, [data-testid="stToolbar"] {
            display: none !important;
            visibility: hidden !important;
        }

        /* VERROUILLAGE STRICT DU DÉFILEMENT SUR TOUTE LA PAGE */
        html, body, .stApp, [data-testid="stAppViewContainer"], .main, [data-testid="stVerticalBlock"] {
            height: 100vh !important;
            max-height: 100vh !important;
            overflow: hidden !important;
            margin: 0 !important;
            padding: 0 !important;
            background-color: #080b10 !important;
            color: #eaecef !important;
            font-family: 'Inter', sans-serif !important;
        }

        /* Conteneur principal fixe */
        .main .block-container {
            padding: 8px 20px 0px 20px !important;
            max-width: 100vw !important;
            height: 100vh !important;
            max-height: 100vh !important;
            overflow: hidden !important;
            position: relative;
            z-index: 2;
        }

        /* Viseurs aux 4 coins */
        .corner-reticle {
            position: fixed; width: 22px; height: 22px; z-index: 99; pointer-events: none;
            border: 2px solid rgba(240, 185, 11, 0.6);
        }
        .corner-tl { top: 6px; left: 6px; border-right: none; border-bottom: none; }
        .corner-tr { top: 6px; right: 6px; border-left: none; border-bottom: none; }
        .corner-bl { bottom: 6px; left: 6px; border-right: none; border-top: none; }
        .corner-br { bottom: 6px; right: 6px; border-left: none; border-top: none; }

        /* Header HUD */
        .hud-header {
            background: rgba(13, 17, 23, 0.94);
            border: 1.5px solid rgba(240, 185, 11, 0.45);
            border-radius: 12px;
            padding: 10px 20px;
            margin-top: 0px;
            margin-bottom: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            backdrop-filter: blur(20px);
            box-shadow: 0 6px 25px rgba(0, 0, 0, 0.8), 0 0 15px rgba(240, 185, 11, 0.2);
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
            font-size: 0.8rem;
            color: #848e9c;
        }

        .hud-card {
            background: rgba(13, 17, 23, 0.88);
            border: 1px solid rgba(240, 185, 11, 0.25);
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
            font-size: 0.88rem !important;
            font-weight: 900 !important;
            letter-spacing: 1.5px !important;
            border-radius: 8px !important;
            padding: 10px 14px !important;
            border: none !important;
            box-shadow: 0 0 20px rgba(240, 185, 11, 0.4) !important;
            cursor: pointer !important;
            transition: all 0.2s ease-in-out !important;
        }

        div.stButton > button:hover {
            box-shadow: 0 0 30px rgba(240, 185, 11, 0.9), 0 0 15px #00f3ff !important;
            color: #000000 !important;
        }

        /* GLOBE 3D EN FOND DE PAGE */
        .bg-globe-wrapper {
            position: fixed;
            top: 50%;
            left: 50%;
            width: 600px;
            height: 600px;
            margin-top: -300px;
            margin-left: -300px;
            z-index: 0;
            pointer-events: none;
            opacity: 0.38;
            perspective: 1000px;
        }

        .bg-globe-sphere {
            width: 100%;
            height: 100%;
            position: relative;
            transform-style: preserve-3d;
            animation: spinGlobeBg 20s linear infinite;
        }

        .bg-globe-ring {
            position: absolute;
            top: 0; left: 0;
            width: 100%;
            height: 100%;
            border-radius: 50%;
            border: 2px solid #f0b90b;
            box-shadow: 0 0 15px rgba(240, 185, 11, 0.6);
        }

        @keyframes spinGlobeBg {
            0% { transform: rotateX(20deg) rotateY(0deg); }
            100% { transform: rotateX(20deg) rotateY(360deg); }
        }
    </style>

    <!-- Globe background -->
    <div class="bg-globe-wrapper">
        <div class="bg-globe-sphere">
            <div class="bg-globe-ring" style="transform: rotateY(0deg);"></div>
            <div class="bg-globe-ring" style="transform: rotateY(30deg);"></div>
            <div class="bg-globe-ring" style="transform: rotateY(60deg);"></div>
            <div class="bg-globe-ring" style="transform: rotateY(90deg);"></div>
            <div class="bg-globe-ring" style="transform: rotateY(120deg);"></div>
            <div class="bg-globe-ring" style="transform: rotateY(150deg);"></div>
            <div class="bg-globe-ring" style="transform: rotateX(30deg);"></div>
            <div class="bg-globe-ring" style="transform: rotateX(60deg);"></div>
            <div class="bg-globe-ring" style="transform: rotateX(90deg);"></div>
            <div class="bg-globe-ring" style="transform: rotateX(120deg);"></div>
            <div class="bg-globe-ring" style="transform: rotateX(150deg);"></div>
        </div>
    </div>

    <!-- Viseurs -->
    <div class="corner-reticle corner-tl"></div>
    <div class="corner-reticle corner-tr"></div>
    <div class="corner-reticle corner-bl"></div>
    <div class="corner-reticle corner-br"></div>
""", unsafe_allow_html=True)


# ==========================================
# PAGE 1 : WELCOME SCREEN (ACCUEIL)
# ==========================================
if st.session_state.page == "welcome":

    now = datetime.utcnow()
    time_utc = now.strftime("%H:%M:%S")

    st.markdown(f"""
        <div class="hud-header">
            <div style="display:flex; align-items:center; gap:16px;">
                <div style="width:36px; height:36px; background:linear-gradient(135deg, #f0b90b, #d4a007); border-radius:8px; display:flex; align-items:center; justify-content:center; font-family:'Orbitron'; font-weight:900; color:#000; font-size:1.1rem; box-shadow:0 0 12px rgba(240,185,11,0.6);">⚡</div>
                <div>
                    <div class="hud-title" style="font-size:1.15rem; line-height:1.1;">TERMINAL TRADER <span class="hud-gold">PRO</span></div>
                    <div class="mono-text" style="font-size:0.68rem; letter-spacing:1px; color:#848e9c;">QUANTITATIVE MARKET INTELLIGENCE PLATFORM</div>
                </div>
            </div>
            <div style="display:flex; gap:20px; align-items:center;">
                <div class="mono-text" style="background:rgba(255,255,255,0.05); padding:5px 12px; border-radius:6px; border:1px solid rgba(255,255,255,0.1);">
                    MS SERVEUR : <span style="color:#00f3ff; font-weight:700;">{latency_ms} ms</span>
                </div>
                <div class="mono-text" style="color:#00f3ff; font-weight:700; font-size:0.85rem;">{time_utc} UTC</div>
                <div class="mono-text hud-green" style="background:rgba(14,203,129,0.12); padding:5px 12px; border-radius:20px; border:1px solid rgba(14,203,129,0.3); display:flex; align-items:center; gap:6px; font-weight:700;">
                    <span style="width:7px; height:7px; background:#0ecb81; border-radius:50%; display:inline-block; box-shadow:0 0 8px #0ecb81;"></span>
                    SYSTEM ONLINE
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    col_left, col_right = st.columns([1.4, 1.0], gap="medium")

    with col_left:
        clock_html = """
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
                    padding: 14px 20px;
                    display: flex;
                    flex-direction: column;
                    gap: 10px;
                    box-shadow: 0 0 20px rgba(240, 185, 11, 0.25);
                    max-width: 320px;
                }

                .clock-row {
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                }

                .city-badge {
                    font-family: 'Orbitron', sans-serif;
                    font-size: 0.75rem;
                    font-weight: 900;
                    color: #f0b90b;
                    letter-spacing: 1.2px;
                }

                .time-val {
                    font-size: 1.45rem;
                    font-weight: 800;
                    color: #ffffff;
                    letter-spacing: 1.5px;
                    text-shadow: 0 0 10px rgba(255, 255, 255, 0.4);
                }

                .time-sub {
                    font-size: 0.6rem;
                    color: #848e9c;
                }

                .horizontal-divider {
                    width: 100%;
                    height: 1px;
                    background: rgba(240, 185, 11, 0.25);
                }
            </style>
        </head>
        <body>
            <div class="hud-clock-card">
                <div class="clock-row">
                    <div class="city-badge">🇫🇷 PARIS</div>
                    <div>
                        <span class="time-val" id="paris-time">--:--:--</span>
                        <span class="time-sub">CET</span>
                    </div>
                </div>

                <div class="horizontal-divider"></div>

                <div class="clock-row">
                    <div class="city-badge">🇺🇸 NEW YORK</div>
                    <div>
                        <span class="time-val" id="ny-time">--:--:--</span>
                        <span class="time-sub">EST</span>
                    </div>
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
        components.html(clock_html, height=125, scrolling=False)

        st.markdown("<div style='height: 190px;'></div>", unsafe_allow_html=True)

        if st.button("ENTRER DANS LE TERMINAL ➔"):
            st.session_state.page = "hub"
            st.rerun()

    with col_right:
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
                    gap: 10px;
                    height: 480px;
                }

                .container-header {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding-bottom: 6px;
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
                    height: 95px;
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

                <div class="quote-row">
                    <div class="tradingview-widget-container">
                        <div class="tradingview-widget-container__widget"></div>
                        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
                        {
                          "symbol": "FOREXCOM:NAS100",
                          "width": "100%",
                          "colorTheme": "dark",
                          "isTransparent": true,
                          "locale": "fr"
                        }
                        </script>
                    </div>
                </div>

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

                <div class="quote-row">
                    <div class="tradingview-widget-container">
                        <div class="tradingview-widget-container__widget"></div>
                        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
                        {
                          "symbol": "FOREXCOM:EURUSD",
                          "width": "100%",
                          "colorTheme": "dark",
                          "isTransparent": true,
                          "locale": "fr"
                        }
                        </script>
                    </div>
                </div>

                <div class="quote-row">
                    <div class="tradingview-widget-container">
                        <div class="tradingview-widget-container__widget"></div>
                        <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
                        {
                          "symbol": "FOREXCOM:XAUUSD",
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
        components.html(market_quotes_html, height=490, scrolling=False)


# ==========================================
# PAGE 2 : HUB / WORKSPACE (PAGE SECONDAIRE)
# ==========================================
elif st.session_state.page == "hub":

    # BARRE SUPÉRIEURE INTEGREE AVEC LE BOUTON ACCUEIL DANS LA BARRE
    col_hdr, col_btn = st.columns([8.2, 1.8])

    with col_hdr:
        page2_header_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@700;800&family=Orbitron:wght@800;900&family=Inter:wght@600;700&display=swap');
                
                * { box-sizing: border-box; }
                body { margin: 0; padding: 0; background: transparent; font-family: 'JetBrains Mono', monospace; }

                .hud-header-p2 {
                    background: rgba(13, 17, 23, 0.94);
                    border: 1.5px solid rgba(240, 185, 11, 0.45);
                    border-radius: 12px;
                    padding: 8px 16px;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    box-shadow: 0 6px 25px rgba(0, 0, 0, 0.8), 0 0 15px rgba(240, 185, 11, 0.2);
                }

                .left-brand {
                    display: flex;
                    align-items: center;
                    gap: 12px;
                }

                .logo-icon {
                    width: 32px;
                    height: 32px;
                    background: linear-gradient(135deg, #f0b90b, #d4a007);
                    border-radius: 8px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-family: 'Orbitron', sans-serif;
                    font-weight: 900;
                    color: #000;
                    font-size: 1rem;
                    box-shadow: 0 0 12px rgba(240,185,11,0.6);
                }

                .title-p2 {
                    font-family: 'Orbitron', sans-serif;
                    font-weight: 900;
                    color: #ffffff;
                    font-size: 1rem;
                    letter-spacing: 1.5px;
                    line-height: 1.1;
                }

                .hud-gold { color: #f0b90b; }

                .subtitle-p2 {
                    font-size: 0.6rem;
                    color: #848e9c;
                    letter-spacing: 1px;
                }

                .header-clocks-container {
                    display: flex;
                    align-items: center;
                    gap: 16px;
                    background: rgba(255, 255, 255, 0.03);
                    border: 1px solid rgba(240, 185, 11, 0.25);
                    padding: 5px 14px;
                    border-radius: 8px;
                }

                .clock-item {
                    display: flex;
                    align-items: center;
                    gap: 6px;
                }

                .clock-flag {
                    font-family: 'Orbitron', sans-serif;
                    font-size: 0.68rem;
                    font-weight: 900;
                    color: #f0b90b;
                }

                .clock-time {
                    font-size: 1.05rem;
                    font-weight: 800;
                    color: #ffffff;
                    letter-spacing: 1px;
                    text-shadow: 0 0 8px rgba(255, 255, 255, 0.3);
                }

                .clock-divider {
                    width: 1px;
                    height: 20px;
                    background: rgba(240, 185, 11, 0.3);
                }

                .right-status {
                    display: flex;
                    align-items: center;
                    gap: 12px;
                }

                .status-badge {
                    background: rgba(255,255,255,0.05);
                    padding: 4px 10px;
                    border-radius: 6px;
                    border: 1px solid rgba(255,255,255,0.1);
                    font-size: 0.72rem;
                    color: #848e9c;
                }

                .online-badge {
                    background: rgba(14,203,129,0.12);
                    padding: 4px 10px;
                    border-radius: 20px;
                    border: 1px solid rgba(14,203,129,0.3);
                    display: flex;
                    align-items: center;
                    gap: 6px;
                    font-weight: 700;
                    color: #0ecb81;
                    font-size: 0.72rem;
                }

                .online-dot {
                    width: 6px;
                    height: 6px;
                    background: #0ecb81;
                    border-radius: 50%;
                    box-shadow: 0 0 8px #0ecb81;
                }
            </style>
        </head>
        <body>
            <div class="hud-header-p2">
                <div class="left-brand">
                    <div class="logo-icon">⚡</div>
                    <div>
                        <div class="title-p2">TERMINAL TRADER <span class="hud-gold">PRO</span></div>
                        <div class="subtitle-p2">QUANTITATIVE WORKSPACE</div>
                    </div>
                </div>

                <div class="header-clocks-container">
                    <div class="clock-item">
                        <span class="clock-flag">🇫🇷 PARIS</span>
                        <span class="clock-time" id="p2-paris">--:--:--</span>
                    </div>

                    <div class="clock-divider"></div>

                    <div class="clock-item">
                        <span class="clock-flag">🇺🇸 NEW YORK</span>
                        <span class="clock-time" id="p2-ny">--:--:--</span>
                    </div>
                </div>

                <div class="right-status">
                    <div class="status-badge">
                        MS : <span style="color:#00f3ff; font-weight:700;">__LATENCY__ ms</span>
                    </div>
                    <div class="online-badge">
                        <span class="online-dot"></span>
                        ONLINE
                    </div>
                </div>
            </div>

            <script>
                function updateP2Clocks() {
                    const now = new Date();
                    const parisStr = now.toLocaleTimeString('fr-FR', { timeZone: 'Europe/Paris', hour: '2-digit', minute: '2-digit', second: '2-digit' });
                    const nyStr = now.toLocaleTimeString('en-US', { timeZone: 'America/New_York', hour12: false, hour: '2-digit', minute: '2-digit', second: '2-digit' });
                    
                    document.getElementById('p2-paris').innerText = parisStr;
                    document.getElementById('p2-ny').innerText = nyStr;
                }
                setInterval(updateP2Clocks, 1000);
                updateP2Clocks();
            </script>
        </body>
        </html>
        """.replace("__LATENCY__", str(latency_ms))

        components.html(page2_header_html, height=60, scrolling=False)

    with col_btn:
        st.markdown("<div style='margin-top:2px;'></div>", unsafe_allow_html=True)
        if st.button("← ACCUEIL"):
            st.session_state.page = "welcome"
            st.rerun()

    st.markdown("""
        <div class="hud-card" style="margin-top:10px;">
            <div class="hud-title" style="font-size:1.1rem; color:#f0b90b;">
                🚀 WORKSPACE EN DÉVELOPPEMENT
            </div>
            <p style="color:#848e9c; margin-top:8px; font-size:0.85rem;">
                Le bouton d'accueil est désormais intégré sur la même ligne que la barre de statut.
            </p>
        </div>
    """, unsafe_allow_html=True)
