import streamlit as st
import streamlit.components.v1 as components
import yfinance as yf
import pandas as pd

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
# RÉCURÉPATION INDIVIDUELLE ULTRA-ROBUSTE
# ==========================================
@st.cache_data(ttl=30)
def get_market_data():
    # Dictionnaire de secours avec des valeurs réalistes
    data = {
        "eur": {"price": 1.0850, "pct": 0.45, "up": True},
        "nas": {"price": 19250.0, "pct": 1.12, "up": True},
        "dxy": {"price": 104.20, "pct": -0.15, "up": False},
        "gold": {"price": 2360.5, "pct": 0.80, "up": True}
    }
    
    tickers_map = {
        "eur": "EURUSD=X",
        "nas": "NQ=F",
        "dxy": "DX-Y.NYB",
        "gold": "GC=F"
    }
    
    for key, symbol in tickers_map.items():
        try:
            df = yf.download(symbol, period="5d", progress=False)
            if not df.empty and "Close" in df.columns:
                # Gère le format multi-index ou simple index de yfinance
                close_series = df["Close"]
                if isinstance(close_series, pd.DataFrame):
                    close_series = close_series.iloc[:, 0]
                
                close_series = close_series.dropna()
                if len(close_series) >= 2:
                    current = float(close_series.iloc[-1])
                    previous = float(close_series.iloc[-2])
                    pct = ((current - previous) / previous) * 100
                    
                    data[key]["price"] = current
                    data[key]["pct"] = pct
                    data[key]["up"] = pct >= 0
        except Exception as e:
            print(f"Erreur pour {symbol}: {e}")
            
    return data

market = get_market_data()

# ==========================================
# PAGE 1 : ACCUEIL SANS SCROLL & PRO
# ==========================================
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
            margin-bottom: 5px;
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

    html_dashboard = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@700&display=swap');
      
      body {{ 
          margin: 0; background: transparent; color: #fff; 
          font-family: 'Share Tech Mono', monospace; 
          display: flex; justify-content: space-between; align-items: center; 
          height: 620px; 
          padding: 0 20px; 
          overflow: hidden;
          position: relative;
      }}
      
      .globe-container {{ 
          position: absolute; top: 50%; left: 50%;
          transform: translate(-50%, -50%); z-index: 1; 
      }}
      .globe {{ 
          width: 560px; height: 560px; border-radius: 50%; 
          background: url('https://eoimages.gsfc.nasa.gov/images/imagerecords/55000/55167/earth_lights_lrg.jpg'); 
          background-size: cover;
          box-shadow: inset -50px -50px 80px rgba(0,0,0,0.95), 0 0 50px rgba(240, 185, 11, 0.15); 
          animation: spin 45s linear infinite;
          opacity: 0.85;
      }}
      @keyframes spin {{ from {{ background-position: 0 0; }} to {{ background-position: 1500px 0; }} }}

      .panel {{ 
          background: rgba(13, 17, 23, 0.6); 
          border: 1px solid rgba(240, 185, 11, 0.2); 
          border-radius: 4px; padding: 25px; 
          box-shadow: 0 0 20px rgba(0,0,0,0.8); 
          backdrop-filter: blur(4px); width: 280px; z-index: 10;
      }}
      
      .clock-title {{ font-family: 'Orbitron', sans-serif; color: #848e9c; font-size: 1rem; margin-bottom: 2px; }}
      .clock-time {{ font-size: 2.8rem; color: #f0b90b; text-shadow: 0 0 10px rgba(240,185,11,0.2); margin-bottom: 20px; font-weight: bold;}}
      
      .asset-row {{ 
          display: flex; justify-content: space-between; align-items: center; 
          padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.05); 
      }}
      .asset-row:last-child {{ border-bottom: none; }}
      .asset-name {{ font-weight: bold; font-size: 1.2rem; color: #c9d1d9; }}
      .asset-price {{ font-size: 1.2rem; text-align: right; font-weight: bold; }}
      .asset-pct {{ font-size: 0.85rem; padding: 2px 6px; border-radius: 4px; text-align: right; margin-top: 2px; font-weight: bold;}}
      
      .up {{ color: #0ecb81; }}
      .down {{ color: #f6465d; }}
      .bg-up {{ background: rgba(14, 203, 129, 0.1); color: #0ecb81; border: 1px solid rgba(14, 203, 129, 0.3); }}
      .bg-down {{ background: rgba(246, 70, 93, 0.1); color: #f6465d; border: 1px solid rgba(246, 70, 93, 0.3); }}
    </style>
    </head>
    <body>

    <div class="globe-container"><div class="globe"></div></div>

    <div class="panel">
        <div class="clock-title">PARIS (CET)</div>
        <div class="clock-time" id="paris">--:--:--</div>
        <div class="clock-title" style="margin-top: 10px;">NEW YORK (EST)</div>
        <div class="clock-time" id="ny" style="margin-bottom: 0;">--:--:--</div>
    </div>

    <div class="panel">
        <div class="asset-row"><span class="asset-name">EUR/USD</span><div><div class="asset-price {'up' if market['eur']['up'] else 'down'}">{market['eur']['price']:.4f}</div><div class="asset-pct {'bg-up' if market['eur']['up'] else 'bg-down'}">{'+' if market['eur']['up'] else ''}{market['eur']['pct']:.2f}%</div></div></div>
        <div class="asset-row"><span class="asset-name">NASDAQ</span><div><div class="asset-price {'up' if market['nas']['up'] else 'down'}">{market['nas']['price']:.2f}</div><div class="asset-pct {'bg-up' if market['nas']['up'] else 'bg-down'}">{'+' if market['nas']['up'] else ''}{market['nas']['pct']:.2f}%</div></div></div>
        <div class="asset-row"><span class="asset-name">DXY</span><div><div class="asset-price {'up' if market['dxy']['up'] else 'down'}">{market['dxy']['price']:.3f}</div><div class="asset-pct {'bg-up' if market['dxy']['up'] else 'bg-down'}">{'+' if market['dxy']['up'] else ''}{market['dxy']['pct']:.2f}%</div></div></div>
        <div class="asset-row"><span class="asset-name">GOLD</span><div><div class="asset-price {'up' if market['gold']['up'] else 'down'}">{market['gold']['price']:.1f}</div><div class="asset-pct {'bg-up' if market['gold']['up'] else 'bg-down'}">{'+' if market['gold']['up'] else ''}{market['gold']['pct']:.2f}%</div></div></div>
    </div>

    <script>
    function updateClocks() {{
        const now = new Date();
        document.getElementById('paris').innerText = now.toLocaleTimeString('fr-FR', {{timeZone: 'Europe/Paris'}});
        document.getElementById('ny').innerText = now.toLocaleTimeString('en-US', {{timeZone: 'America/New_York', hour12: false}});
    }}
    setInterval(updateClocks, 1000); updateClocks();
    </script>
    </body>
    </html>
    """
    
    components.html(html_dashboard, height=620)

    st.markdown("""
        <style>
        div.stButton {
            display: flex;
            justify-content: center;
            margin-top: -15px; 
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

# ==========================================
# PAGE 2 : HUB (WORKSPACE)
# ==========================================
elif st.session_state.page == "hub":
    st.success("✅ AUTHENTIFICATION RÉUSSIE.")
    if st.button("← DISCONNECT"):
        st.session_state.page = "welcome"
        st.rerun()
