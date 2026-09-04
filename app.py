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

if st.session_state.page == "welcome":
    st.markdown("""
        <style>
        header {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        .block-container { 
            padding-top: 1rem !important; 
            padding-bottom: 0rem !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
            max-width: 100% !important;
        }
        
        .top-bar {
            background: linear-gradient(135deg, #0d1117 0%, #161b22 100%);
            border: 1px solid #30363d;
            border-bottom: 1px solid rgba(240, 185, 11, 0.6);
            padding: 10px 20px;
            border-radius: 4px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }
        .top-title {
            font-family: 'Courier New', Courier, monospace;
            font-size: 1.5rem;
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

    col_clocks, col_globe, col_assets = st.columns([1, 1.8, 1])

    with col_clocks:
        components.html("""
        <!DOCTYPE html>
        <html>
        <head>
        <style>
          @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@700&display=swap');
          body { margin: 0; background: transparent; font-family: 'Share Tech Mono', monospace; }
          .panel { 
              background: rgba(13, 17, 23, 0.7); 
              border: 1px solid rgba(240, 185, 11, 0.2); 
              border-radius: 4px; padding: 25px; 
              box-shadow: 0 0 20px rgba(0,0,0,0.8); 
              backdrop-filter: blur(4px); width: 260px;
          }
          .clock-title { font-family: 'Orbitron', sans-serif; color: #848e9c; font-size: 0.9rem; margin-bottom: 2px; }
          .clock-time { font-size: 2.4rem; color: #f0b90b; text-shadow: 0 0 10px rgba(240,185,11,0.2); margin-bottom: 15px; font-weight: bold;}
        </style>
        </head>
        <body>
        <div class="panel">
            <div class="clock-title">PARIS (CET)</div>
            <div class="clock-time" id="paris">--:--:--</div>
            <div class="clock-title">NEW YORK (EST)</div>
            <div class="clock-time" id="ny" style="margin-bottom: 0;">--:--:--</div>
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
        """, height=380)

    with col_globe:
        components.html("""
        <!DOCTYPE html>
        <html>
        <head>
        <style>
          body { margin: 0; background: transparent; display: flex; justify-content: center; align-items: center; height: 380px; overflow: hidden; }
          .globe { 
              width: 340px; height: 340px; border-radius: 50%; 
              background: url('https://eoimages.gsfc.nasa.gov/images/imagerecords/55000/55167/earth_lights_lrg.jpg'); 
              background-size: cover;
              box-shadow: inset -30px -30px 60px rgba(0,0,0,0.95), 0 0 40px rgba(240, 185, 11, 0.15); 
              animation: spin 45s linear infinite;
              opacity: 0.85;
          }
          @keyframes spin { from { background-position: 0 0; } to { background-position: 1500px 0; } }
        </style>
        </head>
        <body>
        <div class="globe"></div>
        </body>
        </html>
        """, height=380)

    with col_assets:
        components.html("""
        <!DOCTYPE html>
        <html>
        <head><style>body { margin: 0; background: transparent; overflow: hidden; }</style></head>
        <body>
        <div class="tradingview-widget-container" style="margin-bottom: 4px;">
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
          {
          "symbol": "FX_IDC:EURUSD",
          "width": "100%",
          "colorTheme": "dark",
          "isTransparent": true,
          "locale": "fr"
        }
          </script>
        </div>
        <div class="tradingview-widget-container" style="margin-bottom: 4px;">
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
          {
          "symbol": "NASDAQ:IXIC",
          "width": "100%",
          "colorTheme": "dark",
          "isTransparent": true,
          "locale": "fr"
        }
          </script>
        </div>
        <div class="tradingview-widget-container" style="margin-bottom: 4px;">
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
          {
          "symbol": "TVC:DXY",
          "width": "100%",
          "colorTheme": "dark",
          "isTransparent": true,
          "locale": "fr"
        }
          </script>
        </div>
        <div class="tradingview-widget-container">
          <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js" async>
          {
          "symbol": "COMEX:GC1!",
          "width": "100%",
          "colorTheme": "dark",
          "isTransparent": true,
          "locale": "fr"
        }
          </script>
        </div>
        </body>
        </html>
        """, height=380)

    st.markdown("""
        <style>
        div.stButton {
            display: flex;
            justify-content: center;
            margin-top: 10px; 
        }
        div.stButton > button {
            background-color: transparent !important;
            color: #848e9c !important; 
            border: 1px solid rgba(240, 185, 11, 0.3) !important; 
            font-family: 'Courier New', Courier, monospace !important;
            font-size: 0.95rem !important;
            font-weight: 600 !important;
            letter-spacing: 4px !important; 
            padding: 12px 40px !important;
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

elif st.session_state.page == "hub":
    st.success("✅ AUTHENTIFICATION RÉUSSIE.")
    if st.button("← DISCONNECT"):
        st.session_state.page = "welcome"
        st.rerun()
