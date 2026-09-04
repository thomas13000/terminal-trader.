import streamlit as st
import streamlit.components.v1 as components

# ==========================================
# CONFIGURATION DE LA PAGE
# ==========================================
st.set_page_config(
    page_title="Terminal Trader Pro",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# GESTION DE LA NAVIGATION
# ==========================================
if "page" not in st.session_state:
    st.session_state.page = "welcome"

# ==========================================
# PAGE 1 : ACCUEIL HYPER-RÉALISTE
# ==========================================
if st.session_state.page == "welcome":
    
    # --- 1. LA BARRE SUPÉRIEURE (HTML/CSS) ---
    st.markdown("""
        <style>
        .block-container { padding-top: 1rem !important; }
        
        .top-bar {
            background: linear-gradient(135deg, #0d1117 0%, #161b22 100%);
            border: 1px solid #30363d;
            border-bottom: 2px solid #f0b90b;
            padding: 15px 30px;
            border-radius: 8px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 4px 20px rgba(0,0,0,0.5);
            margin-bottom: 10px;
        }
        .top-title {
            font-family: 'Courier New', Courier, monospace;
            font-size: 1.8rem;
            font-weight: 900;
            color: #ffffff;
            margin: 0;
            letter-spacing: 2px;
        }
        .top-title span { color: #f0b90b; }
        .top-stats {
            display: flex;
            gap: 20px;
            font-family: 'Courier New', Courier, monospace;
            color: #8b949e;
            align-items: center;
            font-size: 0.9rem;
        }
        .ms { color: #58a6ff; font-weight: bold; }
        .online-box {
            background: rgba(46, 160, 67, 0.15);
            border: 1px solid rgba(46, 160, 67, 0.4);
            color: #3fb950;
            padding: 6px 14px;
            border-radius: 20px;
            display: flex;
            align-items: center;
            gap: 8px;
            font-weight: bold;
        }
        .online-dot {
            width: 8px; height: 8px;
            background-color: #3fb950;
            border-radius: 50%;
            box-shadow: 0 0 10px #3fb950;
            animation: pulse 1.5s infinite;
        }
        @keyframes pulse { 0% {opacity: 1;} 50% {opacity: 0.3;} 100% {opacity: 1;} }
        </style>
        
        <div class="top-bar">
            <h1 class="top-title">TERMINAL TRADER <span>PRO</span></h1>
            <div class="top-stats">
                <div>SERVER LATENCY: <span class="ms">14 ms</span></div>
                <div class="online-box"><div class="online-dot"></div>ONLINE</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # --- 2. LE CŒUR DU DASHBOARD (GLOBE GÉANT + PANNEAUX) ---
    html_dashboard = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@700&display=swap');
      
      body { 
          margin: 0; background: transparent; color: #fff; 
          font-family: 'Share Tech Mono', monospace; 
          display: flex; justify-content: space-between; align-items: center; 
          height: 650px; /* Hauteur augmentée pour le gros globe */
          padding: 0 40px; 
          overflow: hidden;
          position: relative;
      }
      
      /* GLOBE TERRESTRE (Immense et centré en arrière-plan) */
      .globe-container { 
          position: absolute;
          top: 50%;
          left: 50%;
          transform: translate(-50%, -50%);
          z-index: 1; 
      }
      .globe { 
          width: 700px;  /* PLUS DE DEUX FOIS PLUS GRAND ! */
          height: 700px; 
          border-radius: 50%; 
          background: url('https://eoimages.gsfc.nasa.gov/images/imagerecords/55000/55167/earth_lights_lrg.jpg'); 
          background-size: cover;
          box-shadow: inset -60px -60px 100px rgba(0,0,0,0.95), 0 0 120px rgba(240, 185, 11, 0.25);
          animation: spin 45s linear infinite;
          opacity: 0.9;
      }
      @keyframes spin { from { background-position: 0 0; } to { background-position: 1500px 0; } }

      /* PANNEAUX (Gauche et Droite) */
      .panel { 
          background: rgba(13, 17, 23, 0.75); 
          border: 1px solid rgba(240, 185, 11, 0.4); 
          border-radius: 12px; padding: 30px; 
          box-shadow: 0 0 30px rgba(0,0,0,0.9); 
          backdrop-filter: blur(8px); 
          width: 320px; 
          z-index: 10; /* Toujours au-dessus du globe */
      }
      
      /* HORLOGES */
      .clock-title { font-family: 'Orbitron', sans-serif; color: #f0b90b; font-size: 1.2rem; margin-bottom: 5px; }
      .clock-time { font-size: 3.2rem; text-shadow: 0 0 20px rgba(255,255,255,0.25); margin-bottom: 30px; font-weight: bold;}
      
      /* ACTIFS FINANCIERS */
      .asset-row { 
          display: flex; justify-content: space-between; align-items: center; 
          padding: 15px 0; border-bottom: 1px solid rgba(255,255,255,0.08); 
      }
      .asset-row:last-child { border-bottom: none; }
      .asset-name { font-weight: bold; font-size: 1.4rem; color: #c9d1d9; }
      .asset-price { font-size: 1.4rem; text-align: right; transition: color 0.2s ease; font-weight: bold; }
      .asset-pct { font-size: 0.95rem; padding: 4px 8px; border-radius: 6px; text-align: right; margin-top: 4px; font-weight: bold;}
      
      /* COULEURS DES PRIX */
      .up { color: #0ecb81; text-shadow: 0 0 10px rgba(14,203,129,0.3); }
      .down { color: #f6465d; text-shadow: 0 0 10px rgba(246,70,93,0.3); }
      .bg-up { background: rgba(14, 203, 129, 0.15); color: #0ecb81; }
      .bg-down { background: rgba(246, 70, 93, 0.15); color: #f6465d; }
    </style>
    </head>
    <body>

    <!-- GLOBE (EN ARRIÈRE PLAN) -->
    <div class="globe-container">
        <div class="globe"></div>
    </div>

    <!-- GAUCHE : HORLOGES -->
    <div class="panel">
        <div class="clock-title">🇫🇷 PARIS</div>
        <div class="clock-time" id="paris">--:--:--</div>
        <div class="clock-title" style="margin-top: 10px;">🇺🇸 NEW YORK</div>
        <div class="clock-time" id="ny" style="margin-bottom: 0;">--:--:--</div>
    </div>

    <!-- DROITE : PRIX EN DIRECT -->
    <div class="panel">
        <div class="asset-row">
            <span class="asset-name">EUR/USD</span>
            <div><div class="asset-price" id="p-eur">1.0945</div><div class="asset-pct" id="pct-eur">+0.00%</div></div>
        </div>
        <div class="asset-row">
            <span class="asset-name">NASDAQ</span>
            <div><div class="asset-price" id="p-nas">19850.25</div><div class="asset-pct" id="pct-nas">+0.00%</div></div>
        </div>
        <div class="asset-row">
            <span class="asset-name">DXY</span>
            <div><div class="asset-price" id="p-dxy">104.20</div><div class="asset-pct" id="pct-dxy">-0.00%</div></div>
        </div>
        <div class="asset-row">
            <span class="asset-name">GOLD</span>
            <div><div class="asset-price" id="p-gold">2354.10</div><div class="asset-pct" id="pct-gold">+0.00%</div></div>
        </div>
    </div>

    <script>
    // 1. HORLOGES 
    function updateClocks() {
        const now = new Date();
        document.getElementById('paris').innerText = now.toLocaleTimeString('fr-FR', {timeZone: 'Europe/Paris'});
        document.getElementById('ny').innerText = now.toLocaleTimeString('en-US', {timeZone: 'America/New_York', hour12: false});
    }
    setInterval(updateClocks, 1000);
    updateClocks();

    // 2. MOTEUR DE PRIX
    const assets = {
        eur: { p: 1.0945, vol: 0.0003 },
        nas: { p: 19850.25, vol: 6.0 },
        dxy: { p: 104.20, vol: 0.05 },
        gold: { p: 2354.10, vol: 1.5 }
    };

    function updateAssets() {
        for (let key in assets) {
            let change = (Math.random() - 0.5) * assets[key].vol;
            let oldP = assets[key].p;
            let newP = oldP + change;
            assets[key].p = newP;
            
            let pct = (change / oldP) * 100;
            
            let elPrice = document.getElementById('p-' + key);
            let elPct = document.getElementById('pct-' + key);
            
            elPrice.innerText = newP.toFixed(key === 'eur' ? 4 : 2);
            let pctText = (pct >= 0 ? '+' : '') + pct.toFixed(3) + '%';
            elPct.innerText = pctText;
            
            if (change >= 0) {
                elPrice.className = 'asset-price up';
                elPct.className = 'asset-pct bg-up';
            } else {
                elPrice.className = 'asset-price down';
                elPct.className = 'asset-pct bg-down';
            }
        }
    }
    setInterval(updateAssets, 1500);
    updateAssets();
    </script>
    </body>
    </html>
    """
    
    # J'ai augmenté la hauteur du composant Streamlit à 650 pour accommoder le globe géant
    components.html(html_dashboard, height=650)

    # --- 3. BOUTON DE CONNEXION ---
    st.markdown("""
        <style>
        .stButton button {
            border: 2px solid #f0b90b !important;
            background-color: rgba(240, 185, 11, 0.05) !important;
            color: #f0b90b !important;
            font-size: 1.3rem !important;
            font-weight: bold;
            padding: 20px !important;
            border-radius: 8px !important;
            letter-spacing: 2px !important;
            transition: all 0.3s ease;
        }
        .stButton button:hover {
            background-color: #f0b90b !important;
            color: #000000 !important;
            box-shadow: 0 0 30px rgba(240, 185, 11, 0.6) !important;
        }
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        if st.button("DÉMARRER LE WORKSPACE 🚀", use_container_width=True):
            st.session_state.page = "hub"
            st.rerun()

# ==========================================
# PAGE 2 : HUB / DASHBOARD (Exemple)
# ==========================================
elif st.session_state.page == "hub":
    st.success("✅ Connexion au Terminal Pro réussie.")
    if st.button("← Retour Déconnexion"):
        st.session_state.page = "welcome"
        st.rerun()
