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
# PAGE 2 : EXECUTIVE HUB DASHBOARD
# ==========================================
elif st.session_state.page == "hub":
    st.markdown("""
        <style>
        html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
            overflow: hidden !important;
            height: 100vh !important;
            background-color: #0d1117;
            color: #f0f6fc;
            font-family: 'Share Tech Mono', monospace;
        }
        header {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        .block-container { 
            padding-top: 0.4rem !important; 
            padding-bottom: 0.4rem !important;
            padding-left: 1rem !important;
            padding-right: 1rem !important;
            max-width: 100% !important;
            height: 100vh !important;
            display: flex;
            flex-direction: column;
            overflow: hidden !important;
        }

        .ticker-wrap {
            width: 100%;
            overflow: hidden;
            background: #161b22;
            border: 1px solid #30363d;
            border-left: 3px solid #f85149;
            padding: 4px 0;
            margin-bottom: 6px;
            flex-shrink: 0;
            border-radius: 2px;
            display: flex;
            align-items: center;
        }
        .ticker-badge {
            background: #f85149;
            color: white;
            font-weight: bold;
            padding: 2px 6px;
            font-size: 0.7rem;
            margin-left: 8px;
            margin-right: 12px;
            border-radius: 2px;
            letter-spacing: 1px;
            text-transform: uppercase;
        }
        .ticker-text {
            color: #f0f6fc;
            font-size: 0.8rem;
            letter-spacing: 0.5px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .terminal-panel {
            background: rgba(13, 17, 23, 0.95);
            border: 1px solid rgba(240, 185, 11, 0.25);
            border-radius: 4px;
            padding: 8px;
            height: 74vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0,0,0,0.6);
        }
        .panel-heading {
            font-family: 'Orbitron', sans-serif;
            font-size: 0.75rem;
            color: #f0b90b;
            border-bottom: 1px solid #30363d;
            padding-bottom: 4px;
            margin-bottom: 6px;
            letter-spacing: 1px;
            text-transform: uppercase;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .live-dot-green {
            width: 6px; height: 6px; background-color: #3fb950; border-radius: 50%;
            box-shadow: 0 0 6px #3fb950; display: inline-block; margin-right: 5px;
        }
        </style>
        
        <div class="ticker-wrap">
            <span class="ticker-badge">URGENT</span>
            <span class="ticker-text">⚡ FED : Powell maintient les taux directeurs inchangés à 5.25% — Volatilité forte anticipée sur les actifs US & XAUUSD.</span>
        </div>
    """, unsafe_allow_html=True)

    components.html("""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@700&display=swap');
      body {
          margin: 0;
          background: linear-gradient(135deg, #0d1117 0%, #161b22 100%);
          border: 1px solid #30363d;
          border-bottom: 1px solid rgba(240, 185, 11, 0.6);
          padding: 6px 15px;
          border-radius: 4px;
          display: flex;
          justify-content: space-between;
          align-items: center;
          font-family: 'Share Tech Mono', monospace;
          color: #ffffff;
      }
      .hub-title {
          font-family: 'Courier New', Courier, monospace;
          font-size: 1.2rem;
          font-weight: bold;
          margin: 0;
          letter-spacing: 2px;
      }
      .hub-title span { color: #f0b90b; }
      .clocks-container {
          display: flex;
          gap: 20px;
          font-family: 'Courier New', Courier, monospace;
          font-size: 0.9rem;
          color: #c9d1d9;
      }
      .clock-item span { color: #f0b90b; font-weight: bold; }
    </style>
    </head>
    <body>
        <h1 class="hub-title">TERMINAL TRADER <span>PRO</span> // EXECUTIVE HUB</h1>
        <div class="clocks-container">
            <div class="clock-item">PARIS: <span id="clock-paris">--:--:--</span></div>
            <div class="clock-item">NEW YORK: <span id="clock-ny">--:--:--</span></div>
        </div>
        <script>
        function updateClocks() {
            const now = new Date();
            document.getElementById('clock-paris').innerText = now.toLocaleTimeString('fr-FR', {timeZone: 'Europe/Paris'});
            document.getElementById('clock-ny').innerText = now.toLocaleTimeString('en-US', {timeZone: 'America/New_York', hour12: false});
        }
        setInterval(updateClocks, 1000);
        updateClocks();
        </script>
    </body>
    </html>
    """, height=45)

    col_left, col_center, col_right = st.columns([1.25, 1.3, 1.05])

    with col_left:
        st.markdown("""
        <div class="terminal-panel">
            <div class="panel-heading"><span>⚡ NASDAQ 100 HEATMAP</span><span><div class="live-dot-green"></div>LIVE</span></div>
            <div style="flex-grow: 1; overflow: hidden; position: relative;">
                <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-stock-heatmap.js" async>
                {
                  "exchanges": [],
                  "dataSource": "NASDAQ100",
                  "grouping": "sector",
                  "blockSize": "market_cap_basic",
                  "blockColor": "change",
                  "locale": "fr",
                  "symbolUrl": "",
                  "colorTheme": "dark",
                  "hasTopBar": false,
                  "isTransparent": true,
                  "width": "100%",
                  "height": "100%"
                }
                </script>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_center:
        st.markdown("""
        <div class="terminal-panel" style="gap: 6px;">
            <div style="height: 49%; display: flex; flex-direction: column;">
                <div class="panel-heading"><span>📅 CALENDRIER ÉCONOMIQUE</span><span>FOREX FACTORY</span></div>
                <div style="flex-grow: 1; overflow-y: auto;">
                    <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-events.js" async>
                    {
                      "colorTheme": "dark",
                      "isTransparent": true,
                      "width": "100%",
                      "height": "100%",
                      "locale": "fr",
                      "importanceFilter": "-1,0,1"
                    }
                    </script>
                </div>
            </div>
            <div style="height: 49%; display: flex; flex-direction: column;">
                <div class="panel-heading"><span>🌐 ANALYSE MACRO & GÉOPOLITIQUE</span><span><div class="live-dot-green"></div>FLUX CONTINU</span></div>
                <div style="background: #161b22; border: 1px solid #30363d; border-radius: 3px; padding: 8px; flex-grow: 1; overflow-y: auto; font-size: 0.75rem; color: #8b949e;">
                    <div style="margin-bottom: 6px; border-left: 2px solid #f0b90b; padding-left: 6px;">
                        <span style="color: #f0b90b; font-weight: bold;">[11:02] GÉOPOLITIQUE</span> : Tensions accrues au Moyen-Orient : Impact direct sur les flux pétroliers et valeurs refuges (Or).
                    </div>
                    <div style="margin-bottom: 6px; border-left: 2px solid #58a6ff; padding-left: 6px;">
                        <span style="color: #58a6ff; font-weight: bold;">[10:45] BANQUES CENTRALES</span> : BCE : Christine Lagarde insiste sur une stricte dépendance aux données macroéconomiques.
                    </div>
                    <div style="border-left: 2px solid #3fb950; padding-left: 6px;">
                        <span style="color: #3fb950; font-weight: bold;">[10:15] MARCHÉS US</span> : NASDAQ Futures : Forte pression acheteuse sur les semi-conducteurs avant l'ouverture de Wall Street.
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_right:
        st.markdown("""
        <div class="terminal-panel" style="display: flex; flex-direction: column; justify-content: space-between;">
            <div>
                <div class="panel-heading"><span>🔥 TOP PERF & WATCHLIST</span><span>INSTRUMENTS</span></div>
                <div style="margin-bottom: 4px;">
                    <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
                    {"symbol": "NASDAQ:NVDA", "width": "100%", "colorTheme": "dark", "isTransparent": true, "locale": "fr"}
                    </script>
                </div>
                <div style="margin-bottom: 4px;">
                    <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
                    {"symbol": "NASDAQ:TSLA", "width": "100%", "colorTheme": "dark", "isTransparent": true, "locale": "fr"}
                    </script>
                </div>
                <div style="margin-bottom: 4px;">
                    <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
                    {"symbol": "OANDA:XAUUSD", "width": "100%", "colorTheme": "dark", "isTransparent": true, "locale": "fr"}
                    </script>
                </div>
                <div>
                    <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
                    {"symbol": "CAPITALCOM:DXY", "width": "100%", "colorTheme": "dark", "isTransparent": true, "locale": "fr"}
                    </script>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    col_btn1, col_btn2, col_btn3 = st.columns([3, 1, 3])
    with col_btn2:
        st.markdown("""
            <style>
            div.stButton > button {
                background-color: transparent !important;
                color: #848e9c !important; 
                border: 1px solid rgba(240, 185, 11, 0.3) !important; 
                font-family: 'Courier New', Courier, monospace !important;
                font-size: 0.75rem !important;
                letter-spacing: 2px !important; 
                padding: 2px 15px !important;
                border-radius: 2px !important; 
                width: 100% !important;
            }
            div.stButton > button:hover {
                border: 1px solid #f0b90b !important; 
                color: #f0b90b !important; 
            }
            </style>
        """, unsafe_allow_html=True)
        if st.button("← DÉCONNEXION"):
            st.session_state.page = "welcome"
            st.rerun()
