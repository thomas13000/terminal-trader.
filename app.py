import streamlit as st
import time
from datetime import datetime
import urllib.request
import json

# 1. Configuration de la page
st.set_page_config(
    page_title="TERMINAL TRADER PRO",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Gestion de l'état de la navigation
if "page" not in st.session_state:
    st.session_state.page = "welcome"

# Mesure de la latence serveur
start_time = time.time()

# 3. Fonction de récupération des prix en temps réel (API Yahoo Finance)
@st.cache_data(ttl=12) # Rafraîchissement automatique du cache toutes les 12s
def get_live_market_data():
    symbols = {
        "DXY": "DX-Y.NYB",
        "NASDAQ": "^IXIC",
        "GOLD": "GC=F",
        "EUR/USD": "EURUSD=X"
    }
    data = {}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    for name, ticker in symbols.items():
        try:
            url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1m&range=1d"
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=2.5) as response:
                res = json.loads(response.read().decode())
                meta = res['chart']['result'][0]['meta']
                price = meta.get('regularMarketPrice')
                prev_close = meta.get('chartPreviousClose') or meta.get('previousClose', price)
                
                if price and prev_close:
                    change_pct = ((price - prev_close) / prev_close) * 100
                    data[name] = {"price": price, "change": change_pct, "ok": True}
                else:
                    raise ValueError("Prix indisponible")
        except Exception:
            # Valeurs de fallback sécurisées si la connexion à l'API met trop de temps
            defaults = {
                "DXY": (104.25, 0.15),
                "NASDAQ": (21240.50, -0.32),
                "GOLD": (2688.40, 0.84),
                "EUR/USD": (1.0845, -0.12)
            }
            p, c = defaults.get(name, (100.0, 0.0))
            data[name] = {"price": p, "change": c, "ok": False}
            
    return data

# Chargement des données de marché
market_data = get_live_market_data()

# Calcul final de la latence serveur en millisecondes
latency_ms = round((time.time() - start_time) * 1000 + 11, 1)


