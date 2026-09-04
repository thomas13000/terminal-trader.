import streamlit as st

st.set_page_config(
    page_title="TERMINAL TRADER PRO",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Lecture des paramètres d'URL pour la navigation Streamlit
if "page" in st.query_params:
    st.session_state.page = st.query_params["page"]
elif "page" not in st.session_state:
    st.session_state.page = "welcome"

# ==========================================
# PAGE 1 : WELCOME SCREEN (DESIGN COMPLET)
# ==========================================
if st.session_state.page == "welcome":
    st.markdown("""
        <style>
            header, footer, [data-testid="stHeader"] { 
                display: none !important; 
                visibility: hidden !important; 
            }
            
            html, body, .stApp, [data-testid="stAppViewContainer"], .main, .block-container {
                overflow: hidden !important;
                height: 100vh !important;
                max-height: 100vh !important;
                width: 100vw !important;
                max-width: 100vw !important;
                padding: 0 !important;
                margin: 0 !important;
                position: fixed !important;
            }
            
            iframe {
                border: none !important;
                width: 100vw !important;
                height: 100vh !important;
                overflow: hidden !important;
                display: block !important;
            }
        </style>
    """, unsafe_allow_html=True)

    welcome_html_code = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
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
        .clock-time { font-family: var(--font-mono); font-size: 1.6rem; font-weight: 800; color: #fff; letter-spacing: -0.5px; text-shadow: 0 0 10px rgba(255, 255, 255, 0.2); }

        .router-box {
            background: rgba(8, 11, 16, 0.6); border: 1px dashed rgba(240, 185, 11, 0.3);
            border-radius: 10px; padding: 12px; display: flex; flex-direction: column; gap: 8px;
        }
        .router-header { display: flex; justify-content: space-between; font-family: var(--font-mono); font-size: 0.65rem; color: var(--gold-main); font-weight: 700; }
        .router-ticker { font-family: var(--font-mono); font-size: 0.78rem; color: #fff; display: flex; align-items: center; justify-content: space-between; }

        .btn-enter-terminal {
            position: relative; background: linear-gradient(135deg, var(--gold-main) 0%, #d4a007 100%);
            color: #080b10 !important; text-decoration: none !important; padding: 18px 24px; font-family: var(--font-display);
            font-size: 0.88rem; font-weight: 900; letter-spacing: 2px; border-radius: 12px;
            cursor: pointer; overflow: hidden; box-shadow: 0 0 25px var(--gold-glow);
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            display: flex; align-items: center; justify-content: center; gap: 12px; width: 100%; border: none;
        }
        .btn-enter-terminal::after {
            content: ''; position: absolute; top: -50%; left: -50%; width: 200%; height: 200%;
            background: linear-gradient(60deg, transparent, rgba(255, 255, 255, 0.4), transparent);
            transform: rotate(30deg); transition: 0.8s; opacity: 0;
        }
        .btn-enter-terminal:hover {
            transform: translateY(-3px) scale(1.02);
            box-shadow: 0 0 40px rgba(240, 185, 11, 0.7), 0 0 12px var(--cyan-neon); color: #000 !important;
        }
        .btn-enter-terminal:hover::after { opacity: 1; left: 100%; }

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
        .ticker-price { font-family: var(--font-mono); font-size: 0.88rem; font-weight: 800; color: #fff; transition: color 0.3s ease; }
        .ticker-change { font-family: var(--font-mono); font-size: 0.68rem; font-weight: 700; }
        .change-up { color: var(--green-up); }
        .change-down { color: var(--red-down); }
        .sparkline-canvas { width: 65px; height: 26px; }

        .bottom-deck { position: fixed; bottom: 25px; left: 50%; transform: translateX(-50%); z-index: 20; display: flex; align-items: center; gap: 10px; background: var(--bg-card); border: 1px solid var(--border-glass); border-radius: 30px; padding: 8px 18px; backdrop-filter: blur(20px); box-shadow: 0 10px 30px rgba(0,0,0,0.8); }
        .hub-chip { font-family: var(--font-mono); font-size: 0.68rem; font-weight: 700; color: var(--text-muted); padding: 6px 14px; border-radius: 20px; cursor: pointer; transition: all 0.25s ease; border: 1px solid transparent; }
        .hub-chip:hover, .hub-chip.active { color: #000; background: var(--gold-main); box-shadow: 0 0 15px var(--gold-glow); border-color: var(--gold-main); }
        .deck-divider { width: 1px; height: 18px; background: rgba(255, 255, 255, 0.15); }

        @media (max-width: 1024px) {
            .left-hero-panel { width: 320px; left: 20px; top: 90px; }
            .right-sidebar { width: 270px; right: 20px; top: 90px; }
            .hud-header { width: calc(100vw - 40px); }
        }
        @media (max-width: 768px) {
            .right-sidebar { display: none; }
            .left-hero-panel { width: calc(100vw - 40px); left: 20px; }
            .system-status-bar { display: none; }
            .bottom-deck { width: 92vw; overflow-x: auto; justify-content: flex-start; }
        }
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

        <button onclick="navigateToHub()" class="btn-enter-terminal" id="btn-enter-app">
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

        <div class="ticker-card" id="card-us100">
            <div class="ticker-info">
                <div class="ticker-symbol">US100</div>
                <div class="ticker-sub">Nasdaq 100 Index</div>
            </div>
            <canvas class="sparkline-canvas" id="spark-us100"></canvas>
            <div class="ticker-price-block">
                <div class="ticker-price" id="price-us100">21,240.10</div>
                <div class="ticker-change change-up" id="change-us100">+1.12%</div>
            </div>
        </div>

        <div class="ticker-card" id="card-us500">
            <div class="ticker-info">
                <div class="ticker-symbol">US500</div>
                <div class="ticker-sub">S&P 500 Index</div>
            </div>
            <canvas class="sparkline-canvas" id="spark-us500"></canvas>
            <div class="ticker-price-block">
                <div class="ticker-price" id="price-us500">5,992.40</div>
                <div class="ticker-change change-up" id="change-us500">+0.58%</div>
            </div>
        </div>

        <div class="ticker-card" id="card-dxy">
            <div class="ticker-info">
                <div class="ticker-symbol">DXY</div>
                <div class="ticker-sub">US Dollar Index</div>
            </div>
            <canvas class="sparkline-canvas" id="spark-dxy"></canvas>
            <div class="ticker-price-block">
                <div class="ticker-price" id="price-dxy">106.45</div>
                <div class="ticker-change change-down" id="change-dxy">-0.24%</div>
            </div>
        </div>

        <div class="ticker-card" id="card-btc">
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

        <div class="ticker-card" id="card-gold">
            <div class="ticker-info">
                <div class="ticker-symbol">XAU / USD</div>
                <div class="ticker-sub">Gold Spot</div>
            </div>
            <canvas class="sparkline-canvas" id="spark-gold"></canvas>
            <div class="ticker-price-block">
                <div class="ticker-price" id="price-gold">$2,688.30</div>
                <div class="ticker-change change-up" id="change-gold">+0.84%</div>
            </div>
        </div>
    </aside>

    <nav class="bottom-deck">
        <div class="hub-chip active" onclick="focusHub('ALL', this)">GLOBAL VIEW</div>
        <div class="deck-divider"></div>
        <div class="hub-chip" onclick="focusHub('NYC', this)">NEW YORK</div>
        <div class="hub-chip" onclick="focusHub('LON', this)">LONDON</div>
        <div class="hub-chip" onclick="focusHub('PAR', this)">PARIS</div>
        <div class="hub-chip" onclick="focusHub('DXB', this)">DUBAI</div>
        <div class="hub-chip" onclick="focusHub('SIN', this)">SINGAPORE</div>
        <div class="hub-chip" onclick="focusHub('HKG', this)">HONG KONG</div>
        <div class="hub-chip" onclick="focusHub('TYO', this)">TOKYO</div>
    </nav>

    <script>
        // Force le focus dans l'iframe dès l'ouverture pour capturer immédiatement la touche Entrée
        window.focus();
        document.addEventListener('click', () => { window.focus(); });

        // Redirection universelle vers la page Hub de Streamlit
        function navigateToHub() {
            window.top.location.search = '?page=hub';
        }

        const marketData = {
            us100: { price: 21240.10, change: 1.12 },
            us500: { price: 5992.40, change: 0.58 },
            dxy: { price: 106.45, change: -0.24 },
            gold: { price: 2688.30, change: 0.84 }
        };

        async function updateRealtimeBTC() {
            try {
                const response = await fetch('https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT');
                const data = await response.json();
                const price = parseFloat(data.lastPrice);
                const change = parseFloat(data.priceChangePercent);

                const priceEl = document.getElementById('price-btc');
                const changeEl = document.getElementById('change-btc');
                if (priceEl && changeEl) {
                    priceEl.textContent = '$' + price.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
                    changeEl.textContent = (change >= 0 ? '+' : '') + change.toFixed(2) + '%';
                    changeEl.className = 'ticker-change ' + (change >= 0 ? 'change-up' : 'change-down');
                }
            } catch (err) {
                console.warn('API Binance non disponible:', err);
            }
        }

        function simulateLiveMarketTicks() {
            Object.keys(marketData).forEach(key => {
                const item = marketData[key];
                const delta = (Math.random() - 0.49) * (item.price * 0.0004);
                item.price += delta;

                const priceEl = document.getElementById('price-' + key);
                if (priceEl) {
                    const prefix = (key === 'dxy') ? '' : ((key === 'gold') ? '$' : '');
                    priceEl.textContent = prefix + item.price.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
                    
                    priceEl.style.color = delta >= 0 ? '#0ecb81' : '#f6465d';
                    setTimeout(() => { priceEl.style.color = '#ffffff'; }, 350);
                }
            });
        }

        setInterval(updateRealtimeBTC, 2500);
        setInterval(simulateLiveMarketTicks, 1200);
        updateRealtimeBTC();

        const canvas = document.getElementById('webgl-canvas');
        const scene = new THREE.Scene();
        scene.fog = new THREE.FogExp2(0x080b10, 0.012);

        const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
        camera.position.set(0, 4, 28);

        const renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

        const globeGroup = new THREE.Group();
        const arcsGroup = new THREE.Group();
        const ringsGroup = new THREE.Group();
        const hubsGroup = new THREE.Group();
        const starsGroup = new THREE.Group();

        scene.add(starsGroup);
        scene.add(globeGroup);
        globeGroup.add(arcsGroup);
        globeGroup.add(ringsGroup);
        globeGroup.add(hubsGroup);

        const GLOBE_RADIUS = 8.5;

        (function createSpacefield() {
            const starGeo = new THREE.BufferGeometry();
            const count = 2000;
            const pos = new Float32Array(count * 3);
            for (let i = 0; i < count * 3; i += 3) {
                pos[i] = (Math.random() - 0.5) * 160;
                pos[i + 1] = (Math.random() - 0.5) * 160;
                pos[i + 2] = (Math.random() - 0.5) * 160;
            }
            starGeo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
            const starMat = new THREE.PointsMaterial({
                size: 0.15, color: 0x00f3ff, transparent: true, opacity: 0.4
            });
            starsGroup.add(new THREE.Points(starGeo, starMat));
        })();

        const coreGeo = new THREE.SphereGeometry(GLOBE_RADIUS * 0.98, 64, 64);
        const coreMat = new THREE.MeshBasicMaterial({ color: 0x0a101d, transparent: true, opacity: 0.94 });
        globeGroup.add(new THREE.Mesh(coreGeo, coreMat));

        const auraGeo = new THREE.SphereGeometry(GLOBE_RADIUS * 1.18, 64, 64);
        const auraMat = new THREE.ShaderMaterial({
            vertexShader: `
                varying vec3 vNormal;
                void main() {
                    vNormal = normalize(normalMatrix * normal);
                    gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
                }
            `,
            fragmentShader: `
                varying vec3 vNormal;
                void main() {
                    float intensity = pow(0.65 - dot(vNormal, vec3(0, 0, 1.0)), 2.5);
                    gl_FragColor = vec4(0.0, 0.95, 1.0, 1.0) * intensity * 0.5;
                }
            `,
            blending: THREE.AdditiveBlending, side: THREE.BackSide, transparent: true
        });
        scene.add(new THREE.Mesh(auraGeo, auraMat));

        const FINANCIAL_HUBS = [
            { id: 'NYC', name: 'New York', lat: 40.7128, lon: -74.0060, color: 0xf0b90b },
            { id: 'LON', name: 'London', lat: 51.5074, lon: -0.1278, color: 0x00f3ff },
            { id: 'PAR', name: 'Paris', lat: 48.8566, lon: 2.3522, color: 0x0ecb81 },
            { id: 'DXB', name: 'Dubai', lat: 25.2048, lon: 55.2708, color: 0xf0b90b },
            { id: 'SIN', name: 'Singapore', lat: 1.3521, lon: 103.8198, color: 0x00f3ff },
            { id: 'HKG', name: 'Hong Kong', lat: 22.3193, lon: 114.1694, color: 0x00f3ff },
            { id: 'TYO', name: 'Tokyo', lat: 35.6762, lon: 139.6503, color: 0xf0b90b }
        ];

        function latLonToVector3(lat, lon, radius = GLOBE_RADIUS) {
            const phi = (90 - lat) * (Math.PI / 180);
            const theta = (lon + 180) * (Math.PI / 180);
            const x = -(radius * Math.sin(phi) * Math.cos(theta));
            const z = radius * Math.sin(phi) * Math.sin(theta);
            const y = radius * Math.cos(phi);
            return new THREE.Vector3(x, y, z);
        }

        function createDottedGlobe() {
            const particleCount = 15000;
            const positions = new Float32Array(particleCount * 3);
            const colors = new Float32Array(particleCount * 3);

            const colorGold = new THREE.Color(0xf0b90b);
            const colorCyan = new THREE.Color(0x00f3ff);
            const colorDark = new THREE.Color(0x1a2638);

            function isLand(lat, lon) {
                if (lat > 15 && lat < 72 && lon > -168 && lon < -52) return true;
                if (lat > -56 && lat < 12 && lon > -82 && lon < -34) return true;
                if (lat > 35 && lat < 70 && lon > -10 && lon < 45) return true;
                if (lat > -35 && lat < 37 && lon > -18 && lon < 51) return true;
                if (lat > 5 && lat < 75 && lon > 45 && lon < 180) return true;
                if (lat > -44 && lat < -10 && lon > 112 && lon < 154) return true;
                return false;
            }

            for (let i = 0; i < particleCount; i++) {
                const u = Math.random();
                const v = Math.random();
                const lat = (Math.asin(2 * u - 1) * (180 / Math.PI));
                const lon = (v * 360 - 180);

                const vec = latLonToVector3(lat, lon, GLOBE_RADIUS);
                positions[i * 3] = vec.x;
                positions[i * 3 + 1] = vec.y;
                positions[i * 3 + 2] = vec.z;

                const land = isLand(lat, lon);
                let col = colorDark;
                if (land) col = Math.random() > 0.3 ? colorCyan : colorGold;

                colors[i * 3] = col.r;
                colors[i * 3 + 1] = col.g;
                colors[i * 3 + 2] = col.b;
            }

            const geo = new THREE.BufferGeometry();
            geo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
            geo.setAttribute('color', new THREE.BufferAttribute(colors, 3));

            const mat = new THREE.PointsMaterial({ size: 0.11, vertexColors: true, transparent: true, opacity: 0.85 });
            globeGroup.add(new THREE.Points(geo, mat));
        }
        createDottedGlobe();

        const hubObjects = [];
        const activeArcs = [];

        FINANCIAL_HUBS.forEach(hub => {
            const pos = latLonToVector3(hub.lat, hub.lon, GLOBE_RADIUS);
            const pinGeo = new THREE.SphereGeometry(0.18, 16, 16);
            const pinMat = new THREE.MeshBasicMaterial({ color: hub.color });
            const pinMesh = new THREE.Mesh(pinGeo, pinMat);
            pinMesh.position.copy(pos);
            hubsGroup.add(pinMesh);

            const ringBeaconGeo = new THREE.RingGeometry(0.2, 0.4, 32);
            const ringBeaconMat = new THREE.MeshBasicMaterial({ color: hub.color, side: THREE.DoubleSide, transparent: true, opacity: 0.8 });
            const ringBeacon = new THREE.Mesh(ringBeaconGeo, ringBeaconMat);
            ringBeacon.position.copy(pos);
            ringBeacon.lookAt(0, 0, 0);
            hubsGroup.add(ringBeacon);

            hubObjects.push({ ...hub, vec: pos, mesh: pinMesh, ring: ringBeacon });
        });

        function createFinancialArc(hubA, hubB) {
            const p1 = hubA.vec;
            const p2 = hubB.vec;
            const distance = p1.distanceTo(p2);
            const mid = new THREE.Vector3().addVectors(p1, p2).multiplyScalar(0.5);
            mid.normalize().multiplyScalar(mid.length() + distance * 0.35);

            const curve = new THREE.QuadraticBezierCurve3(p1, mid, p2);
            const points = curve.getPoints(64);
            const curveGeo = new THREE.BufferGeometry().setFromPoints(points);
            const curveMat = new THREE.LineBasicMaterial({ color: 0x00f3ff, transparent: true, opacity: 0.35 });
            arcsGroup.add(new THREE.Line(curveGeo, curveMat));

            const photonGeo = new THREE.SphereGeometry(0.12, 12, 12);
            const photonMat = new THREE.MeshBasicMaterial({ color: 0xf0b90b });
            const photon = new THREE.Mesh(photonGeo, photonMat);
            arcsGroup.add(photon);

            activeArcs.push({ curve, photon, speed: 0.15 + Math.random() * 0.2, progress: Math.random() });
        }

        const ROUTES = [['LON', 'NYC'], ['NYC', 'TYO'], ['LON', 'PAR'], ['PAR', 'DXB'], ['DXB', 'SIN'], ['SIN', 'HKG'], ['HKG', 'TYO'], ['LON', 'DXB']];
        ROUTES.forEach(([id1, id2]) => {
            const h1 = hubObjects.find(h => h.id === id1);
            const h2 = hubObjects.find(h => h.id === id2);
            if (h1 && h2) createFinancialArc(h1, h2);
        });

        let isDragging = false;
        let prevMousePos = { x: 0, y: 0 };
        let targetRotation = { x: 0.2, y: 0 };
        let currentRotation = { x: 0.2, y: 0 };

        window.addEventListener('mousedown', (e) => {
            if (e.target.tagName === 'CANVAS') {
                isDragging = true;
                prevMousePos = { x: e.clientX, y: e.clientY };
            }
        });

        window.addEventListener('mousemove', (e) => {
            if (isDragging) {
                targetRotation.y += (e.clientX - prevMousePos.x) * 0.005;
                targetRotation.x += (e.clientY - prevMousePos.y) * 0.005;
                prevMousePos = { x: e.clientX, y: e.clientY };
            }
        });

        window.addEventListener('mouseup', () => { isDragging = false; });
        window.addEventListener('wheel', (e) => {
            camera.position.z = Math.max(14, Math.min(45, camera.position.z + e.deltaY * 0.02));
        });

        window.focusHub = function(hubId, element) {
            document.querySelectorAll('.hub-chip').forEach(chip => chip.classList.remove('active'));
            element.classList.add('active');

            if (hubId === 'ALL') {
                targetRotation.x = 0.2; targetRotation.y = 0;
            } else {
                const hub = hubObjects.find(h => h.id === hubId);
                if (hub) {
                    targetRotation.x = (hub.lat * (Math.PI / 180));
                    targetRotation.y = - (hub.lon * (Math.PI / 180)) - Math.PI / 2;
                }
            }
        };

        function initSparklines() {
            const sparkCanvases = [
                { id: 'spark-us100', color: '#0ecb81' },
                { id: 'spark-us500', color: '#0ecb81' },
                { id: 'spark-dxy', color: '#f6465d' },
                { id: 'spark-btc', color: '#0ecb81' },
                { id: 'spark-gold', color: '#0ecb81' }
            ];

            sparkCanvases.forEach(cfg => {
                const cvs = document.getElementById(cfg.id);
                if (!cvs) return;
                const ctx = cvs.getContext('2d');
                cvs.width = 65; cvs.height = 26;
                const points = Array.from({ length: 10 }, () => 4 + Math.random() * 18);

                ctx.beginPath();
                ctx.strokeStyle = cfg.color;
                ctx.lineWidth = 2;
                points.forEach((val, idx) => {
                    const x = (idx / (points.length - 1)) * cvs.width;
                    const y = cvs.height - val;
                    if (idx === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
                });
                ctx.stroke();
            });
        }
        initSparklines();

        function updateClocks() {
            const now = new Date();
            document.getElementById('clock-paris').textContent = new Intl.DateTimeFormat('fr-FR', { timeZone: 'Europe/Paris', hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false }).format(now);
            document.getElementById('clock-ny').textContent = new Intl.DateTimeFormat('fr-FR', { timeZone: 'America/New_York', hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false }).format(now);
            document.getElementById('ping-val').textContent = Math.floor(12 + Math.random() * 6);
        }
        setInterval(updateClocks, 1000);
        updateClocks();

        // Écouteur pour la touche ENTRÉE
        window.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.code === 'Enter') {
                navigateToHub();
            } else if (e.code === 'KeyR') {
                targetRotation.x = 0.2; targetRotation.y = 0; camera.position.z = 28;
            }
        });

        const clock = new THREE.Clock();
        function animate() {
            requestAnimationFrame(animate);
            const delta = clock.getDelta();
            const time = clock.getElapsedTime();

            currentRotation.x += (targetRotation.x - currentRotation.x) * 0.05;
            currentRotation.y += (targetRotation.y - currentRotation.y) * 0.05;

            globeGroup.rotation.x = currentRotation.x;
            globeGroup.rotation.y = currentRotation.y + time * 0.03;
            ringsGroup.rotation.z = time * 0.05;
            starsGroup.rotation.y = time * 0.01;

            activeArcs.forEach(arc => {
                arc.progress = (arc.progress + delta * arc.speed) % 1.0;
                arc.photon.position.copy(arc.curve.getPoint(arc.progress));
            });

            hubObjects.forEach(hub => {
                const scale = 1 + Math.sin(time * 3 + hub.lat) * 0.25;
                hub.ring.scale.set(scale, scale, scale);
            });

            renderer.render(scene, camera);
        }

        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        });

        window.onload = function() { animate(); };
    </script>
</body>
</html>
    """

    st.components.v1.html(welcome_html_code, height=1000, scrolling=False)

# ==========================================
# PAGE 2 : PAGE VIERGE (HUB)
# ==========================================
elif st.session_state.page == "hub":
    
    st.markdown("""
        <style>
            header[data-testid="stHeader"] { visibility: hidden !important; }
            footer { visibility: hidden !important; }
            .stApp {
                background-color: #080b10 !important;
                color: #eaecef !important;
            }
        </style>
    """, unsafe_allow_html=True)

    if st.button("← Retour au Globe"):
        st.query_params["page"] = "welcome"
        st.session_state.page = "welcome"
        st.rerun()

    st.title("🚀 Page Vierge (Hub)")
    st.write("Tu es sur la page 2. Ton bouton et ta touche Entrée fonctionnent désormais correctement !")
