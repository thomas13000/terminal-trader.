import streamlit as st
import streamlit.components.v1 as components
import time
from datetime import datetime

# ==========================================
# 1. CONFIGURATION DE LA PAGE
# ==========================================
st.set_page_config(
    page_title="TERMINAL TRADER PRO",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# 2. GESTION DE LA NAVIGATION (SESSION STATE)
# ==========================================
if "page" not in st.session_state:
    st.session_state.page = "welcome"

start_time = time.time()
latency_ms = round((time.time() - start_time) * 1000 + 12, 1)

# ==========================================
# 3. CSS GLOBAL (THEME TRADER HUD)
# ==========================================
st.markdown("""
    <style>
        /* Masquer l'en-tête et le pied de page Streamlit */
        header[data-testid="stHeader"], footer, [data-testid="stToolbar"] {
            display: none !important;
            visibility: hidden !important;
        }

        /* Style global du fond */
        html, body, .stApp, [data-testid="stAppViewContainer"], .main {
            background-color: #080b10 !important;
            color: #eaecef !important;
            font-family: 'Inter', sans-serif !important;
        }

        .main .block-container {
            padding: 15px 25px 10px 25px !important;
            max-width: 100vw !important;
        }

        /* Viseurs HUD aux coins */
        .corner-reticle {
            position: fixed; width: 20px; height: 20px; z-index: 99; pointer-events: none;
            border: 2px solid rgba(240, 185, 11, 0.5);
        }
        .corner-tl { top: 8px; left: 8px; border-right: none; border-bottom: none; }
        .corner-tr { top: 8px; right: 8px; border-left: none; border-bottom: none; }
        .corner-bl { bottom: 8px; left: 8px; border-right: none; border-top: none; }
        .corner-br { bottom: 8px; right: 8px; border-left: none; border-top: none; }

        /* Style des Cartes HUD */
        .hud-card {
            background: rgba(13, 17, 23, 0.90);
            border: 1px solid rgba(240, 185, 11, 0.3);
            border-radius: 12px;
            padding: 18px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.6);
        }

        /* BOUTON PRINCIPAL EN NÉON DORE */
        div.stButton > button {
            width: 100% !important;
            height: 48px !important;
            background: linear-gradient(135deg, #f0b90b 0%, #d4a007 100%) !important;
            color: #080b10 !important;
            font-family: 'Orbitron', sans-serif !important;
            font-size: 0.88rem !important;
            font-weight: 900 !important;
            letter-spacing: 1.5px !important;
            border-radius: 8px !important;
            border: none !important;
            box-shadow: 0 0 18px rgba(240, 185, 11, 0.4) !important;
            cursor: pointer !important;
            transition: all 0.2s ease-in-out !important;
        }

        div.stButton > button:hover {
            box-shadow: 0 0 28px rgba(240, 185, 11, 0.8), 0 0 12px #00f3ff !important;
            color: #000000 !important;
            transform: translateY(-1px);
        }
    </style>

    <!-- Viseurs de bordure -->
    <div class="corner-reticle corner-tl"></div>
    <div class="corner-reticle corner-tr"></div>
    <div class="corner-reticle corner-bl"></div>
    <div class="corner-reticle corner-br"></div>
""", unsafe_allow_html=True)


# ==========================================
# PAGE 1 : ACCUEIL (WELCOME SCREEN)
# ==========================================
if st.session_state.page == "welcome":

    # En-tête HUD avec statut serveur
    now_utc = datetime.utcnow().strftime("%H:%M:%S")
    
    st.markdown(f"""
        <div style="background: rgba(13, 17, 23, 0.94); border: 1.5px solid rgba(240, 185, 11, 0.45); border-radius: 12px; padding: 10px 20px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center;">
            <div style="display:flex; align-items:center; gap:12px;">
                <div style="width:34px; height:34px; background:linear-gradient(135deg, #f0b90b, #d4a007); border-radius:8px; display:flex; align-items:center; justify-content:center; font-family:'Orbitron'; font-weight:900; color:#000; font-size:1.1rem; box-shadow:0 0 12px rgba(240,185,11,0.6);">⚡</div>
                <div>
                    <div style="font-family:'Orbitron', sans-serif; font-weight:900; color:#ffffff; font-size:1.1rem; letter-spacing:1px;">TERMINAL TRADER <span style="color:#f0b90b;">PRO</span></div>
                    <div style="font-family:'JetBrains Mono', monospace; font-size:0.65rem; color:#848e9c; letter-spacing:0.8px;">QUANTITATIVE MARKET INTELLIGENCE PLATFORM</div>
                </div>
            </div>
            <div style="display:flex; gap:16px; align-items:center; font-family:'JetBrains Mono', monospace; font-size:0.8rem;">
                <div style="background:rgba(255,255,255,0.05); padding:5px 12px; border-radius:6px; border:1px solid rgba(255,255,255,0.1); color:#848e9c;">
                    MS SERVEUR : <span style="color:#ffffff; font-weight:700;">{latency_ms} ms</span>
                </div>
                <div style="color:#00f3ff; font-weight:700;">{now_utc} UTC</div>
                <div style="background:rgba(14,203,129,0.12); color:#0ecb81; padding:5px 12px; border-radius:20px; border:1px solid rgba(14,203,129,0.3); font-weight:700;">
                    ● SYSTEM ONLINE
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    col_left, col_right = st.columns([1.2, 1.0], gap="medium")

    with col_left:
        # Horloges Paris & New York
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
                    padding: 14px 18px;
                    display: flex; flex-direction: column; gap: 10px;
                    box-shadow: 0 0 20px rgba(240, 185, 11, 0.25);
                    max-width: 320px;
                }
                .clock-row { display: flex; align-items: center; justify-content: space-between; }
                .city-badge { font-family: 'Orbitron', sans-serif; font-size: 0.72rem; font-weight: 900; color: #f0b90b; letter-spacing: 1.2px; }
                .time-val { font-size: 1.3rem; font-weight: 800; color: #ffffff; letter-spacing: 1.5px; }
                .time-sub { font-size: 0.6rem; color: #848e9c; }
                .divider { width: 100%; height: 1px; background: rgba(240, 185, 11, 0.25); }
            </style>
        </head>
        <body>
            <div class="hud-clock-card">
                <div class="clock-row">
                    <div class="city-badge">🇫🇷 PARIS</div>
                    <div><span class="time-val" id="p-time">--:--:--</span> <span class="time-sub">CET</span></div>
                </div>
                <div class="divider"></div>
                <div class="clock-row">
                    <div class="city-badge">🇺🇸 NEW YORK</div>
                    <div><span class="time-val" id="ny-time">--:--:--</span> <span class="time-sub">EST</span></div>
                </div>
            </div>
            <script>
                function updateClocks() {
                    const now = new Date();
                    document.getElementById('p-time').innerText = now.toLocaleTimeString('fr-FR', { timeZone: 'Europe/Paris', hour: '2-digit', minute: '2-digit', second: '2-digit' });
                    document.getElementById('ny-time').innerText = now.toLocaleTimeString('en-US', { timeZone: 'America/New_York', hour12: false, hour: '2-digit', minute: '2-digit', second: '2-digit' });
                }
                setInterval(updateClocks, 1000);
                updateClocks();
            </script>
        </body>
        </html>
        """
        components.html(clock_html, height=120, scrolling=False)

        st.markdown("""
            <div class="hud-card" style="margin-top: 15px; margin-bottom: 20px;">
                <div style="font-family:'Orbitron', sans-serif; font-size:0.95rem; font-weight:800; color:#f0b90b; letter-spacing:1px;">
                    ⚡ ACCÈS SYSTÈME AUTORISÉ
                </div>
                <div style="color:#848e9c; font-size:0.82rem; margin-top:8px; line-height:1.4;">
                    Bienvenue dans l'interface quantitative. Flux de marché synchronisés en temps réel via passerelle ultra-basse latence.
                </div>
            </div>
        """, unsafe_allow_html=True)

        if st.button("ENTRER DANS LE TERMINAL ➔"):
            st.session_state.page = "hub"
            st.rerun()

    with col_right:
        # Widget TradingView Live Quotes
        market_quotes_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&display=swap');
                * { box-sizing: border-box; }
                body { margin: 0; padding: 0; background: transparent; }
                .compact-container {
                    background: rgba(13, 17, 23, 0.95);
                    border: 1.5px solid #f0b90b;
                    border-radius: 12px;
                    padding: 10px;
                    display: flex; flex-direction: column; gap: 8px;
                    height: 430px;
                }
                .container-header {
                    display: flex; justify-content: space-between; align-items: center;
                    padding-bottom: 6px; border-bottom: 1px solid rgba(240, 185, 11, 0.3);
                    font-family: 'Orbitron', sans-serif; font-size: 0.75rem; color: #f0b90b; font-weight: 900;
                }
                .quote-row {
                    background: rgba(22, 27, 34, 0.85);
                    border: 1px solid rgba(240, 185, 11, 0.2);
                    border-radius: 8px; height: 88px; overflow: hidden;
                }
            </style>
        </head>
        <body>
            <div class="compact-container">
                <div class="container-header">
                    <span>⚡ MARCHÉS EN DIRECT</span>
                    <span style="color:#0ecb81;">● LIVE</span>
                </div>
                <div class="quote-row">
                    <div class="tradingview-widget-container"><div class="tradingview-widget-container__widget"></div>
                    <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
                    {"symbol": "FOREXCOM:NAS100", "width": "100%", "colorTheme": "dark", "isTransparent": true, "locale": "fr"}
                    </script></div>
                </div>
                <div class="quote-row">
                    <div class="tradingview-widget-container"><div class="tradingview-widget-container__widget"></div>
                    <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
                    {"symbol": "CAPITALCOM:DXY", "width": "100%", "colorTheme": "dark", "isTransparent": true, "locale": "fr"}
                    </script></div>
                </div>
                <div class="quote-row">
                    <div class="tradingview-widget-container"><div class="tradingview-widget-container__widget"></div>
                    <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
                    {"symbol": "FOREXCOM:EURUSD", "width": "100%", "colorTheme": "dark", "isTransparent": true, "locale": "fr"}
                    </script></div>
                </div>
                <div class="quote-row">
                    <div class="tradingview-widget-container"><div class="tradingview-widget-container__widget"></div>
                    <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
                    {"symbol": "FOREXCOM:XAUUSD", "width": "100%", "colorTheme": "dark", "isTransparent": true, "locale": "fr"}
                    </script></div>
                </div>
            </div>
        </body>
        </html>
        """
        components.html(market_quotes_html, height=440, scrolling=False)


# ==========================================
# PAGE 2 : TERMINAL / HUB DE WORKSPACE
# ==========================================
elif st.session_state.page == "hub":

    col_title, col_btn = st.columns([4, 1], gap="medium")

    with col_title:
        st.markdown(f"""
            <div style="background: rgba(13, 17, 23, 0.94); border: 1.5px solid rgba(240, 185, 11, 0.45); border-radius: 12px; padding: 10px 20px; display: flex; align-items: center; justify-content: space-between;">
                <div style="display:flex; align-items:center; gap:12px;">
                    <div style="width:34px; height:34px; background:linear-gradient(135deg, #f0b90b, #d4a007); border-radius:8px; display:flex; align-items:center; justify-content:center; font-family:'Orbitron'; font-weight:900; color:#000; font-size:1.1rem;">⚡</div>
                    <div>
                        <div style="font-family:'Orbitron', sans-serif; font-weight:900; color:#ffffff; font-size:1.05rem;">TERMINAL TRADER <span style="color:#f0b90b;">PRO</span></div>
                        <div style="font-family:'JetBrains Mono', monospace; font-size:0.62rem; color:#848e9c;">QUANTITATIVE WORKSPACE ACTIVE</div>
                    </div>
                </div>
                <div style="font-family:'JetBrains Mono', monospace; font-size:0.8rem; color:#848e9c; background:rgba(255,255,255,0.05); padding:5px 12px; border-radius:6px; border:1px solid rgba(255,255,255,0.1);">
                    MS SERVEUR : <span style="color:#ffffff; font-weight:700;">{latency_ms} ms</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with col_btn:
        if st.button("← ACCUEIL"):
            st.session_state.page = "welcome"
            st.rerun()

    st.markdown("""
        <div class="hud-card" style="margin-top: 15px;">
            <div style="font-family:'Orbitron', sans-serif; font-size:1.1rem; font-weight:900; color:#f0b90b;">
                🚀 ESPACE DE TRAVAIL ACTIF
            </div>
            <p style="color:#848e9c; margin-top:10px; font-size:0.85rem; line-height:1.5;">
                Le système est à présent stable et opérationnel.<br/>
                Tu peux ajouter tes outils, graphiques ou modules dans cette zone.
            </p>
        </div>
    """, unsafe_allow_html=True)
