import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np

# ----------------------------
# CONFIG DE LA PAGE
# ----------------------------
st.set_page_config(
    page_title="Terminal Trader Pro",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ----------------------------
# STYLE SOMBRE PERSONNALISÉ (sections basses de la page)
# ----------------------------
st.markdown("""
<style>
    .stApp {
        background-color: #050607;
        color: #d7dee5;
    }
    .block-container { padding-top: 0rem; padding-left: 0rem; padding-right: 0rem; }
    .metric-card {
        background-color: #0b0d10;
        border: 1px solid #1c2128;
        border-radius: 6px;
        padding: 18px 20px;
        text-align: left;
        font-family: 'JetBrains Mono', monospace;
    }
    .metric-label {
        color: #6b7680;
        font-size: 12px;
        letter-spacing: 0.5px;
    }
    .metric-value {
        font-size: 24px;
        font-weight: 600;
        margin-top: 4px;
    }
    .metric-change-up { color: #00e08f; font-size: 13px; }
    .metric-change-down { color: #ff4d4d; font-size: 13px; }
    .section-title {
        font-size: 16px;
        font-weight: 600;
        margin-top: 26px;
        margin-bottom: 10px;
        margin-left: 20px;
        color: #d7dee5;
        font-family: 'JetBrains Mono', monospace;
    }
    .main .block-container { max-width: 100% !important; }
    thead tr th {
        background-color: #0b0d10 !important;
        color: #6b7680 !important;
    }
    tbody tr td {
        background-color: #050607 !important;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------------
# HERO : BARRE + GLOBE + HORLOGES + TICKER (HTML/CSS/JS autonome)
# ----------------------------
HERO_HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.8.5/d3.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/topojson-client/3.1.0/topojson-client.min.js"></script>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body {
    background: #050607;
    font-family: 'JetBrains Mono', monospace;
    overflow: hidden;
  }

  .top-accent {
    height: 2px;
    background: linear-gradient(90deg, #c9a04d 0%, #00e08f 50%, #c9a04d 100%);
    opacity: 0.7;
  }

  /* ---------- BARRE SUPERIEURE ---------- */
  .topbar {
    height: 46px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 22px;
    background: #08090b;
    border-bottom: 1px solid #1c2128;
  }
  .brand {
    display: flex;
    align-items: center;
    gap: 10px;
    color: #e7ecf1;
    font-weight: 700;
    font-size: 14px;
    letter-spacing: 1.5px;
  }
  .brand .dot-brand {
    width: 7px; height: 7px; border-radius: 50%;
    background: #c9a04d;
    box-shadow: 0 0 8px #c9a04d;
  }
  .status-group {
    display: flex;
    align-items: center;
    gap: 20px;
    font-size: 12px;
    color: #6b7680;
  }
  .status-item { display: flex; align-items: center; gap: 7px; }
  .pulse {
    width: 8px; height: 8px; border-radius: 50%;
    background: #00e08f;
    box-shadow: 0 0 6px #00e08f;
    animation: pulse 1.6s ease-in-out infinite;
  }
  @keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.4; transform: scale(0.8); }
  }
  .online-label { color: #00e08f; font-weight: 600; letter-spacing: 0.5px; }
  #ping { color: #d7dee5; font-weight: 600; }

  /* ---------- ZONE HERO ---------- */
  .hero {
    position: relative;
    height: 460px;
    background:
      radial-gradient(ellipse at center, rgba(16,26,32,0.7) 0%, #050607 70%);
    background-image:
      radial-gradient(ellipse at center, rgba(16,26,32,0.7) 0%, #050607 70%),
      linear-gradient(rgba(255,255,255,0.02) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255,255,255,0.02) 1px, transparent 1px);
    background-size: auto, 34px 34px, 34px 34px;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  /* Globe réaliste (canvas D3 : continents + graticule + rotation) */
  .globe-scene {
    position: relative;
    width: 360px;
    height: 360px;
  }
  .globe-glow {
    position: absolute;
    inset: -20px;
    border-radius: 50%;
    background: radial-gradient(circle at 38% 32%, rgba(0,224,143,0.16), rgba(0,224,143,0) 65%);
    filter: blur(2px);
    pointer-events: none;
  }
  #globeCanvas {
    position: relative;
    z-index: 1;
  }

  /* ---------- HORLOGES (gauche) ---------- */
  .clocks {
    position: absolute;
    left: 28px;
    top: 50%;
    transform: translateY(-50%);
    display: flex;
    flex-direction: column;
    gap: 26px;
    z-index: 3;
  }
  .clock-block .city {
    color: #6b7680;
    font-size: 11px;
    letter-spacing: 1.5px;
    margin-bottom: 4px;
  }
  .clock-block .time {
    color: #e7ecf1;
    font-size: 30px;
    font-weight: 600;
    letter-spacing: 1px;
  }
  .clock-block .date {
    color: #4d5761;
    font-size: 11px;
    margin-top: 2px;
  }

  /* ---------- TICKER ACTIFS (droite) ---------- */
  .ticker-box {
    position: absolute;
    right: 28px;
    top: 50%;
    transform: translateY(-50%);
    width: 240px;
    background: rgba(11,13,16,0.88);
    border: 1px solid #1c2128;
    border-radius: 8px;
    padding: 14px 16px;
    z-index: 3;
    backdrop-filter: blur(3px);
    box-shadow: 0 12px 30px rgba(0,0,0,0.45);
  }
  .ticker-title {
    color: #6b7680;
    font-size: 10px;
    letter-spacing: 1.5px;
    margin-bottom: 10px;
    padding-bottom: 8px;
    border-bottom: 1px solid #1c2128;
  }
  .ticker-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 8px 0;
    border-bottom: 1px solid rgba(28,33,40,0.6);
  }
  .ticker-row:last-child { border-bottom: none; }
  .ticker-row .sym {
    display: flex;
    align-items: center;
    gap: 7px;
    color: #d7dee5;
    font-size: 12.5px;
    font-weight: 600;
    width: 76px;
  }
  .ticker-row .sym .lead-dot {
    width: 5px; height: 5px; border-radius: 50%;
    background: #6b7680;
    flex-shrink: 0;
  }
  .ticker-row .price {
    font-size: 12.5px;
    color: #d7dee5;
    text-align: right;
    width: 70px;
  }
  .ticker-row .pct {
    font-size: 11.5px;
    text-align: right;
    width: 58px;
    font-weight: 600;
  }
  .up { color: #00e08f; }
  .down { color: #ff4d4d; }
</style>
</head>
<body>

  <div class="top-accent"></div>
  <div class="topbar">
    <div class="brand"><span class="dot-brand"></span>TERMINAL TRADER PRO</div>
    <div class="status-group">
      <div class="status-item">SERVER <span id="ping">—</span> ms</div>
      <div class="status-item"><span class="pulse"></span><span class="online-label">ONLINE</span></div>
    </div>
  </div>

  <div class="hero">
    <div class="globe-scene">
      <div class="globe-glow"></div>
      <canvas id="globeCanvas" width="360" height="360"></canvas>
    </div>

    <div class="clocks">
      <div class="clock-block">
        <div class="city">PARIS</div>
        <div class="time" id="clock-paris">--:--:--</div>
        <div class="date" id="date-paris">--</div>
      </div>
      <div class="clock-block">
        <div class="city">NEW YORK</div>
        <div class="time" id="clock-ny">--:--:--</div>
        <div class="date" id="date-ny">--</div>
      </div>
    </div>

    <div class="ticker-box">
      <div class="ticker-title">MARCHÉS EN DIRECT</div>
      <div id="ticker-list"></div>
    </div>
  </div>

<script>
  // ---- Globe réaliste : projection orthographique D3 avec vrais contours de continents ----
  (function() {
    const width = 360, height = 360;
    const canvas = document.getElementById('globeCanvas');
    const context = canvas.getContext('2d');

    const projection = d3.geoOrthographic()
      .scale(168)
      .translate([width / 2, height / 2])
      .clipAngle(90)
      .precision(0.3);

    const path = d3.geoPath(projection, context);
    const graticule = d3.geoGraticule10();
    let rotation = [0, -18];

    function drawFrame(landFeatures) {
      context.clearRect(0, 0, width, height);

      // Sphère océanique
      context.beginPath();
      path({ type: 'Sphere' });
      context.fillStyle = 'rgba(6, 22, 22, 0.55)';
      context.fill();
      context.lineWidth = 1;
      context.strokeStyle = 'rgba(0, 224, 143, 0.35)';
      context.stroke();

      // Graticule (méridiens / parallèles)
      context.beginPath();
      path(graticule);
      context.lineWidth = 0.5;
      context.strokeStyle = 'rgba(0, 224, 143, 0.14)';
      context.stroke();

      // Continents
      if (landFeatures) {
        context.beginPath();
        path(landFeatures);
        context.fillStyle = 'rgba(0, 224, 143, 0.30)';
        context.fill();
        context.lineWidth = 0.7;
        context.strokeStyle = 'rgba(120, 240, 200, 0.65)';
        context.stroke();
      }

      // Voile d'ombre bas-droite pour donner du volume
      const shade = context.createRadialGradient(
        width * 0.68, height * 0.68, width * 0.1,
        width * 0.5, height * 0.5, width * 0.62
      );
      shade.addColorStop(0, 'rgba(0,0,0,0)');
      shade.addColorStop(1, 'rgba(0,0,0,0.35)');
      context.beginPath();
      path({ type: 'Sphere' });
      context.fillStyle = shade;
      context.fill();
    }

    let land = null;
    d3.json('https://cdn.jsdelivr.net/npm/world-atlas@2/countries-110m.json')
      .then(world => {
        land = topojson.feature(world, world.objects.countries);
      })
      .catch(() => { land = null; })
      .finally(() => {
        d3.timer(() => {
          rotation[0] += 0.18;
          projection.rotate(rotation);
          drawFrame(land);
        });
      });
  })();

  // ---- Horloges Paris / New York ----
  function pad(n) { return n.toString().padStart(2, '0'); }
  function updateClocks() {
    const now = new Date();
    const parisFmt = new Intl.DateTimeFormat('fr-FR', { timeZone: 'Europe/Paris', hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false });
    const parisDateFmt = new Intl.DateTimeFormat('fr-FR', { timeZone: 'Europe/Paris', day: '2-digit', month: 'short' });
    const nyFmt = new Intl.DateTimeFormat('en-US', { timeZone: 'America/New_York', hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false });
    const nyDateFmt = new Intl.DateTimeFormat('en-US', { timeZone: 'America/New_York', day: '2-digit', month: 'short' });
    document.getElementById('clock-paris').textContent = parisFmt.format(now);
    document.getElementById('date-paris').textContent = parisDateFmt.format(now);
    document.getElementById('clock-ny').textContent = nyFmt.format(now);
    document.getElementById('date-ny').textContent = nyDateFmt.format(now);
  }
  updateClocks();
  setInterval(updateClocks, 1000);

  // ---- Ping serveur simulé ----
  function updatePing() {
    const ms = Math.floor(8 + Math.random() * 34);
    document.getElementById('ping').textContent = ms;
  }
  updatePing();
  setInterval(updatePing, 2200);

  // ---- Ticker d'actifs (simulation de flux live) ----
  const assets = [
    { sym: 'EUR/USD', price: 1.0842, decimals: 4, changePct: 0.00 },
    { sym: 'NASDAQ',  price: 19210.55, decimals: 2, changePct: -0.31 },
    { sym: 'DXY',     price: 101.24, decimals: 2, changePct: 0.18 },
    { sym: 'GOLD',    price: 2382.40, decimals: 2, changePct: 0.62 },
  ];

  const list = document.getElementById('ticker-list');
  assets.forEach((a, i) => {
    const row = document.createElement('div');
    row.className = 'ticker-row';
    row.id = 'row-' + i;
    row.innerHTML = `
      <span class="sym"><span class="lead-dot" id="dot-${i}"></span>${a.sym}</span>
      <span class="price" id="price-${i}">${a.price.toFixed(a.decimals)}</span>
      <span class="pct" id="pct-${i}">${a.changePct.toFixed(2)}%</span>
    `;
    list.appendChild(row);
  });

  function refreshAssets() {
    assets.forEach((a, i) => {
      const drift = (Math.random() - 0.5) * (a.price * 0.0006);
      a.price += drift;
      a.changePct += (Math.random() - 0.5) * 0.05;
      const priceEl = document.getElementById('price-' + i);
      const pctEl = document.getElementById('pct-' + i);
      const dotEl = document.getElementById('dot-' + i);
      const isUp = a.changePct >= 0;
      priceEl.textContent = a.price.toFixed(a.decimals);
      pctEl.textContent = (isUp ? '+' : '') + a.changePct.toFixed(2) + '%';
      priceEl.className = 'price ' + (isUp ? 'up' : 'down');
      pctEl.className = 'pct ' + (isUp ? 'up' : 'down');
      dotEl.style.background = isUp ? '#00e08f' : '#ff4d4d';
      dotEl.style.boxShadow = isUp ? '0 0 5px #00e08f' : '0 0 5px #ff4d4d';
    });
  }
  refreshAssets();
  setInterval(refreshAssets, 2000);
</script>
</body>
</html>
"""

components.html(HERO_HTML, height=510, scrolling=False)

# ----------------------------
# DONNÉES DE DÉMO (à remplacer par une vraie source plus tard)
# ----------------------------
indices = [
    {"name": "CAC 40", "value": "7 542.10", "change": +0.84},
    {"name": "S&P 500", "value": "5 980.32", "change": +0.42},
    {"name": "NASDAQ", "value": "19 210.55", "change": -0.31},
    {"name": "Bitcoin", "value": "61 240 €", "change": +2.15},
]

portfolio_value = 24_318.72
portfolio_change_pct = 1.36
portfolio_change_eur = 326.10

watchlist = pd.DataFrame({
    "Actif": ["Apple", "LVMH", "TotalEnergies", "Tesla", "Air Liquide"],
    "Symbole": ["AAPL", "MC.PA", "TTE.PA", "TSLA", "AI.PA"],
    "Cours": [227.15, 682.40, 58.92, 248.30, 178.60],
    "Variation (%)": [1.2, -0.4, 0.8, -2.1, 0.3],
})

# ----------------------------
# CARTES INDICES
# ----------------------------
st.markdown('<div class="section-title">Marché</div>', unsafe_allow_html=True)
cols = st.columns(len(indices))
for col, idx in zip(cols, indices):
    css_class = "metric-change-up" if idx["change"] >= 0 else "metric-change-down"
    arrow = "▲" if idx["change"] >= 0 else "▼"
    col.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">{idx['name']}</div>
        <div class="metric-value">{idx['value']}</div>
        <div class="{css_class}">{arrow} {abs(idx['change'])}%</div>
    </div>
    """, unsafe_allow_html=True)

# ----------------------------
# PORTEFEUILLE
# ----------------------------
st.markdown('<div class="section-title">Mon portefeuille</div>', unsafe_allow_html=True)

col_a, col_b = st.columns([0.3, 0.7])

with col_a:
    change_class = "metric-change-up" if portfolio_change_pct >= 0 else "metric-change-down"
    arrow = "▲" if portfolio_change_pct >= 0 else "▼"
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Valeur totale</div>
        <div class="metric-value">{portfolio_value:,.2f} €</div>
        <div class="{change_class}">{arrow} {portfolio_change_pct}% ({portfolio_change_eur:+.2f} €) aujourd'hui</div>
    </div>
    """, unsafe_allow_html=True)

with col_b:
    # petit graphique de performance simulé
    dates = pd.date_range(end=pd.Timestamp.today(), periods=30)
    np.random.seed(42)
    values = portfolio_value + np.cumsum(np.random.normal(0, 150, len(dates)))
    perf_df = pd.DataFrame({"Date": dates, "Valeur (€)": values}).set_index("Date")
    st.line_chart(perf_df, height=160)

# ----------------------------
# WATCHLIST
# ----------------------------
st.markdown('<div class="section-title">Watchlist</div>', unsafe_allow_html=True)
st.dataframe(watchlist, use_container_width=True, hide_index=True)

# ----------------------------
# PIED DE PAGE
# ----------------------------
st.markdown("---")
st.caption("Données fictives à des fins de démonstration • Aucun conseil en investissement")
