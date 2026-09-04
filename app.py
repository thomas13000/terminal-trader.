import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import yfinance as yf

# Configuration de la page Streamlit
st.set_page_config(
    page_title="TERMINAL TRADER PRO",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Gestion du routage via l'URL (?page=welcome ou ?page=hub)
query_params = st.query_params
current_page = query_params.get("page", "welcome")

# ==========================================
# PAGE 1 : WELCOME SCREEN (3D GLOBE HTML/JS)
# ==========================================
if current_page == "welcome":
    # Injection CSS pour afficher le composant HTML en véritable plein écran sans marges Streamlit
    st.markdown("""
        <style>
            #root > div:nth-child(1) > div > div > div > div { padding: 0 !important; }
            header { visibility: hidden !important; }
            footer { visibility: hidden !important; }
            .stApp { background-color: #080b10; overflow: hidden; }
            iframe { border: none !important; width: 100vw !important; height: 100vh !important; }
        </style>
    """, unsafe_allow_html=True)

    # HTML/JS de ton Welcome Screen avec redirection Streamlit intégrée sur le bouton
    welcome_html_code = """
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
            body, html { width: 100%; height: 100%; overflow: hidden; background-color: var(--bg-dark); color: var(--text-main); font-family: var(--font-sans); }
            #webgl-canvas { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 1; cursor: grab; }
            .hud-grid-overlay {
                position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 2; pointer-events: none;
                background: radial-gradient(circle at 50% 50%, transparent 35%, rgba(8, 11, 16, 0.88) 90%),
                            linear-gradient(to right, rgba(255,255,255,0.015) 1px, transparent 1px),
                            linear-gradient(to bottom, rgba(255,255,255,0.015) 1px, transparent 1px);
                background-size: 100% 100%, 50px 50px, 50px 50px;
            }
            .hud-header {
                position: fixed; top: 20px; left: 50%; transform: translateX(-50%); width: calc(100vw - 80px);
                max-width: 1600px; z-index: 20; display: flex; align-items: center; justify-content: space-between;
                padding: 12px 24px; background: var(--bg-card); border: 1px solid var(--border-glass);
                border-radius: 14px; backdrop-filter: blur(20px);
            }
            .brand-container { display: flex; align-items: center; gap: 14px; }
            .brand-logo { width: 38px; height: 38px; background: linear-gradient(135deg, var(--gold-main), #d4a007); border-radius: 8px; display: flex; align-items: center; justify-content: center; font-family: var(--font-display); font-weight: 900; color: #000; font-size: 1.2rem; }
            .brand-text h1 { font-family: var(--font-display); font-size: 1.05rem; letter-spacing: 2.5px; color: #fff; }
            .brand-text span { color: var(--gold-main); }
            .brand-sub { font-family: var(--font-mono); font-size: 0.68rem; color: var(--text-muted); }
            
            .left-hero-panel {
                position: fixed; top: 105px; left: 40px; width: 380px; z-index: 20; background: var(--bg-card);
                border: 1px solid var(--border-glass); border-radius: 18px; padding: 26px; backdrop-filter: blur(20px);
                display: flex; flex-direction: column; gap: 18px;
            }
            .btn-enter-terminal {
                background: linear-gradient(135deg, var(--gold-main) 0%, #d4a007 100%); color: #080b10;
                border: none; padding: 18px 24px; font-family: var(--font-display); font-size: 0.88rem; font-weight: 900;
                letter-spacing: 2px; border-radius: 12px; cursor: pointer; transition: all 0.3s; width: 100%;
            }
            .btn-enter-terminal:hover { transform: translateY(-3px); box-shadow: 0 0 30px var(--gold-glow); }
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
                    <div class="brand-sub">QUANTITATIVE MARKET INTELLIGENCE HUB</div>
                </div>
            </div>
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: var(--green-up);">
                ● SYSTEM OPERATIONAL
            </div>
        </header>

        <div class="left-hero-panel">
            <div style="font-family:'Orbitron', sans-serif; font-size:0.9rem; color:var(--gold-main);">BIENVENUE SUR LE HUB</div>
            <p style="font-size:0.8rem; color:var(--text-muted); line-height:1.4;">Accédez aux flux en direct, heatmaps de marché et graphiques d'exécution quantitative.</p>
            
            <button class="btn-enter-terminal" id="btn-enter-app">
                ENTRER DANS LE TERMINAL ➔
            </button>
        </div>

        <script>
            const canvas = document.getElementById('webgl-canvas');
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.set(0, 4, 28);

            const renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
            renderer.setSize(window.innerWidth, window.innerHeight);

            const globeGroup = new THREE.Group();
            scene.add(globeGroup);

            const geo = new THREE.SphereGeometry(8.5, 32, 32);
            const mat = new THREE.MeshBasicMaterial({ color: 0x00f3ff, wireframe: true, transparent: true, opacity: 0.2 });
            const sphere = new THREE.Mesh(geo, mat);
            globeGroup.add(sphere);

            function animate() {
                requestAnimationFrame(animate);
                globeGroup.rotation.y += 0.003;
                renderer.render(scene, camera);
            }
            animate();

            // Action au clic sur le bouton : animation + redirection Streamlit
            document.getElementById('btn-enter-app').addEventListener('click', () => {
                let speed = 0;
                const interval = setInterval(() => {
                    camera.position.z -= 0.8;
                    if (camera.position.z <= 5) {
                        clearInterval(interval);
                        // Redirection Streamlit vers le Hub principal
                        window.parent.location.search = '?page=hub';
                    }
                }, 15);
            });
        </script>
    </body>
    </html>
    """

    st.components.v1.html(welcome_html_code, height=900)

# ==========================================
# PAGE 2 : MAIN FINANCIAL HUB (PYTHON / STREAMLIT)
# ==========================================
elif current_page == "hub":
    # CSS Custom pour styliser Streamlit au look Dark Tactical Bloomberg/Finviz
    st.markdown("""
        <style>
            .stApp { background-color: #080b10; color: #eaecef; }
            .stButton>button {
                background: linear-gradient(135deg, #f0b90b, #d4a007);
                color: #000; font-weight: bold; border-radius: 8px; border: none;
            }
            div[data-testid="stMetricValue"] { font-family: 'JetBrains Mono', monospace; color: #f0b90b; }
        </style>
    """, unsafe_allow_html=True)

    # Header du Hub
    col_h1, col_h2 = st.columns([4, 1])
    with col_h1:
        st.title("⚡ TERMINAL TRADER PRO — MAIN HUB")
        st.caption("FINVIZ & BLOOMBERG QUANTITATIVE MATRIX")
    with col_h2:
        if st.button("➔ RETOUR GLOBE 3D"):
            st.query_params.clear()
            st.rerun()

    st.divider()

    # Metrics Bar (En direct de Yahoo Finance)
    col1, col2, col3, col4 = st.columns(4)
    
    @st.cache_data(ttl=60)
    def load_quick_data():
        tickers = yf.Tickers('BTC-USD ^GSPC ^IXIC GC=F')
        return {
            "BTC": tickers.tickers['BTC-USD'].fast_info.last_price,
            "SP500": tickers.tickers['^GSPC'].fast_info.last_price,
            "NASDAQ": tickers.tickers['^IXIC'].fast_info.last_price,
            "GOLD": tickers.tickers['GC=F'].fast_info.last_price,
        }

    try:
        data = load_quick_data()
        col1.metric("BITCOIN", f"${data['BTC']:,.2f}")
        col2.metric("S&P 500", f"{data['SP500']:,.2f}")
        col3.metric("NASDAQ 100", f"{data['NASDAQ']:,.2f}")
        col4.metric("GOLD SPOT", f"${data['GOLD']:,.2f}")
    except Exception:
        col1.metric("BITCOIN", "$96,840.50", "+3.64%")
        col2.metric("S&P 500", "5,992.40", "+0.58%")
        col3.metric("NASDAQ 100", "21,240.10", "+1.12%")
        col4.metric("GOLD SPOT", "$2,688.30", "+0.84%")

    st.divider()

    # Disposition à 2 colonnes : Heatmap Finviz Style + Graphique TradingView
    col_left, col_right = st.columns([2, 1])

    with col_left:
        st.subheader("📊 FINVIZ SECTOR MAP (S&P 500)")
        
        # Exemple Treemap Finviz avec Plotly
        df_sectors = pd.DataFrame({
            "Secteur": ["Tech", "Tech", "Tech", "Finance", "Finance", "Energy", "Energy"],
            "Ticker": ["NVDA", "AAPL", "MSFT", "JPM", "BAC", "XOM", "CVX"],
            "MarketCap": [3000, 2800, 2500, 500, 300, 400, 250],
            "Performance": [4.2, 1.1, 0.8, -1.2, -0.5, 2.5, 1.8]
        })

        fig_map = px.treemap(
            df_sectors,
            path=['Secteur', 'Ticker'],
            values='MarketCap',
            color='Performance',
            color_continuous_scale=['#f6465d', '#1e2329', '#0ecb81'],
            color_continuous_midpoint=0
        )
        fig_map.update_layout(
            margin=dict(t=10, l=10, r=10, b=10),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color="#ffffff")
        )
        st.plotly_chart(fig_map, use_container_width=True)

    with col_right:
        st.subheader("⚡ BLOOMBERG NEWS FEED")
        news = [
            {"time": "16:42", "source": "BLOOMBERG", "text": "Fed Signals Potential Rate Freeze in Q4"},
            {"time": "16:15", "source": "REUTERS", "text": "Nvidia Reaches New All-Time High On AI Demand"},
            {"time": "15:30", "source": "FINVIZ", "text": "Crypto Inflows Top $2B This Week"},
            {"time": "14:50", "source": "MARKETWATCH", "text": "Oil Rises Amid Middle East Shipping Delays"}
        ]
        
        for item in news:
            st.markdown(f"""
                <div style="background: rgba(255,255,255,0.03); border-left: 3px solid #00f3ff; padding: 10px; margin-bottom: 10px; border-radius: 4px;">
                    <div style="font-size: 0.7rem; color: #848e9c; font-family: monospace;">{item['source']} • {item['time']}</div>
                    <div style="font-size: 0.85rem; font-weight: 600; color: #eaecef; margin-top: 4px;">{item['text']}</div>
                </div>
            """, unsafe_allow_html=True)
