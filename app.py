import streamlit as st
import pandas as pd
import numpy as np

# ----------------------------
# CONFIG DE LA PAGE
# ----------------------------
st.set_page_config(
    page_title="Finance & Trading",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ----------------------------
# STYLE SOMBRE PERSONNALISÉ
# ----------------------------
st.markdown("""
<style>
    .stApp {
        background-color: #0e1117;
        color: #e6e6e6;
    }
    .metric-card {
        background-color: #161b22;
        border: 1px solid #262c36;
        border-radius: 10px;
        padding: 18px 20px;
        text-align: left;
    }
    .metric-label {
        color: #8b949e;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .metric-value {
        font-size: 26px;
        font-weight: 600;
        margin-top: 4px;
    }
    .metric-change-up { color: #3fb950; font-size: 14px; }
    .metric-change-down { color: #f85149; font-size: 14px; }
    .section-title {
        font-size: 18px;
        font-weight: 600;
        margin-top: 30px;
        margin-bottom: 12px;
        color: #e6e6e6;
    }
    thead tr th {
        background-color: #161b22 !important;
        color: #8b949e !important;
    }
    tbody tr td {
        background-color: #0e1117 !important;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------------
# EN-TÊTE
# ----------------------------
col_logo, col_title = st.columns([0.06, 0.94])
with col_logo:
    st.markdown("### 📈")
with col_title:
    st.markdown("### Finance & Trading")

st.caption("Vue d'ensemble du marché et de votre portefeuille")

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
