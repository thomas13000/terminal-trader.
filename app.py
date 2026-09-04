import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(
    page_title="TERMINAL TRADER PRO",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Gestion de l'état de la navigation
if "page" not in st.session_state:
    st.session_state.page = "welcome"

# ==========================================
# CREATION DU COMPOSANT HTML/JS PERSONNALISÉ
# ==========================================
COMP_DIR = os.path.abspath("welcome_component")
os.makedirs(COMP_DIR, exist_ok=True)
INDEX_HTML_PATH = os.path.join(COMP_DIR, "index.html")

welcome_html_code = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TERMINAL TRADER PRO</title>
    
    <!-- Streamlit Custom Component API -->
    <script src="https://cdn.jsdelivr.net/npm/streamlit-component-lib@1.4.0/dist/streamlit-component-lib.js"></script>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;900&family=JetBrains+Mono:wght@400;600;700;800&family=Orbitron:wght@500;700;900&display=swap" rel="stylesheet">
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

    <style>
        :root {
            --bg-dark: #080b10;
            --bg-card: rgba(13, 17, 23, 0.85);
            --gold-main: #f0b90b;
            --gold-glow: rgba(240, 185, 11, 0.45);
            --cyan-neon: #00f3ff;
            --cyan-glow: rgba(0, 243, 255, 0.35);
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
            width: 100vw; height: 100vh; overflow: hidden !important;
            position: fixed; top: 0; left: 0; touch-action: none;
            background-color: var(--bg-dark); color: var(--text-main); font-family: var(--font-sans);
        }

        #webgl-canvas {
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 1; cursor: grab;
        }
        #webgl-canvas:active { cursor: grabbing; }

        .hud-grid-overlay {
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 2; pointer-events: none;
            background: 
                radial-gradient(circle at 50% 50%, transparent 35%, rgba(8, 11, 16, 0.88) 90%),
                linear-gradient(to right, rgba(255,255,255,0.015) 1px, transparent 1px),
                linear-gradient(to bottom, rgba(255,255,255,0.015) 1px, transparent 1px);
            background-size: 100% 100%, 50px 50px, 50px 50px;
        }

        .corner-reticle {
            position: fixed; width: 36px; height: 36px; z-index: 10; pointer-events: none;
            border: 2px solid rgba(240, 185, 11, 0.4);
        }
        .corner-tl { top: 20px; left: 20px; border-right: none; border-bottom: none; }
        .corner-tr { top: 20px; right: 20px; border-left: none; border-bottom: none; }
        .corner-bl { bottom: 20px; left: 20px; border-right: none; border-top: none; }
        .corner-br { bottom: 20px; right: 20px; border-left: none; border-top: none; }

        .hud-header {
            position: fixed; top: 20px; left: 50%; transform: translateX(-50%);
            width: calc(100vw - 80px); max-width: 1600px; z-index: 20; display: flex;
            align-items: center; justify-content: space-between; padding: 12px 24px;
            background: var(--bg-card); border: 1px solid var(--border-glass); border-radius: 14px;
            backdrop-filter: blur(20px); box-shadow: 0 8px 32px rgba(0, 0, 0, 0.6);
        }

        .brand-container { display: flex; align-items: center; gap: 14px; }
        .brand-logo {
            width: 38px; height: 38px; background: linear-gradient(135deg, var(--gold-main), #d4a007);
            border-radius: 8px; display: flex; align-items: center; justify-content: center;
            font-family: var(--font-display); font-weight: 900; color: #000; font-size: 1.2rem;
            box-shadow: 0 0 15px var(--gold-glow);
        }
        .brand-text h1 { font-family: var(--font-display); font-size: 1.05rem; letter-spacing: 2.5px; color: #fff; text-transform: uppercase; }
        .brand-text span { color: var(--gold-main); }
        .brand-sub { font-family: var(--font-mono); font-size: 0.68rem; color: var(--text-muted); letter-spacing: 1px; }

        .system-status-bar { display: flex; align-items: center; gap: 22px; }
        .status-item { display: flex; align-items: center; gap: 8px; font-family: var(--font-mono); font-size: 0.72rem; color: var(--text-muted); }
        .status-dot {
            width: 8px; height: 8px; border-radius: 50%; background-color: var(--green-up);
            box-shadow: 0 0 10px var(--green-up); animation: pulse-dot 1.8s infinite;
        }

        @keyframes pulse-dot {
            0% { transform: scale(0.9); opacity: 0.7; }
            50% { transform: scale(1.3); opacity: 1; }
            100% { transform: scale(0.9); opacity: 0.7; }
        }

        .left-hero-panel {
            position: fixed; top: 105px; left: 40px; width: 380px; z-index: 20;
            background: var(--bg-card); border: 1px solid var(--border-glass); border-radius: 18px;
            padding: 26px; backdrop-filter: blur(20px); box-shadow: 0 10px 40px rgba(0, 0, 0, 0.7);
            display: flex; flex-direction: column; gap: 18px;
        }

        .panel-badge {
            display: inline-flex; align-items: center; gap: 8px; font-family: var(--font-mono);
            font-size: 0.65rem; font-weight: 700; letter-spacing: 2px; color: var(--gold-main);
            background: rgba(240, 185, 11, 0.1); padding: 5px 12px; border-radius: 20px;
            border: 1px solid rgba(240, 185, 11, 0.3); width: fit-content;
        }

        .clock-section {
            display: grid; grid-template-columns: 1fr 1fr; gap: 12px;
            background: rgba(8, 11, 16, 0.6); border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 12px; padding: 12px;
        }
        .clock-block { display: flex; flex-direction: column; }
        .clock-label { font-family: var(--font-mono); font-size: 0.62rem; color: var(--text-muted); letter-spacing: 1px; }
        .clock-time { font-family: var(--font-mono); font-size: 1.5rem; font-weight: 800; color: #fff; letter-spacing: -0.5px; }

        .router-box {
            background: rgba(8, 11, 16, 0.6); border: 1px dashed rgba(240, 185, 11, 0.3);
            border-radius: 10px; padding: 12px; display: flex; flex-direction: column; gap: 8px;
        }
        .router-header { display: flex; justify-content: space-between; font-family: var(--font-mono); font-size: 0.65rem; color: var(--gold-main); font-weight: 700; }
        .router-ticker { font-family: var(--font-mono); font-size: 0.78rem; color: #fff; display: flex; align-items: center; justify-content: space-between; }

        /* BOUTON D'ACTION PRINCIPAL */
        .btn-enter-terminal {
            position: relative; background: linear-gradient(135deg, var(--gold-main) 0%, #d4a007 100%);
            color: #080b10 !important; text-decoration: none; padding: 18px 24px; font-family: var(--font-display);
            font-size: 0.88rem; font-weight: 900; letter-spacing: 2px; border-radius: 12px;
            cursor: pointer; overflow: hidden; box-shadow: 0 0 25px var(--gold-glow);
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            display: flex; align-items: center; justify-content: center; gap: 12px; width: 100%; border: none;
            outline: none;
        }
        .btn-enter-terminal:hover {
            transform: translateY(-3px) scale(1.02);
            box-shadow: 0 0 40px rgba(240, 185, 11, 0.7), 0 0 12px var(--cyan-neon);
            color: #000 !important;
        }

        .hotkey-legend { font-family: var(--font-mono); font-size: 0.63rem; color: var(--text-muted); text-align: center; display: flex; justify-content: center; gap: 12px; }
        .hotkey-badge { background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); padding: 2px 6px; border-radius: 4px; color: var(--gold-main); font-weight: 700; }

        .right-sidebar { position: fixed; top: 105px; right: 40px; width: 340px; z-index: 20; display: flex; flex-direction: column; gap: 10px; }
        .sidebar-title { font-family: var(--font-display); font-size: 0.75rem; letter-spacing: 2px; color: var(--gold-main); background: var(--bg-card); border: 1px solid var(--border-glass); padding: 10px 16px; border-radius: 10px; backdrop-filter: blur(16px); display: flex; align-items: center; justify-content: space-between; }
        
        .ticker-card { background: var(--bg-card); border: 1px solid rgba(255, 255, 255, 0.08); border-left: 3px solid var(--gold-main); border-radius: 12px; padding: 10px 14px; backdrop-filter: blur(16px); transition: all 0.25s ease; display: flex; align-items: center; justify-content: space-between; }
        .ticker-card:hover { border-color: rgba(240, 185, 11, 0.5); background: rgba(18, 24, 34, 0.88); transform: translateX(-4px); }
        .ticker-info { display: flex; flex-direction: column; gap: 2px; }
        .ticker-symbol { font-family: var(--font-mono); font-size: 0.82rem; font-weight: 700; color: #fff; }
        .ticker-sub { font-size: 0.65rem; color: var(--text-muted); }
        .ticker-price-block { text-align: right; display: flex; flex-direction: column; gap: 2px; }
        .ticker-price { font-family: var(--font-mono); font-size: 0.88rem; font-weight: 800; color: #fff; }
        .ticker-change { font-family: var(--font-mono); font-size: 0.68rem; font-weight: 700; }
        .change-up { color: var(--green-up); }
        .change-down { color: var(--red-down); }
        .sparkline-canvas { width: 65px; height: 26px; }

        .bottom-deck { position: fixed; bottom: 25px; left: 50%; transform: translateX(-50%); z-index: 20; display: flex; align-items: center; gap: 10px; background: var(--bg-card); border: 1px solid var(--border-glass); border-radius: 30px; padding: 8px 18px; backdrop-filter: blur(20px); box-shadow: 0 10px 30px rgba(0,0,0,0.8); }
        .hub-chip { font-family: var(--font-mono); font-size: 0.68rem; font-weight: 700; color: var(--text-muted); padding: 6px 14px; border-radius: 20px; cursor: pointer; transition: all 0.25s ease; border: 1px solid transparent; }
        .hub-chip:hover, .hub-chip.active { color: #000; background: var(--gold-main); box-shadow: 0 0 15px var(--gold-glow); border-color: var(--gold-main); }
        .deck-divider { width: 1px; height: 18px; background: rgba(255, 255, 255, 0.15); }
    </style>
</head>
<body>

    <canvas id="webgl-canvas"></canvas>

    <div class="hud-grid-overlay"></div>
    <div class="corner-reticle corner-tl"></div>
    <div class="corner-reticle corner-tr"></div>
    <div class="corner-reticle corner-bl"></div>
    <div class="corner-reticle corner-br"></div>

    <header class="hud-header">
        <div class="brand-container">
            <div class="brand-logo">⚡</div>
            <div class="brand-text">
                <h1>TERMINAL TRADER <span>PRO</span></h1>
                <div class="brand-sub">QUANTITATIVE MARKET INTELLIGENCE — v5.5</div>
            </div>
        </div>

        <div class="system-status-bar">
            <div class="status-item">
                <span class="status-dot"></span>
                <span>FLUX TEMPS RÉEL ACTIF</span>
            </div>
            <div class="status-item" style="color: var(--cyan-neon);">
                <span>LATENCE: <span id="ping-val">14</span>ms</span>
            </div>
        </div>
    </header>

    <div class="left-hero-panel">
        <div class="panel-badge">
            <span class="status-dot"></span> SESSION EN DIRECT
        </div>

        <div class="clock-section">
            <div class="clock-block">
                <span class="clock-label">PARIS</span>
                <span class="clock-time" id="clock-paris">00:00:00</span>
            </div>
            <div class="clock-block">
                <span class="clock-label">NEW YORK</span>
                <span class="clock-time" id="clock-ny">00:00:00</span>
            </div>
        </div>

        <div class="router-box">
            <div class="router-header">
                <span>FLUX DE CAPITAUX ACTIFS</span>
                <span style="color: var(--cyan-neon);" id="flow-val">$5.24B / s</span>
            </div>
            <div class="router-ticker">
                <span id="flow-route">LONDON ➔ NEW YORK</span>
                <span style="color: var(--green-up); font-size:0.72rem;">● OPTIMISÉ</span>
            </div>
        </div>

        <button class="btn-enter-terminal" id="nav-btn">
            ENTRER DANS LE TERMINAL ➔
        </button>

        <div class="hotkey-legend">
            <span><span class="hotkey-badge">ENTRÉE</span> Démarrer</span>
            <span><span class="hotkey-badge">R</span> Reset Globe</span>
        </div>
    </div>

    <aside class="right-sidebar">
        <div class="sidebar-title">
            <span>⚡ SURVEILLANCE MARCHÉS</span>
            <span style="font-family:var(--font-mono); font-size:0.65rem; color:var(--text-muted);">LIVE TICKERS</span>
        </div>

        <div class="ticker-card">
            <div class="ticker-info">
                <div class="ticker-symbol">US100</div>
                <div class="ticker-sub">Nasdaq 100 Index</div>
            </div>
            <canvas class="sparkline-canvas" id="spark-us100"></canvas>
            <div class="ticker-price-block">
                <div class="ticker-price">21,240.10</div>
                <div class="ticker-change change-up">+1.12%</div>
            </div>
        </div>

        <div class="ticker-card">
            <div class="ticker-info">
                <div class="ticker-symbol">US500</div>
                <div class="ticker-sub">S&P 500 Index</div>
            </div>
            <canvas class="sparkline-canvas" id="spark-us500"></canvas>
            <div class="ticker-price-block">
                <div class="ticker-price">5,992.40</div>
                <div class="ticker-change change-up">+0.58%</div>
            </div>
        </div>

        <div class="ticker-card">
            <div class="ticker-info">
                <div class="ticker-symbol">DXY</div>
                <div class="ticker-sub">US Dollar Index</div>
            </div>
            <canvas class="sparkline-canvas" id="spark-dxy"></canvas>
            <div class="ticker-price-block">
                <div class="ticker-price">106.45</div>
                <div class="ticker-change change-down">-0.24%</div>
            </div>
        </div>

        <div class="ticker-card">
            <div class="ticker-info">
                <div class="ticker-symbol">BTC / USDT</div>
                <div class="ticker-sub">Binance Direct Feed</div>
            </div>
            <canvas class="sparkline-canvas" id="spark-btc"></canvas>
            <div class="ticker-price-block">
                <div class="ticker-price" id="price-btc">Chargement...</div>
                <div class="ticker-change change-up" id="change-btc">+0.00%</div>
            </div>
        </div>

        <div class="ticker-card">
            <div class="ticker-info">
                <div class="ticker-symbol">XAU / USD</div>
                <div class="ticker-sub">Gold Spot</div>
            </div>
            <canvas class="sparkline-canvas" id="spark-gold"></canvas>
            <div class="ticker-price-block">
                <div class="ticker-price">$2,688.30</div>
                <div class="ticker-change change-up">+0.84%</div>
            </div>
        </div>
    </aside>

    <nav class="bottom-deck">
        <div class="hub-chip active">GLOBAL VIEW</div>
        <div class="deck-divider"></div>
        <div class="hub-chip">NEW YORK</div>
        <div class="hub-chip">LONDON</div>
        <div class="hub-chip">PARIS</div>
        <div class="hub-chip">DUBAI</div>
        <div class="hub-chip">SINGAPORE</div>
        <div class="hub-chip">HONG KONG</div>
        <div class="hub-chip">TOKYO</div>
    </nav>

    <script>
        // Fonction de communication bi-directionnelle avec Streamlit
        function triggerStreamlitNavigation() {
            if (window.Streamlit) {
                Streamlit.setComponentValue("enter_hub_" + Date.now());
            } else {
                window.parent.postMessage({
                    isStreamlitMessage: true,
                    type: "streamlit:setComponentValue",
                    value: "enter_hub_" + Date.now()
                }, "*");
            }
        }

        // Clic sur le bouton
        document.getElementById('nav-btn').addEventListener('click', (e) => {
            e.preventDefault();
            triggerStreamlitNavigation();
        });

        // Touche Entrée
        window.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.code === 'Enter') {
                triggerStreamlitNavigation();
            }
        });

        // Tickers Binance Live
        async function updateRealtimeBTC() {
            try {
                const response = await fetch('https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT');
                const data = await response.json();
                const price = parseFloat(data.lastPrice);
                const change = parseFloat(data.priceChangePercent);

                const priceEl = document.getElementById('price-btc');
                const changeEl = document.getElementById('change-btc');
                if (priceEl && changeEl) {
                    priceEl.textContent = '$' + price.toLocaleString('en-US', { minimumFractionDigits: 2 });
                    changeEl.textContent = (change >= 0 ? '+' : '') + change.toFixed(2) + '%';
                    changeEl.className = 'ticker-change ' + (change >= 0 ? 'change-up' : 'change-down');
                }
            } catch (err) {}
        }
        setInterval(updateRealtimeBTC, 2500);
        updateRealtimeBTC();

        // Horloges
        function updateClocks() {
            const now = new Date();
            document.getElementById('clock-paris').textContent = new Intl.DateTimeFormat('fr-FR', { timeZone: 'Europe/Paris', hour: '2-digit', minute: '2-digit', second: '2-digit' }).format(now);
            document.getElementById('clock-ny').textContent = new Intl.DateTimeFormat('fr-FR', { timeZone: 'America/New_York', hour: '2-digit', minute: '2-digit', second: '2-digit' }).format(now);
        }
        setInterval(updateClocks, 1000);
        updateClocks();

        // Dessin des mini graphiques Sparklines
        function drawSparkline(id, color) {
            const c = document.getElementById(id);
            if (!c) return;
            const ctx = c.getContext('2d');
            const w = c.width = c.clientWidth;
            const h = c.height = c.clientHeight;
            ctx.clearRect(0,0,w,h);
            ctx.beginPath();
            ctx.strokeStyle = color;
            ctx.lineWidth = 2;
            let points = [];
            for (let i = 0; i < 10; i++) points.push(Math.random() * (h - 6) + 3);
            ctx.moveTo(0, points[0]);
            for (let i = 1; i < points.length; i++) {
                const x = (i / (points.length - 1)) * w;
                ctx.lineTo(x, points[i]);
            }
            ctx.stroke();
        }
        drawSparkline('spark-us100', '#0ecb81');
        drawSparkline('spark-us500', '#0ecb81');
        drawSparkline('spark-dxy', '#f6465d');
        drawSparkline('spark-btc', '#0ecb81');
        drawSparkline('spark-gold', '#0ecb81');

        // Three.js 3D Globe
        const canvas = document.getElementById('webgl-canvas');
        const scene = new THREE.Scene();
        scene.fog = new THREE.FogExp2(0x080b10, 0.012);

        const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
        camera.position.set(0, 4, 28);

        const renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

        const globeGroup = new THREE.Group();
        scene.add(globeGroup);

        const GLOBE_RADIUS = 8.5;

        const coreGeo = new THREE.SphereGeometry(GLOBE_RADIUS * 0.98, 64, 64);
        const coreMat = new THREE.MeshBasicMaterial({ color: 0x0a101d, transparent: true, opacity: 0.94 });
        globeGroup.add(new THREE.Mesh(coreGeo, coreMat));

        function latLonToVector3(lat, lon, radius = GLOBE_RADIUS) {
            const phi = (90 - lat) * (Math.PI / 180);
            const theta = (lon + 180) * (Math.PI / 180);
            return new THREE.Vector3(
                -(radius * Math.sin(phi) * Math.cos(theta)),
                radius * Math.cos(phi),
                radius * Math.sin(phi) * Math.sin(theta)
            );
        }

        function createDottedGlobe() {
            const particleCount = 12000;
            const positions = new Float32Array(particleCount * 3);
            for (let i = 0; i < particleCount; i++) {
                const u = Math.random();
                const v = Math.random();
                const lat = (Math.asin(2 * u - 1) * (180 / Math.PI));
                const lon = (v * 360 - 180);
                const vec = latLonToVector3(lat, lon, GLOBE_RADIUS);
                positions[i * 3] = vec.x;
                positions[i * 3 + 1] = vec.y;
                positions[i * 3 + 2] = vec.z;
            }
            const geo = new THREE.BufferGeometry();
            geo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
            const mat = new THREE.PointsMaterial({ size: 0.1, color: 0x00f3ff, transparent: true, opacity: 0.7 });
            globeGroup.add(new THREE.Points(geo, mat));
        }
        createDottedGlobe();

        const clock = new THREE.Clock();
        function animate() {
            requestAnimationFrame(animate);
            const time = clock.getElapsedTime();
            globeGroup.rotation.y = time * 0.05;
            renderer.render(scene, camera);
        }
        animate();

        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
            if (window.Streamlit) Streamlit.setFrameHeight(window.innerHeight);
        });

        // Initialisation Streamlit Height
        if (window.Streamlit) {
            Streamlit.setFrameHeight(window.innerHeight);
        }
    </script>
</body>
</html>
"""

# Ecriture automatique du fichier HTML
with open(INDEX_HTML_PATH, "w", encoding="utf-8") as f:
    f.write(welcome_html_code)

# Declaration du composant Streamlit
welcome_component = components.declare_component("welcome_screen", path=COMP_DIR)

# ==========================================
# PAGE 1 : WELCOME SCREEN
# ==========================================
if st.session_state.page == "welcome":
    
    st.markdown("""
        <style>
            header, footer, [data-testid="stHeader"] { 
                display: none !important; 
                visibility: hidden !important; 
            }
            .stApp {
                background-color: #080b10 !important;
            }
            .main .block-container {
                padding: 0 !important;
                margin: 0 !important;
                max-width: 100vw !important;
                width: 100vw !important;
                height: 100vh !important;
            }
            iframe {
                width: 100vw !important;
                height: 100vh !important;
                border: none !important;
                display: block !important;
            }
        </style>
    """, unsafe_allow_html=True)

    # Execution du composant 3D & HUD
    event = welcome_component(key="welcome_terminal")

    # Écoute de l'événement de clic / touche Entrée transmis par JS
    if event:
        st.session_state.page = "hub"
        st.rerun()

# ==========================================
# PAGE 2 : HUB / TERMINAL (PAGE VIERGE)
# ==========================================
elif st.session_state.page == "hub":
    
    st.markdown("""
        <style>
            header[data-testid="stHeader"], footer { visibility: hidden !important; }
            .stApp {
                background-color: #080b10 !important;
                color: #eaecef !important;
            }
        </style>
    """, unsafe_allow_html=True)

    if st.button("← Retour au Globe"):
        st.session_state.page = "welcome"
        st.rerun()

    st.title("🚀 TERMINAL TRADER PRO — HUB")
    st.success("Connexion réussie ! Vous êtes désormais dans le terminal.")
