import streamlit as st

st.set_page_config(
    page_title="TERMINAL TRADER PRO",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Navigation gérée en mémoire (session_state) sans toucher à l'URL
if "page" not in st.session_state:
    st.session_state.page = "welcome"

# Initialisation de la liste des sites financiers
if "custom_sites" not in st.session_state:
    st.session_state.custom_sites = [
        {"name": "TradingView", "url": "https://fr.tradingview.com", "category": "Graphiques", "desc": "Analyse technique et graphiques interactifs en direct"},
        {"name": "Investing.com", "url": "https://fr.investing.com", "category": "Actu & Macro", "desc": "Calendrier économique et cotations internationales"},
        {"name": "Forex Factory", "url": "https://www.forexfactory.com", "category": "Calendrier", "desc": "Suivi des annonces de la FED, BCE et chiffres macro"},
        {"name": "CoinMarketCap", "url": "https://coinmarketcap.com/fr/", "category": "Crypto", "desc": "Capitalisation, volumes et prix des crypto-actifs"},
        {"name": "Yahoo Finance", "url": "https://fr.finance.yahoo.com", "category": "Marchés", "desc": "Suivi des actions, indices et actualités boursières"},
        {"name": "Bloomberg", "url": "https://www.bloomberg.com", "category": "Actu & Macro", "desc": "Actualités économiques et financières internationales"}
    ]

# ==========================================
# PAGE 1 : WELCOME SCREEN (GLOBE 3D)
# ==========================================
if st.session_state.page == "welcome":
    st.markdown("""
        <style>
            #root > div:nth-child(1) > div > div > div > div { padding: 0 !important; }
            header { visibility: hidden !important; }
            footer { visibility: hidden !important; }
            .stApp { background-color: #080b10; overflow: hidden; }
            iframe { border: none !important; width: 100vw !important; height: 82vh !important; }
            .block-container { padding: 0 !important; max-width: 100% !important; }
            
            /* Style du bouton Streamlit de navigation */
            div.stButton > button {
                width: 90%;
                max-width: 400px;
                margin: 0 auto;
                display: block;
                background: linear-gradient(135deg, #f0b90b 0%, #d4a007 100%) !important;
                color: #080b10 !important;
                border: none !important;
                padding: 16px 24px !important;
                font-family: 'Orbitron', sans-serif !important;
                font-size: 1rem !important;
                font-weight: 900 !important;
                letter-spacing: 2px !important;
                border-radius: 12px !important;
                box-shadow: 0 0 25px rgba(240, 185, 11, 0.45) !important;
                transition: all 0.3s ease !important;
            }
            div.stButton > button:hover {
                transform: translateY(-2px);
                box-shadow: 0 0 35px rgba(240, 185, 11, 0.7) !important;
                color: #000000 !important;
            }
        </style>
    """, unsafe_allow_html=True)

    welcome_html_code = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TERMINAL TRADER PRO — 3D Globe Welcome Screen</title>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;900&family=JetBrains+Mono:wght@400;600;700;800&family=Orbitron:wght@500;700;900&display=swap" rel="stylesheet">
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

    <style>
        :root {
            --bg-dark: #080b10;
            --bg-card: rgba(13, 17, 23, 0.82);
            --gold-main: #f0b90b;
            --gold-glow: rgba(240, 185, 11, 0.45);
            --cyan-neon: #00f3ff;
            --green-up: #0ecb81;
            --red-down: #f6465d;
            --text-main: #eaecef;
            --text-muted: #848e9c;
            --border-glass: rgba(240, 185, 11, 0.25);
            --font-sans: 'Inter', sans-serif;
            --font-mono: 'JetBrains Mono', monospace;
            --font-display: 'Orbitron', sans-serif;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; user-select: none; }

        body, html {
            width: 100%; height: 100%; overflow: hidden;
            background-color: var(--bg-dark); color: var(--text-main); font-family: var(--font-sans);
        }

        #webgl-canvas {
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 1; cursor: grab;
        }

        .hud-grid-overlay {
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 2; pointer-events: none;
            background: 
                radial-gradient(circle at 50% 50%, transparent 35%, rgba(8, 11, 16, 0.88) 90%),
                linear-gradient(to right, rgba(255,255,255,0.015) 1px, transparent 1px),
                linear-gradient(to bottom, rgba(255,255,255,0.015) 1px, transparent 1px);
            background-size: 100% 100%, 50px 50px, 50px 50px;
        }

        .hud-header {
            position: fixed; top: 20px; left: 50%; transform: translateX(-50%);
            width: calc(100vw - 80px); max-width: 1600px; z-index: 20; display: flex;
            align-items: center; justify-content: space-between; padding: 12px 24px;
            background: var(--bg-card); border: 1px solid var(--border-glass); border-radius: 14px;
            backdrop-filter: blur(20px);
        }

        .brand-container { display: flex; align-items: center; gap: 14px; }
        .brand-logo {
            width: 38px; height: 38px; background: linear-gradient(135deg, var(--gold-main), #d4a007);
            border-radius: 8px; display: flex; align-items: center; justify-content: center;
            font-family: var(--font-display); font-weight: 900; color: #000; font-size: 1.2rem;
        }
        .brand-text h1 { font-family: var(--font-display); font-size: 1.05rem; letter-spacing: 2.5px; color: #fff; }
        .brand-text span { color: var(--gold-main); }
        .brand-sub { font-family: var(--font-mono); font-size: 0.68rem; color: var(--text-muted); }

        .left-hero-panel {
            position: fixed; top: 105px; left: 40px; width: 360px; z-index: 20;
            background: var(--bg-card); border: 1px solid var(--border-glass); border-radius: 18px;
            padding: 22px; backdrop-filter: blur(20px); display: flex; flex-direction: column; gap: 16px;
        }

        .clock-section {
            display: grid; grid-template-columns: 1fr 1fr; gap: 12px;
            background: rgba(8, 11, 16, 0.6); border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 12px; padding: 12px;
        }
        .clock-label { font-family: var(--font-mono); font-size: 0.62rem; color: var(--text-muted); }
        .clock-time { font-family: var(--font-mono); font-size: 1.5rem; font-weight: 800; color: #fff; }

        button.btn-enter-terminal {
            background: linear-gradient(135deg, var(--gold-main) 0%, #d4a007 100%);
            color: #080b10 !important; border: none; padding: 16px 20px; font-family: var(--font-display);
            font-size: 0.85rem; font-weight: 900; letter-spacing: 2px; border-radius: 12px;
            cursor: pointer; box-shadow: 0 0 25px var(--gold-glow); transition: all 0.3s ease;
            width: 100%;
        }
        button.btn-enter-terminal:hover { transform: translateY(-2px); }

        .right-sidebar { position: fixed; top: 105px; right: 40px; width: 320px; z-index: 20; display: flex; flex-direction: column; gap: 10px; }
        .ticker-card { background: var(--bg-card); border: 1px solid rgba(255, 255, 255, 0.08); border-left: 3px solid var(--gold-main); border-radius: 12px; padding: 10px 14px; backdrop-filter: blur(16px); display: flex; align-items: center; justify-content: space-between; }
        .ticker-symbol { font-family: var(--font-mono); font-size: 0.82rem; font-weight: 700; color: #fff; }
        .ticker-price { font-family: var(--font-mono); font-size: 0.88rem; font-weight: 800; color: #fff; }

        @media (max-width: 900px) { .right-sidebar { display: none; } }
    </style>
</head>
<body>

    <canvas id="webgl-canvas"></canvas>
    <div class="hud-grid-overlay"></div>

    <header class="hud-header">
        <div class="brand-container">
            <div class="brand-logo">⚡</div>
            <div class="brand-text">
                <h1>TERMINAL TRADER <span>PRO</span></h1>
                <div class="brand-sub">QUANTITATIVE MARKET INTELLIGENCE</div>
            </div>
        </div>
    </header>

    <div class="left-hero-panel">
        <div class="clock-section">
            <div>
                <div class="clock-label">PARIS</div>
                <div class="clock-time" id="clock-paris">00:00:00</div>
            </div>
            <div>
                <div class="clock-label">NEW YORK</div>
                <div class="clock-time" id="clock-ny">00:00:00</div>
            </div>
        </div>

        <button onclick="triggerStreamlitNavigation()" class="btn-enter-terminal">
            ENTRER DANS LE TERMINAL ➔
        </button>
    </div>

    <aside class="right-sidebar">
        <div class="ticker-card">
            <span class="ticker-symbol">BTC / USDT</span>
            <span class="ticker-price" id="price-btc">Chargement...</span>
        </div>
        <div class="ticker-card">
            <span class="ticker-symbol">US100</span>
            <span class="ticker-price">21,240.10</span>
        </div>
        <div class="ticker-card">
            <span class="ticker-symbol">XAU / USD</span>
            <span class="ticker-price">$2,688.30</span>
        </div>
    </aside>

    <script>
        // Déclenche le clic sur le bouton Streamlit dans le document parent
        function triggerStreamlitNavigation() {
            try {
                const parentButtons = window.parent.document.querySelectorAll('button');
                for (let btn of parentButtons) {
                    if (btn.innerText.includes('ENTRER DANS LE TERMINAL')) {
                        btn.click();
                        return;
                    }
                }
            } catch(e) {
                console.warn('Accès parent restreint:', e);
            }
        }

        async function updateBTC() {
            try {
                const res = await fetch('https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT');
                const data = await res.json();
                document.getElementById('price-btc').textContent = '$' + parseFloat(data.lastPrice).toLocaleString('en-US', {minimumFractionDigits: 2});
            } catch(e) {}
        }
        setInterval(updateBTC, 3000); updateBTC();

        function updateClocks() {
            const now = new Date();
            document.getElementById('clock-paris').textContent = new Intl.DateTimeFormat('fr-FR', { timeZone: 'Europe/Paris', hour: '2-digit', minute: '2-digit', second: '2-digit' }).format(now);
            document.getElementById('clock-ny').textContent = new Intl.DateTimeFormat('fr-FR', { timeZone: 'America/New_York', hour: '2-digit', minute: '2-digit', second: '2-digit' }).format(now);
        }
        setInterval(updateClocks, 1000); updateClocks();

        const canvas = document.getElementById('webgl-canvas');
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
        camera.position.z = 25;

        const renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
        renderer.setSize(window.innerWidth, window.innerHeight);

        const globe = new THREE.Group();
        scene.add(globe);

        const geo = new THREE.SphereGeometry(8, 32, 32);
        const mat = new THREE.MeshBasicMaterial({ color: 0xf0b90b, wireframe: true, transparent: true, opacity: 0.25 });
        globe.add(new THREE.Mesh(geo, mat));

        function animate() {
            requestAnimationFrame(animate);
            globe.rotation.y += 0.003;
            renderer.render(scene, camera);
        }
        animate();

        window.addEventListener('keydown', (e) => {
            if (e.code === 'Enter') triggerStreamlitNavigation();
        });
    </script>
</body>
</html>
    """

    st.components.v1.html(welcome_html_code, height=750)

    # Bouton Streamlit qui effectue la bascule d'état sans toucher à l'URL
    if st.button("ENTRER DANS LE TERMINAL ➔", key="nav_btn"):
        st.session_state.page = "hub"
        st.rerun()

# ==========================================
# PAGE 2 : HUB FINANCIER
# ==========================================
elif st.session_state.page == "hub":
    st.markdown("""
        <style>
            header[data-testid="stHeader"] { visibility: hidden !important; }
            footer { visibility: hidden !important; }
            .stApp { background-color: #080b10 !important; color: #eaecef !important; }
            .main .block-container { max-width: 1400px !important; padding-top: 2rem !important; }
            .stButton>button { background: linear-gradient(135deg, #f0b90b 0%, #d4a007 100%) !important; color: #000 !important; font-weight: 700 !important; border-radius: 8px !important; }
            .site-card { background: rgba(13, 17, 23, 0.85); border: 1px solid rgba(240, 185, 11, 0.2); border-radius: 12px; padding: 18px; margin-bottom: 15px; }
            .site-badge { font-size: 0.7rem; background: rgba(0, 243, 255, 0.1); color: #00f3ff; border: 1px solid rgba(0, 243, 255, 0.3); padding: 2px 8px; border-radius: 10px; display: inline-block; margin-bottom: 8px; }
        </style>
    """, unsafe_allow_html=True)

    col_title, col_back = st.columns([5, 1])
    with col_title:
        st.markdown("<h1 style='color: #f0b90b; font-family: monospace; font-size: 1.8rem; margin: 0;'>⚡ FINANCIAL TERMINAL HUB</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color: #848e9c; font-size: 0.9rem;'>Centre de commande et outils d'analyse financière</p>", unsafe_allow_html=True)
    with col_back:
        if st.button("← GLOBE 3D"):
            st.session_state.page = "welcome"
            st.rerun()

    st.markdown("---")

    st.markdown("<h3 style='color: #ffffff; font-size: 1.1rem;'>📈 Graphique en direct (TradingView)</h3>", unsafe_allow_html=True)
    
    tv_widget_html = """
    <div class="tradingview-widget-container" style="height:500px;width:100%;">
      <div id="tradingview_chart" style="height:500px;width:100%;"></div>
      <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
      <script type="text/javascript">
      new TradingView.widget({
        "autosize": true,
        "symbol": "BINANCE:BTCUSDT",
        "interval": "60",
        "timezone": "Europe/Paris",
        "theme": "dark",
        "style": "1",
        "locale": "fr",
        "backgroundColor": "rgba(8, 11, 16, 1)",
        "container_id": "tradingview_chart"
      });
      </script>
    </div>
    """
    st.components.v1.html(tv_widget_html, height=520)

    st.markdown("---")

    col_left, col_right = st.columns([2, 1])

    with col_left:
        st.markdown("<h3 style='color: #ffffff; font-size: 1.1rem;'>🌐 Mes Raccourcis & Sites Financiers</h3>", unsafe_allow_html=True)
        cards_cols = st.columns(2)
        for idx, site in enumerate(st.session_state.custom_sites):
            col_target = cards_cols[idx % 2]
            with col_target:
                st.markdown(f"""
                    <div class="site-card">
                        <span class="site-badge">{site['category']}</span>
                        <h4 style="color: #ffffff; margin: 0 0 6px 0; font-size: 1rem;">{site['name']}</h4>
                        <p style="color: #848e9c; font-size: 0.8rem; margin-bottom: 12px; height: 36px; overflow: hidden;">{site['desc']}</p>
                    </div>
                """, unsafe_allow_html=True)
                
                c_btn1, c_btn2 = st.columns([3, 1])
                with c_btn1:
                    st.link_button("Ouvrir le site ↗", site['url'], use_container_width=True)
                with c_btn2:
                    if st.button("🗑️", key=f"del_{idx}"):
                        st.session_state.custom_sites.pop(idx)
                        st.rerun()

    with col_right:
        st.markdown("<h3 style='color: #ffffff; font-size: 1.1rem;'>➕ Ajouter un Site</h3>", unsafe_allow_html=True)
        with st.form("add_site_form"):
            new_name = st.text_input("Nom du site", placeholder="Ex: ForexLive")
            new_url = st.text_input("URL complète", placeholder="https://www.forexlive.com")
            new_cat = st.selectbox("Catégorie", ["Graphiques", "Actu & Macro", "Calendrier", "Crypto", "Marchés", "Outil Perso"])
            new_desc = st.text_area("Description", placeholder="Ex: Flux d'actualités rapide", height=80)
            
            if st.form_submit_button("Ajouter au Terminal"):
                if new_name and new_url:
                    formatted_url = new_url if new_url.startswith("http") else f"https://{new_url}"
                    st.session_state.custom_sites.append({
                        "name": new_name,
                        "url": formatted_url,
                        "category": new_cat,
                        "desc": new_desc or "Aucune description"
                    })
                    st.rerun()