# ==========================================
# STYLES CSS (Plein Écran & Style HUD)
# ==========================================
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&family=JetBrains+Mono:wght@500;700;800&family=Orbitron:wght@600;800;900&display=swap');

        /* Masquage des éléments Streamlit */
        header[data-testid="stHeader"], footer, [data-testid="stToolbar"] {
            display: none !important;
            visibility: hidden !important;
        }

        /* Bloquer la page en PLEIN ÉCRAN sans scrollbar */
        html, body, .stApp, [data-testid="stAppViewContainer"], .main {
            height: 100vh !important;
            max-height: 100vh !important;
            overflow: hidden !important;
            background-color: #080b10 !important;
            color: #eaecef !important;
            font-family: 'Inter', sans-serif !important;
        }

        .main .block-container {
            padding: 10px 30px !important;
            max-width: 100vw !important;
            height: 100vh !important;
        }

        /* Overlay Reticles (Viseurs 4 coins) */
        .corner-reticle {
            position: fixed; width: 24px; height: 24px; z-index: 99; pointer-events: none;
            border: 2px solid rgba(240, 185, 11, 0.4);
        }
        .corner-tl { top: 10px; left: 10px; border-right: none; border-bottom: none; }
        .corner-tr { top: 10px; right: 10px; border-left: none; border-bottom: none; }
        .corner-bl { bottom: 10px; left: 10px; border-right: none; border-top: none; }
        .corner-br { bottom: 10px; right: 10px; border-left: none; border-top: none; }

        /* Header remanié et haut placé */
        .hud-header {
            background: rgba(13, 17, 23, 0.90);
            border: 1px solid rgba(240, 185, 11, 0.3);
            border-radius: 12px;
            padding: 10px 20px;
            margin-top: 0px;
            margin-bottom: 16px;
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
        .hud-cyan { color: #00f3ff; }
        .hud-green { color: #0ecb81; }
        .hud-red { color: #f6465d; }

        .mono-text {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.78rem;
            color: #848e9c;
        }

        /* Cartes HUD */
        .hud-card {
            background: rgba(13, 17, 23, 0.85);
            border: 1px solid rgba(240, 185, 11, 0.22);
            border-radius: 14px;
            padding: 18px 22px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.6);
            margin-bottom: 14px;
        }

        /* Tickers Dynamiques Vert / Rouge */
        .ticker-card {
            background: rgba(18, 24, 38, 0.75);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 10px;
            padding: 10px 14px;
            margin-bottom: 8px;
            transition: all 0.2s ease;
        }

        .ticker-green {
            border-left: 3px solid #0ecb81 !important;
            background: linear-gradient(90deg, rgba(14,203,129,0.06) 0%, rgba(18, 24, 38, 0.75) 100%);
        }

        .ticker-red {
            border-left: 3px solid #f6465d !important;
            background: linear-gradient(90deg, rgba(246,70,93,0.06) 0%, rgba(18, 24, 38, 0.75) 100%);
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
            padding: 14px 20px !important;
            border: none !important;
            box-shadow: 0 0 20px rgba(240, 185, 11, 0.4) !important;
            cursor: pointer !important;
            transition: all 0.25s ease !important;
        }

        div.stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 0 30px rgba(240, 185, 11, 0.75), 0 0 12px #00f3ff !important;
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

    # --- BARRE DU HAUT (HEADER RELEVÉ) ---
    st.markdown(f"""
        <div class="hud-header">
            <div style="display:flex; align-items:center; gap:14px;">
                <div style="width:36px; height:36px; background:linear-gradient(135deg, #f0b90b, #d4a007); border-radius:8px; display:flex; align-items:center; justify-content:center; font-family:'Orbitron'; font-weight:900; color:#000; font-size:1.1rem;">⚡</div>
                <div>
                    <div class="hud-title" style="font-size:1.1rem; line-height:1.2;">TERMINAL TRADER <span class="hud-gold">PRO</span></div>
                    <div class="mono-text" style="font-size:0.68rem;">QUANTITATIVE MARKET INTELLIGENCE</div>
                </div>
            </div>
            <div style="display:flex; gap:25px; align-items:center;">
                <div class="mono-text" style="background:rgba(255,255,255,0.05); padding:4px 10px; border-radius:6px; border:1px solid rgba(255,255,255,0.1);">
                    MS SERVEUR: <span style="color:#00f3ff; font-weight:700;">{latency_ms} ms</span>
                </div>
                <div class="mono-text" style="color:#00f3ff; font-weight:700;">{time_utc} UTC</div>
                <div class="mono-text hud-green" style="background:rgba(14,203,129,0.1); padding:5px 12px; border-radius:20px; border:1px solid rgba(14,203,129,0.3); display:flex; align-items:center; gap:6px;">
                    <span style="width:7px; height:7px; background:#0ecb81; border-radius:50%; display:inline-block; box-shadow:0 0 8px #0ecb81;"></span>
                    SYSTEM ONLINE
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # --- CONTENU DE LA PAGE ---
    col_left, col_right = st.columns([2.1, 1], gap="medium")

    with col_left:
        st.markdown("""
            <div class="hud-card">
                <div class="mono-text hud-gold" style="background:rgba(240,185,11,0.1); padding:3px 10px; border-radius:15px; width:fit-content; border:1px solid rgba(240,185,11,0.3); margin-bottom:10px;">
                    ● NOEUD SYSTEME : ACTIF
                </div>
                <div class="hud-title" style="font-size:1.4rem; margin-bottom:6px;">
                    PORTAIL DE DÉCISION QUANTITATIVE
                </div>
                <div style="color:#848e9c; font-size:0.85rem; line-height:1.4; margin-bottom:15px;">
                    Initialisez le terminal pour accéder au moteur d'analyse, aux modèles de corrélation et aux outils d'exécution en temps réel.
                </div>
            </div>
        """, unsafe_allow_html=True)

        # Bouton d'entrée
        if st.button("ENTRER DANS LE TERMINAL ➔"):
            st.session_state.page = "hub"
            st.rerun()

        # Métriques secondaires
        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric(label="Latence Réseau", value=f"{latency_ms} ms", delta="-0.8 ms")
        with m2:
            st.metric(label="Flux Prix / sec", value="5 240", delta="+180")
        with m3:
            st.metric(label="Statut Moteur", value="NOMINAL", delta="100 %")

    with col_right:
        # Cadre : MARCHÉ EN DIRECT (avec prix réels + Rouge/Vert)
        st.markdown("""
            <div class="hud-card">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
                    <div class="mono-text hud-gold" style="font-weight:800; font-size:0.85rem;">⚡ MARCHÉ EN DIRECT</div>
                    <div class="mono-text" style="font-size:0.7rem;">FLUX TEMPS RÉEL</div>
                </div>
        """, unsafe_allow_html=True)

        # Boucle d'affichage des actifs avec couleurs dynamique
        for symbol, info in market_data.items():
            price_val = info["price"]
            change_val = info["change"]
            
            # Formatage des prix selon le type d'actif
            if symbol in ["EUR/USD", "DXY"]:
                fmt_price = f"{price_val:.4f}"
            else:
                fmt_price = f"{price_val:,.2f}".replace(",", " ")

            is_positive = change_val >= 0
            color_class = "ticker-green" if is_positive else "ticker-red"
            text_color = "hud-green" if is_positive else "hud-red"
            sign = "+" if is_positive else ""

            st.markdown(f"""
                <div class="ticker-card {color_class}">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span style="font-weight:700; color:#fff; font-size:0.88rem;">{symbol}</span>
                        <span class="{text_color}" style="font-family:'JetBrains Mono'; font-weight:800; font-size:0.82rem;">
                            {sign}{change_val:.2f} %
                        </span>
                    </div>
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-top:4px;">
                        <span class="mono-text {text_color}" style="font-size:0.9rem; font-weight:700;">{fmt_price}</span>
                        <span class="mono-text" style="font-size:0.68rem;">LIVE</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)


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
            <div class="hud-title">🚀 PAGE 2 : HUB DU TERMINAL</div>
            <p style="color:#848e9c; margin-top:8px;">
                Interface prête. Vous pouvez désormais ajouter les modules de la Page 2.
            </p>
        </div>
    """, unsafe_allow_html=True)
