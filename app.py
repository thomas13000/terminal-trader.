import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Terminal Trader Pro",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "page" not in st.session_state:
    st.session_state.page = "welcome"

# ==========================================
# PAGE 1 : WELCOME / AUTH SCREEN
# ==========================================
if st.session_state.page == "welcome":
    st.markdown("""
        <style>
        html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
            overflow: hidden !important;
            height: 100vh !important;
            background-color: #0d1117;
        }
        header {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        .block-container { 
            padding-top: 0.5rem !important; 
            padding-bottom: 0.2rem !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
            max-width: 100% !important;
            height: 100vh !important;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            overflow: hidden !important;
        }
        
        .top-bar {
            background: linear-gradient(135deg, #0d1117 0%, #161b22 100%);
            border: 1px solid #30363d;
            border-bottom: 1px solid rgba(240, 185, 11, 0.6);
            padding: 8px 20px;
            border-radius: 4px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-shrink: 0;
        }
        .top-title {
            font-family: 'Courier New', Courier, monospace;
            font-size: 1.4rem;
            font-weight: bold;
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
            font-size: 0.85rem;
        }
        .ms { color: #58a6ff; font-weight: bold; }
        .online-box {
            color: #3fb950;
            display: flex;
            align-items: center;
            gap: 8px;
            font-weight: bold;
        }
        .online-dot {
            width: 8px; height: 8px;
            background-color: #3fb950;
            border-radius: 50%;
            box-shadow: 0 0 8px #3fb950;
            animation: pulse 1.5s infinite;
        }
        @keyframes pulse { 0% {opacity: 1;} 50% {opacity: 0.3;} 100% {opacity: 1;} }
        </style>
        
        <div class="top-bar">
            <h1 class="top-title">TERMINAL TRADER <span>PRO</span></h1>
            <div class="top-stats">
                <div>LATENCY: <span class="ms">14 ms</span></div>
                <div class="online-box"><div class="online-dot"></div>SYS. ONLINE</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    components.html("""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@700&display=swap');
      
      body { 
          margin: 0; background: transparent; color: #fff; 
          font-family: 'Share Tech Mono', monospace; 
          display: flex; justify-content: space-between; align-items: center; 
          height: 600px; 
          padding: 0 20px; 
          overflow: hidden;
          position: relative;
      }
      
      .globe-container { 
          position: absolute; top: 54%; left: 50%;
          transform: translate(-50%, -50%); z-index: 1; 
          pointer-events: none;
      }
      .globe { 
          width: 530px; height: 530px; border-radius: 50%; 
          background: url('https://eoimages.gsfc.nasa.gov/images/imagerecords/55000/55167/earth_lights_lrg.jpg'); 
          background-size: cover;
          box-shadow: inset -50px -50px 80px rgba(0,0,0,0.95), 0 0 50px rgba(240, 185, 11, 0.15); 
          animation: spin 45s linear infinite;
          opacity: 0.85;
      }
      @keyframes spin { from { background-position: 0 0; } to { background-position: 1500px 0; } }

      .panel { 
          background: rgba(13, 17, 23, 0.85); 
          border: 1px solid rgba(240, 185, 11, 0.25); 
          border-radius: 4px; padding: 20px; 
          box-shadow: 0 0 25px rgba(0,0,0,0.9); 
          backdrop-filter: blur(6px); width: 280px; z-index: 10;
      }
      
      .clock-title { font-family: 'Orbitron', sans-serif; color: #848e9c; font-size: 0.85rem; margin-bottom: 2px; }
      .clock-time { font-size: 2.3rem; color: #f0b90b; text-shadow: 0 0 10px rgba(240,185,11,0.2); margin-bottom: 15px; font-weight: bold;}
    </style>
    </head>
    <body>

    <div class="globe-container"><div class="globe"></div></div>

    <div class="panel">
        <div class="clock-title">PARIS (CET)</div>
        <div class="clock-time" id="paris">--:--:--</div>
        <div class="clock-title">NEW YORK (EST)</div>
        <div class="clock-time" id="ny" style="margin-bottom: 0;">--:--:--</div>
    </div>

    <div class="panel" style="padding: 10px 15px;">
        <div class="tradingview-widget-container" style="margin-bottom: 2px;">
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
          {"symbol": "OANDA:EURUSD", "width": "100%", "colorTheme": "dark", "isTransparent": true, "locale": "fr"}
          </script>
        </div>
        <div class="tradingview-widget-container" style="margin-bottom: 2px;">
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
          {"symbol": "CAPITALCOM:US100", "width": "100%", "colorTheme": "dark", "isTransparent": true, "locale": "fr"}
          </script>
        </div>
        <div class="tradingview-widget-container" style="margin-bottom: 2px;">
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
          {"symbol": "CAPITALCOM:DXY", "width": "100%", "colorTheme": "dark", "isTransparent": true, "locale": "fr"}
          </script>
        </div>
        <div class="tradingview-widget-container">
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
          {"symbol": "OANDA:XAUUSD", "width": "100%", "colorTheme": "dark", "isTransparent": true, "locale": "fr"}
          </script>
        </div>
    </div>

    <script>
    function updateClocks() {
        const now = new Date();
        document.getElementById('paris').innerText = now.toLocaleTimeString('fr-FR', {timeZone: 'Europe/Paris'});
        document.getElementById('ny').innerText = now.toLocaleTimeString('en-US', {timeZone: 'America/New_York', hour12: false});
    }
    setInterval(updateClocks, 1000); updateClocks();
    </script>
    </body>
    </html>
    """, height=600)

    st.markdown("""
        <style>
        div.stButton {
            display: flex;
            justify-content: center;
            margin-top: -20px; 
            margin-bottom: 2px;
            flex-shrink: 0;
        }
        div.stButton > button {
            background-color: transparent !important;
            color: #848e9c !important; 
            border: 1px solid rgba(240, 185, 11, 0.3) !important; 
            font-family: 'Courier New', Courier, monospace !important;
            font-size: 0.9rem !important;
            font-weight: 600 !important;
            letter-spacing: 4px !important; 
            padding: 8px 35px !important;
            border-radius: 2px !important; 
            transition: all 0.4s ease !important;
            text-transform: uppercase !important;
            width: auto !important; 
        }
        div.stButton > button:hover {
            background-color: rgba(240, 185, 11, 0.05) !important;
            border: 1px solid #f0b90b !important; 
            color: #f0b90b !important; 
            box-shadow: 0 0 15px rgba(240, 185, 11, 0.15) !important; 
        }
        </style>
    """, unsafe_allow_html=True)

    if st.button("CONNECT SYSTEM"):
        st.session_state.page = "hub"
        st.rerun()

# ==========================================
# PAGE 2 : TRADING HUB & ANALYTICS DASHBOARD
# ==========================================
elif st.session_state.page == "hub":
    st.markdown("""
        <style>
        html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
            background-color: #0d1117;
            color: #f0f6fc;
            font-family: 'Share Tech Mono', monospace, sans-serif;
        }
        header {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        .hub-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #30363d;
            padding-bottom: 10px;
            margin-bottom: 15px;
        }
        .hub-title {
            font-family: 'Orbitron', sans-serif;
            font-size: 1.2rem;
            color: #f0b90b;
            letter-spacing: 1px;
        }
        .metric-card {
            background: rgba(13, 17, 23, 0.9);
            border: 1px solid #30363d;
            border-radius: 6px;
            padding: 12px 15px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.5);
        }
        </style>
    """, unsafe_allow_html=True)

    # Top Navigation / Control Bar inside Hub
    col_h1, col_h2 = st.columns([4, 1])
    with col_h1:
        st.markdown('<div class="hub-title">⚡ TERMINAL TRADER PRO // EXECUTIVE HUB</div>', unsafe_allow_html=True)
    with col_h2:
        if st.button("← DISCONNECT SESSION"):
            st.session_state.page = "welcome"
            st.rerun()

    # Metrics Row
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric(label="BALANCE ACTUELLE", value="$124,580.40", delta="+2.4%")
    with m2:
        st.metric(label="PNL OUVERT (24H)", value="+$3,420.15", delta="+1.12%")
    with m3:
        st.metric(label="EXPOSITION MARGIN", value="42.8%", delta="-3.2%")
    with m4:
        st.metric(label="WIN RATE", value="68.4%", delta="+4.1%")

    st.markdown("---")

    # Main Sections (Tabs for multi-view dashboard)
    tab1, tab2, tab3 = st.tabs(["📈 GRAPHIQUES & MARCHÉS", "⚡ EXÉCUTION D'ORDRES", "📊 ANALYSE DE PORTEFEUILLE"])

    with tab1:
        col_chart1, col_chart2 = st.columns(2)
        with col_chart1:
            st.markdown("### **DXY Live Overview**")
            components.html("""
            <div class="tradingview-widget-container">
              <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
              {"symbol": "CAPITALCOM:DXY", "width": "100%", "colorTheme": "dark", "isTransparent": true, "locale": "fr"}
              </script>
            </div>
            """, height=180)
        with col_chart2:
            st.markdown("### **XAUUSD (Gold) Overview**")
            components.html("""
            <div class="tradingview-widget-container">
              <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
              {"symbol": "OANDA:XAUUSD", "width": "100%", "colorTheme": "dark", "isTransparent": true, "locale": "fr"}
              </script>
            </div>
            """, height=180)

    with tab2:
        st.markdown("### ⚡ **Panel d'Ordre Rapide**")
        col_o1, col_o2, col_o3 = st.columns(3)
        with col_o1:
            st.selectbox("Actif cible", ["CAPITALCOM:DXY", "OANDA:EURUSD", "CAPITALCOM:US100", "OANDA:XAUUSD"])
            st.number_input("Taille du Lot / Volume", value=1.0, step=0.1)
        with col_o2:
            st.selectbox("Type d'Ordre", ["MARKET", "LIMIT", "STOP"])
            st.number_input("Prix d'entrée", value=104.50, step=0.01)
        with col_o3:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("🟢 BUY / LONG", use_container_width=True):
                st.success("Ordre Long exécuté avec succès.")
            if st.button("🔴 SELL / SHORT", use_container_width=True):
                st.error("Ordre Short exécuté avec succès.")

    with tab3:
        st.markdown("### 📊 **Rapport de Performance Global**")
        st.info("Module d'analyse comportementale et gestion des risques actif. Les graphiques de répartition s'afficheront ici en direct.")
