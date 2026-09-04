import base64
import datetime
import glob
import os
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

# ---------------------------------------------------------
# 1. CONFIGURATION STREAMLIT & STYLE PRO TRADER
# ---------------------------------------------------------
st.set_page_config(
    page_title="TERMINAL TRADER PRO",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
<style>
    .stApp {
        background-color: #0b0e11;
        color: #eaecef;
        font-family: 'Inter', sans-serif;
    }
    .header-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: #181a20;
        padding: 15px 25px;
        border-radius: 12px;
        border: 1px solid #2b313a;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.5);
    }
    .status-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(14, 203, 129, 0.12);
        color: #0ecb81;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 700;
        border: 1px solid rgba(14, 203, 129, 0.3);
    }
    .pulse-dot {
        width: 8px;
        height: 8px;
        background-color: #0ecb81;
        border-radius: 50%;
        box-shadow: 0 0 10px #0ecb81;
        animation: pulse-animation 1.5s infinite;
    }
    @keyframes pulse-animation {
        0% { transform: scale(0.95); opacity: 0.8; }
        50% { transform: scale(1.2); opacity: 1; }
        100% { transform: scale(0.95); opacity: 0.8; }
    }
    .metric-card {
        background: #1e2329;
        border: 1px solid #2b313a;
        border-radius: 10px;
        padding: 16px;
        text-align: center;
        transition: border-color 0.2s;
    }
    .metric-card:hover { border-color: #f0b90b; }
    .metric-title { font-size: 0.75rem; color: #848e9c; font-weight: 600; text-transform: uppercase; }
    .metric-val { font-size: 1.4rem; font-weight: 800; color: #ffffff; margin: 4px 0; }
    .val-up { color: #0ecb81; font-weight: 700; font-size: 0.85rem; }
    .val-down { color: #f6465d; font-weight: 700; font-size: 0.85rem; }
</style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# 2. SESSION STATE (ALERTES & PORTEFEUILLE)
# ---------------------------------------------------------
if "alerts" not in st.session_state:
    st.session_state.alerts = [
        {
            "id": 1,
            "symbol": "BTCUSDT",
            "target": 98500.0,
            "type": "Franchissement Haussier",
            "status": "Active",
            "created": "14:30:00",
        },
        {
            "id": 2,
            "symbol": "US100",
            "target": 21200.0,
            "type": "Franchissement Baissier",
            "status": "Active",
            "created": "10:15:00",
        },
    ]

if "capital" not in st.session_state:
    st.session_state.capital = 25000.0


# ---------------------------------------------------------
# 3. CHARGEMENT AUTOMATIQUE DU FICHIER AUDIO MP3
# ---------------------------------------------------------
def load_audio_b64():
    target_filename = "AC DC Back In Black (1).mp3"
    candidates = [target_filename, "acdc.mp3"]

    mp3_in_dir = glob.glob("*.mp3")
    for mp3 in mp3_in_dir:
        if mp3 not in candidates:
            candidates.append(mp3)

    for filename in candidates:
        if os.path.exists(filename):
            try:
                with open(filename, "rb") as f:
                    data = f.read()
                    if len(data) > 0:
                        return base64.b64encode(data).decode(), filename
            except Exception:
                continue

    return "", None


audio_b64, audio_filename_found = load_audio_b64()


# ---------------------------------------------------------
# 4. COMPOSANT ÉCRAN D'ACCUEIL 3D (GLOBE FUTURISTE + ARCS + AUDIO)
# ---------------------------------------------------------
def render_welcome_screen(audio_data):
    audio_src = f"data:audio/mp3;base64,{audio_data}" if audio_data else ""

    html_code = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&family=JetBrains+Mono:wght@500;700;800&display=swap">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; user-select: none; }}
            body, html {{ width: 100%; height: 100%; overflow: hidden; font-family: 'Inter', sans-serif; background: transparent; }}
            
            #welcome-screen-root {{
                position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
                background: radial-gradient(circle at center, #0a0e17 0%, #020305 100%);
                z-index: 999999; display: flex; align-items: center; justify-content: space-between;
                padding: 0 4vw; cursor: pointer; transition: opacity 0.7s cubic-bezier(0.4, 0, 0.2, 1);
            }}
            #canvas-3d {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; }}
            
            .left-panel {{
                position: relative; z-index: 2; text-align: center;
                background: rgba(11, 15, 23, 0.88); border: 1px solid rgba(240, 185, 11, 0.4);
                padding: 38px 32px; border-radius: 24px; backdrop-filter: blur(20px);
                box-shadow: 0 0 80px rgba(0, 0, 0, 0.95), inset 0 0 20px rgba(240, 185, 11, 0.08); width: 390px;
            }}
            .badge-live {{
                display: inline-flex; align-items: center; gap: 8px;
                font-family: 'JetBrains Mono', monospace; color: #f0b90b;
                font-size: 0.7rem; font-weight: 700; letter-spacing: 2px;
                background: rgba(240, 185, 11, 0.12); padding: 5px 14px; border-radius: 20px;
                border: 1px solid rgba(240, 185, 11, 0.3); margin-bottom: 12px;
            }}
            .dot-pulse {{ width: 8px; height: 8px; background-color: #089981; border-radius: 50%; box-shadow: 0 0 10px #089981; animation: pulse 1.5s infinite; }}
            @keyframes pulse {{ 0% {{ transform: scale(0.95); opacity: 0.8; }} 50% {{ transform: scale(1.2); opacity: 1; }} 100% {{ transform: scale(0.95); opacity: 0.8; }} }}
            
            .clock-main {{ font-family: 'JetBrains Mono', monospace; font-size: 3.8rem; font-weight: 800; color: #ffffff; margin: 4px 0; line-height: 1; text-shadow: 0 0 20px rgba(255,255,255,0.2); }}
            .clock-sub {{ font-size: 0.68rem; color: #787b86; letter-spacing: 1.8px; margin-bottom: 24px; font-weight: 600; }}
            
            .btn-enter {{
                background: linear-gradient(135deg, #f0b90b 0%, #d4a007 100%); color: #090a0f;
                border: none; padding: 16px 24px; font-size: 0.88rem; font-weight: 900;
                letter-spacing: 1.8px; border-radius: 10px; cursor: pointer; width: 100%;
                box-shadow: 0 4px 25px rgba(240, 185, 11, 0.4); transition: all 0.25s ease;
                display: flex; align-items: center; justify-content: center; gap: 10px;
            }}
            .btn-enter:hover {{ transform: translateY(-2px) scale(1.02); box-shadow: 0 6px 30px rgba(240, 185, 11, 0.6); }}
            
            .side-panel {{ position: relative; z-index: 2; display: flex; flex-direction: column; gap: 12px; width: 300px; }}
            .side-panel-header {{
                font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; font-weight: 800;
                color: #f0b90b; letter-spacing: 1.5px; background: rgba(19, 23, 34, 0.85);
                padding: 8px 14px; border-radius: 8px; border: 1px solid rgba(240, 185, 11, 0.25);
            }}
            .tv-card-wrapper {{
                background: rgba(13, 17, 26, 0.85); border: 1px solid rgba(255, 255, 255, 0.12);
                border-left: 3px solid #f0b90b; border-radius: 10px; padding: 6px 10px; backdrop-filter: blur(14px);
            }}
            .hint-bottom {{ margin-top: 12px; font-size: 0.65rem; color: #787b86; text-align: center; }}
        </style>
    </head>
    <body>
    <div id="welcome-screen-root" onclick="enterTerminalWithAudio()">
        <canvas id="canvas-3d"></canvas>

        <div class="left-panel" onclick="event.stopPropagation()">
            <div class="badge-live"><span class="dot-pulse"></span> FLUX GLOBAL CONNECTÉ</div>
            <div class="clock-main" id="clock-display">00:00:00</div>
            <div class="clock-sub">PARIS TIME — MARKET STANDBY</div>
            <button class="btn-enter" onclick="enterTerminalWithAudio()">
                ENTRER DANS LE TERMINAL ➔
            </button>
            <div class="hint-bottom">Appuyez sur <b style="color:#f0b90b;">ENTRÉE</b> ou cliquez pour démarrer</div>
        </div>

        <div class="side-panel" onclick="event.stopPropagation()">
            <div class="side-panel-header">⚡ INDICES EN DIRECT</div>
            <div class="tv-card-wrapper">
                <div class="tradingview-widget-container"><div class="tradingview-widget-container__widget"></div>
                <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
                {{ "symbol": "CAPITALCOM:US100", "width": "100%", "colorTheme": "dark", "isTransparent": true, "locale": "fr" }}
                </script></div>
            </div>
            <div class="tv-card-wrapper">
                <div class="tradingview-widget-container"><div class="tradingview-widget-container__widget"></div>
                <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
                {{ "symbol": "CAPITALCOM:US500", "width": "100%", "colorTheme": "dark", "isTransparent": true, "locale": "fr" }}
                </script></div>
            </div>
            <div class="tv-card-wrapper">
                <div class="tradingview-widget-container"><div class="tradingview-widget-container__widget"></div>
                <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
                {{ "symbol": "CAPITALCOM:DXY", "width": "100%", "colorTheme": "dark", "isTransparent": true, "locale": "fr" }}
                </script></div>
            </div>
        </div>
    </div>

    <script>
        const audioDataUri = "{audio_src}";
        
        // --- TIMING AUDIO (10s -> 35s) ---
        const startSecond = 10;
        const endSecond   = 35;
        const fadeSec     = 2.5;

        let audioObj = null;

        function enterTerminalWithAudio() {{
            if (audioDataUri && audioDataUri.length > 50) {{
                try {{
                    audioObj = new Audio(audioDataUri);
                    audioObj.volume = 0.85;
                    audioObj.currentTime = startSecond;

                    const playPromise = audioObj.play();
                    if (playPromise !== undefined) {{
                        playPromise.then(() => {{
                            const totalPlayMs = (endSecond - startSecond) * 1000;
                            const fadeStartMs = Math.max(0, totalPlayMs - (fadeSec * 1000));

                            setTimeout(() => {{
                                const intervalMs = 50;
                                const steps = (fadeSec * 1000) / intervalMs;
                                const volStep = audioObj.volume / steps;

                                const fadeInterval = setInterval(() => {{
                                    if (audioObj && audioObj.volume > volStep) {{
                                        audioObj.volume -= volStep;
                                    }} else {{
                                        if (audioObj) {{
                                            audioObj.volume = 0;
                                            audioObj.pause();
                                        }}
                                        clearInterval(fadeInterval);
                                    }}
                                }}, intervalMs);
                            }}, fadeStartMs);
                        }}).catch(e => console.log("Info lecture audio:", e));
                    }}
                }} catch(e) {{
                    console.log("Erreur audio:", e);
                }}
            }}
            dismissOverlay();
        }}

        // Raccourci clavier Touche Entrée / Espace
        window.addEventListener('keydown', (e) => {{
            if (e.key === 'Enter' || e.key === ' ') {{
                enterTerminalWithAudio();
            }}
        }});

        function dismissOverlay() {{
            const root = document.getElementById('welcome-screen-root');
            if (root) {{
                root.style.opacity = '0';
                root.style.pointerEvents = 'none';
                setTimeout(() => {{ root.style.display = 'none'; }}, 800);
            }}
            try {{
                if (window.parent && window.parent.document) {{
                    const iframes = window.parent.document.querySelectorAll('iframe');
                    iframes.forEach(iframe => {{
                        try {{
                            if (iframe.contentWindow === window) {{
                                iframe.style.pointerEvents = 'none';
                            }}
                        }} catch(e) {{}}
                    }});
                }}
            }} catch(e) {{}}
        }}

        function expandIframeToFullscreen() {{
            try {{
                if (window.parent && window.parent.document) {{
                    const iframes = window.parent.document.querySelectorAll('iframe');
                    iframes.forEach(iframe => {{
                        try {{
                            if (iframe.contentWindow === window) {{
                                iframe.style.position = 'fixed'; 
                                iframe.style.top = '0'; 
                                iframe.style.left = '0';
                                iframe.style.width = '100vw'; 
                                iframe.style.height = '100vh'; 
                                iframe.style.zIndex = '999999'; 
                                iframe.style.border = 'none';
                            }}
                        }} catch(e) {{}}
                    }});
                }}
            }} catch(e) {{}}
        }}
        expandIframeToFullscreen();

        function updateClock() {{
            const now = new Date();
            const timeStr = new Intl.DateTimeFormat('fr-FR', {{ timeZone: 'Europe/Paris', hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false }}).format(now);
            const el = document.getElementById('clock-display');
            if (el) el.textContent = timeStr;
        }}
        setInterval(updateClock, 1000); updateClock();

        // --------------------------------------------------
        // 🌐 MOTEUR 3D GLOBE + FLUX DE CAPITAUX (THREE.JS)
        // --------------------------------------------------
        let scene, camera, renderer, globeGroup, animParticles = [];
        let mouseX = 0, mouseY = 0, targetX = 0, targetY = 0;

        function latLongToVector3(lat, lon, radius) {{
            const phi = (90 - lat) * (Math.PI / 180);
            const theta = (lon + 180) * (Math.PI / 180);
            const x = -(radius * Math.sin(phi) * Math.cos(theta));
            const z = (radius * Math.sin(phi) * Math.sin(theta));
            const y = (radius * Math.cos(phi));
            return new THREE.Vector3(x, y, z);
        }}

        function init3DGlobe() {{
            const canvas = document.getElementById('canvas-3d');
            scene = new THREE.Scene();
            camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.z = 25;

            renderer = new THREE.WebGLRenderer({{ canvas: canvas, alpha: true, antialias: true }});
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

            globeGroup = new THREE.Group();
            scene.add(globeGroup);

            const R = 9.0; // Rayon du Globe

            // 1. Sphère Maillée Dorée
            const globeMesh = new THREE.Mesh(
                new THREE.SphereGeometry(R, 36, 36),
                new THREE.MeshBasicMaterial({{ color: 0xf0b90b, wireframe: true, transparent: true, opacity: 0.15 }})
            );
            globeGroup.add(globeMesh);

            // 2. Halo d'Atmosphère Néon (Glow)
            const glowMesh = new THREE.Mesh(
                new THREE.SphereGeometry(R * 1.08, 32, 32),
                new THREE.MeshBasicMaterial({{ color: 0xf0b90b, side: THREE.BackSide, transparent: true, opacity: 0.08 }})
            );
            globeGroup.add(glowMesh);

            // 3. Nuage de Points (Continents Virtuels)
            const ptsGeo = new THREE.BufferGeometry();
            const count = 2200;
            const ptsPos = new Float32Array(count * 3);
            for (let i = 0; i < count; i++) {{
                const u = Math.random(), v = Math.random();
                const theta = u * Math.PI * 2, phi = Math.acos(2 * v - 1);
                ptsPos[i * 3]     = (R + 0.05) * Math.sin(phi) * Math.cos(theta);
                ptsPos[i * 3 + 1] = (R + 0.05) * Math.sin(phi) * Math.sin(theta);
                ptsPos[i * 3 + 2] = (R + 0.05) * Math.cos(phi);
            }}
            ptsGeo.setAttribute('position', new THREE.BufferAttribute(ptsPos, 3));
            globeGroup.add(new THREE.Points(ptsGeo, new THREE.PointsMaterial({{ size: 0.15, color: 0x089981, transparent: true, opacity: 0.85 }})));

            // 4. Hubs Financiers Mondiaux (Capitales)
            const hubs = [
                {{ name: 'Paris', lat: 48.8566, lon: 2.3522 }},
                {{ name: 'London', lat: 51.5074, lon: -0.1278 }},
                {{ name: 'New York', lat: 40.7128, lon: -74.0060 }},
                {{ name: 'Tokyo', lat: 35.6762, lon: 139.6503 }},
                {{ name: 'Hong Kong', lat: 22.3193, lon: 114.1694 }},
                {{ name: 'Dubai', lat: 25.2048, lon: 55.2708 }}
            ];

            const hubCoords = hubs.map(h => latLongToVector3(h.lat, h.lon, R));

            // Marqueurs lumineux sur les hubs
            hubCoords.forEach(pos => {{
                const dot = new THREE.Mesh(
                    new THREE.SphereGeometry(0.22, 12, 12),
                    new THREE.MeshBasicMaterial({{ color: 0xf0b90b }})
                );
                dot.position.copy(pos);
                globeGroup.add(dot);
            }});

            // 5. Arcs de Capitaux 3D (Flux de trading intercontinentaux)
            const routes = [
                [0, 2], // Paris -> NY
                [1, 2], // Londres -> NY
                [2, 3], // NY -> Tokyo
                [3, 4], // Tokyo -> HK
                [4, 5], // HK -> Dubaï
                [5, 0]  // Dubaï -> Paris
            ];

            routes.forEach(r => {{
                const p1 = hubCoords[r[0]];
                const p2 = hubCoords[r[1]];

                // Point médian surélevé pour créer la courbe d'arc
                const mid = new THREE.Vector3().addVectors(p1, p2).multiplyScalar(0.5);
                const distance = p1.distanceTo(p2);
                mid.normalize().multiplyScalar(R + distance * 0.32);

                const curve = new THREE.QuadraticBezierCurve3(p1, mid, p2);
                const points = curve.getPoints(50);
                const curveGeo = new THREE.BufferGeometry().setFromPoints(points);

                const line = new THREE.Line(
                    curveGeo,
                    new THREE.LineBasicMaterial({{ color: 0xf0b90b, transparent: true, opacity: 0.45 }})
                );
                globeGroup.add(line);

                // Particule d'énergie qui voyage le long de l'arc
                const particle = new THREE.Mesh(
                    new THREE.SphereGeometry(0.18, 8, 8),
                    new THREE.MeshBasicMaterial({{ color: 0xffffff }})
                );
                globeGroup.add(particle);
                animParticles.push({{ mesh: particle, curve: curve, progress: Math.random() }});
            }});

            // 6. Anneau Équatorial de Surveillance
            const ring = new THREE.Mesh(
                new THREE.RingGeometry(R * 1.25, R * 1.26, 64),
                new THREE.MeshBasicMaterial({{ color: 0xf0b90b, side: THREE.DoubleSide, transparent: true, opacity: 0.3 }})
            );
            ring.rotation.x = Math.PI / 2.2;
            globeGroup.add(ring);

            // Écouteur de mouvements de souris pour effet Parallaxe
            document.addEventListener('mousemove', (e) => {{
                mouseX = (e.clientX - window.innerWidth / 2) * 0.0005;
                mouseY = (e.clientY - window.innerHeight / 2) * 0.0005;
            }});

            window.addEventListener('resize', () => {{
                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, window.innerHeight);
            }});

            animate();
        }}

        function animate() {{
            requestAnimationFrame(animate);

            // Rotation douce continue du globe
            if (globeGroup) {{
                globeGroup.rotation.y += 0.0025;
                
                // Effet Parallaxe lissé par rapport à la souris
                targetX += (mouseX - targetX) * 0.05;
                targetY += (mouseY - targetY) * 0.05;
                globeGroup.rotation.x = targetY;
                globeGroup.rotation.z = targetX * 0.5;
            }}

            // Animation des flux d'énergie le long des arcs
            animParticles.forEach(p => {{
                p.progress += 0.008;
                if (p.progress > 1) p.progress = 0;
                const pos = p.curve.getPoint(p.progress);
                p.mesh.position.copy(pos);
            }});

            renderer.render(scene, camera);
        }}

        window.onload = init3DGlobe;
    </script>
    </body>
    </html>
    """
    components.html(html_code, height=0)


# Lancement du composant au démarrage de la page
render_welcome_screen(audio_b64)


# ---------------------------------------------------------
# 5. BARRE LATÉRALE (SIDEBAR) & STATUT AUDIO
# ---------------------------------------------------------
with st.sidebar:
    st.image(
        "https://img.icons8.com/fluency/96/000000/financial-analytics.png",
        width=50,
    )
    st.title("⚡ TERMINAL PRO")
    st.caption("Version 4.2 — Institutional Grade")

    st.markdown("---")
    st.subheader("🎵 Statut Audio")
    if audio_filename_found:
        st.success(f"Fichier actif :\n`{audio_filename_found}`")
    else:
        st.warning("⚠️ acdc.mp3 introuvable")

    st.markdown("---")
    selected_asset = st.selectbox(
        "🎯 Actif Principal",
        [
            "BINANCE:BTCUSDT",
            "BINANCE:ETHUSDT",
            "CAPITALCOM:US100",
            "CAPITALCOM:US500",
            "FX:EURUSD",
            "TVC:GOLD",
        ],
        index=0,
    )

    timeframe = st.select_slider(
        "⏱️ Unité de Temps (UT)",
        options=["1", "5", "15", "60", "240", "D"],
        value="15",
    )

    st.markdown("---")
    st.session_state.capital = st.number_input(
        "Capital ($)", value=st.session_state.capital, step=1000.0
    )


# ---------------------------------------------------------
# 6. DASHBOARD TRADING COMPLET
# ---------------------------------------------------------
now_str = datetime.datetime.now().strftime("%H:%M:%S")

st.markdown(
    f"""
<div class="header-container">
    <div>
        <h2 style="margin:0; font-weight:900; color:#fff; font-family:'JetBrains Mono';">
            ⚡ TERMINAL TRADER PRO — <span style="color:#f0b90b;">{selected_asset.split(':')[-1]}</span>
        </h2>
        <span style="color:#848e9c; font-size:0.8rem;">Session En Cours | Heure Serveur : {now_str} UTC</span>
    </div>
    <div class="status-badge">
        <span class="pulse-dot"></span> DIRECT MARCHE
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# Bandeau de métriques marché
m1, m2, m3, m4, m5 = st.columns(5)
with m1:
    st.markdown(
        """<div class="metric-card"><div class="metric-title">BITCOIN</div><div class="metric-val">$96,480</div><div class="val-up">+3.42% ⚡</div></div>""",
        unsafe_allow_html=True,
    )
with m2:
    st.markdown(
        """<div class="metric-card"><div class="metric-title">NASDAQ (US100)</div><div class="metric-val">21,145</div><div class="val-up">+0.88% 📈</div></div>""",
        unsafe_allow_html=True,
    )
with m3:
    st.markdown(
        """<div class="metric-card"><div class="metric-title">S&P 500</div><div class="metric-val">5,980</div><div class="val-up">+0.45% 📈</div></div>""",
        unsafe_allow_html=True,
    )
with m4:
    st.markdown(
        """<div class="metric-card"><div class="metric-title">EUR / USD</div><div class="metric-val">1.0482</div><div class="val-down">-0.21% 📉</div></div>""",
        unsafe_allow_html=True,
    )
with m5:
    st.markdown(
        """<div class="metric-card"><div class="metric-title">OR (GOLD)</div><div class="metric-val">$2,685</div><div class="val-up">+0.62% 📈</div></div>""",
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 7. ONGLETS ET OUTILS DE TRADING
# ---------------------------------------------------------
tab_chart, tab_alerts, tab_news, tab_calc = st.tabs(
    [
        "📈 Graphique & Carnet d'Ordres",
        "🚨 Système d'Alertes",
        "📰 Actualités & Macro",
        "🧮 Calculateur de Risque",
    ]
)

# TAB 1 : Graphique TradingView & Orderbook
with tab_chart:
    col_chart, col_side = st.columns([3, 1])

    with col_chart:
        st.subheader("📊 Graphique Temps Réel TradingView")
        tv_chart_code = f"""
        <div class="tradingview-widget-container" style="height:580px;width:100%;">
          <div id="tradingview_advanced" style="height:580px;width:100%;"></div>
          <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
          <script type="text/javascript">
          new TradingView.widget({{
            "autosize": true,
            "symbol": "{selected_asset}",
            "interval": "{timeframe}",
            "timezone": "Europe/Paris",
            "theme": "dark",
            "style": "1",
            "locale": "fr",
            "toolbar_bg": "#f1f3f6",
            "enable_publishing": false,
            "hide_side_toolbar": false,
            "allow_symbol_change": true,
            "container_id": "tradingview_advanced"
          }});
          </script>
        </div>
        """
        components.html(tv_chart_code, height=590)

    with col_side:
        st.subheader("⚡ Analyse Technique")
        tv_tech_code = f"""
        <div class="tradingview-widget-container">
          <div class="tradingview-widget-container__widget"></div>
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-technical-analysis.js" async>
          {{
            "interval": "15m",
            "width": "100%",
            "isTransparent": true,
            "height": 280,
            "symbol": "{selected_asset}",
            "showIntervalTabs": true,
            "displayMode": "single",
            "locale": "fr",
            "colorTheme": "dark"
          }}
          </script>
        </div>
        """
        components.html(tv_tech_code, height=290)

        st.subheader("📖 Carnet d'Ordres")
        st.markdown(
            """
        <div style="font-family:'JetBrains Mono', monospace; font-size:0.82rem; background:#181a20; padding:12px; border-radius:8px; border:1px solid #2b313a;">
            <div style="color:#848e9c; font-size:0.7rem; margin-bottom:6px; display:flex; justify-content:space-between;"><span>PRIX ($)</span><span>VOLUME</span></div>
            <div style="color:#f6465d; display:flex; justify-content:space-between;"><span>96495.0</span><span>2.50 BTC</span></div>
            <div style="color:#f6465d; display:flex; justify-content:space-between;"><span>96490.0</span><span>1.80 BTC</span></div>
            <div style="color:#f6465d; display:flex; justify-content:space-between;"><span>96485.0</span><span>0.90 BTC</span></div>
            <hr style="border-color:#2b313a; margin:6px 0;">
            <div style="color:#0ecb81; display:flex; justify-content:space-between;"><span>96475.0</span><span>1.25 BTC</span></div>
            <div style="color:#0ecb81; display:flex; justify-content:space-between;"><span>96470.0</span><span>2.10 BTC</span></div>
            <div style="color:#0ecb81; display:flex; justify-content:space-between;"><span>96465.0</span><span>0.85 BTC</span></div>
        </div>
        """,
            unsafe_allow_html=True,
        )

# TAB 2 : Alertes
with tab_alerts:
    st.subheader("🚨 Gestionnaire d'Alertes de Prix")
    c_add, c_list = st.columns([1, 2])

    with c_add:
        with st.form("add_alert_form", clear_on_submit=True):
            sym = st.selectbox(
                "Actif", ["BTCUSDT", "ETHUSDT", "US100", "EURUSD", "GOLD"]
            )
            target = st.number_input("Prix Cible", value=98000.0, step=10.0)
            atype = st.selectbox(
                "Condition",
                ["Franchissement Haussier", "Franchissement Baissier"],
            )

            if st.form_submit_button("🔔 Ajouter l'Alerte"):
                st.session_state.alerts.append(
                    {
                        "id": len(st.session_state.alerts) + 1,
                        "symbol": sym,
                        "target": target,
                        "type": atype,
                        "status": "Active",
                        "created": datetime.datetime.now().strftime("%H:%M:%S"),
                    }
                )
                st.success("Alerte enregistrée avec succès !")

        if st.button("🔊 Tester Sonnette d'Alerte"):
            st.toast("🚨 TEST ALERTE : Niveau de prix atteint !")
            st.balloons()

    with c_list:
        if st.session_state.alerts:
            df = pd.DataFrame(st.session_state.alerts)
            st.dataframe(df, use_container_width=True, hide_index=True)
            if st.button(" Effacer toutes les alertes"):
                st.session_state.alerts = []
                st.rerun()

# TAB 3 : News
with tab_news:
    col_n1, col_n2 = st.columns(2)
    with col_n1:
        st.subheader("📰 Fil d'Actualités Financières")
        components.html(
            """
        <div class="tradingview-widget-container">
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-timeline.js" async>
          {"feedMode": "all_symbols", "colorTheme": "dark", "isTransparent": true, "width": "100%", "height": 550, "locale": "fr"}
          </script>
        </div>""",
            height=560,
        )

    with col_n2:
        st.subheader("📅 Calendrier Économique Macro")
        components.html(
            """
        <div class="tradingview-widget-container">
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>
          {"colorTheme": "dark", "isTransparent": true, "width": "100%", "height": 550, "locale": "fr"}
          </script>
        </div>""",
            height=560,
        )

# TAB 4 : Calculateur
with tab_calc:
    st.subheader("🧮 Calculateur de Management du Risque")
    ca, cb = st.columns(2)
    with ca:
        cap = st.number_input(
            "Capital ($)", value=st.session_state.capital, key="calc_cap"
        )
        risk = st.slider("Risque par Trade (%)", 0.25, 5.0, 1.0)
        entry = st.number_input("Prix d'Entrée ($)", value=96500.0)
        sl = st.number_input("Stop Loss ($)", value=95200.0)
        tp = st.number_input("Take Profit ($)", value=99500.0)

    with cb:
        risk_val = cap * (risk / 100.0)
        dist_sl = abs(entry - sl)
        dist_tp = abs(tp - entry)
        pos_size = risk_val / dist_sl if dist_sl > 0 else 0
        rr = dist_tp / dist_sl if dist_sl > 0 else 0

        st.metric("Risque en Dollar ($)", f"{risk_val:.2f} $")
        st.metric("Taille de Position Recommandée", f"{pos_size:.4f} Unités")
        st.metric("Ratio Risque / Récompense (R:R)", f"1 : {rr:.2f}")
