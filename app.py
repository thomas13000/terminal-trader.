# ==========================================
# PAGE 2 : HUB / WORKSPACE (BARRE UNIFIÉE PRO)
# ==========================================
elif st.session_state.page == "hub":

    # 1. BOUTON NATIF STREAMLIT (Gère la navigation de manière fiable)
    if st.button("← ACCUEIL"):
        st.session_state.page = "welcome"
        st.query_params["page"] = "welcome"
        st.rerun()

    # 2. SUPERPOSITION CSS (Place le bouton Streamlit dans la barre HTML)
    st.markdown("""
        <style>
        /* On cible le bouton généré ci-dessus pour le placer en haut à droite */
        [data-testid="stButton"] {
            position: absolute !important;
            top: 20px !important;
            right: 40px !important;
            z-index: 9999 !important;
            width: auto !important;
        }
        [data-testid="stButton"] > button {
            background: linear-gradient(135deg, #f0b90b 0%, #d4a007 100%) !important;
            color: #080b10 !important;
            border-radius: 6px !important;
            padding: 7px 16px !important;
            border: none !important;
            box-shadow: 0 0 15px rgba(240, 185, 11, 0.4) !important;
            width: auto !important;
            min-height: 0 !important;
        }
        [data-testid="stButton"] > button p {
            font-family: 'Orbitron', sans-serif !important;
            font-size: 0.75rem !important;
            font-weight: 900 !important;
            letter-spacing: 1.2px !important;
            margin: 0 !important;
        }
        [data-testid="stButton"] > button:hover {
            box-shadow: 0 0 25px rgba(240, 185, 11, 0.9), 0 0 12px #00f3ff !important;
            color: #000000 !important;
            transform: translateY(-1px) !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # 3. LE HTML (Identique, mais la ligne du lien <a> a été supprimée)
    page2_header_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@700;800&family=Orbitron:wght@800;900&family=Inter:wght@600;700&display=swap');
            * { box-sizing: border-box; }
            body { margin: 0; padding: 0; background: transparent; font-family: 'JetBrains Mono', monospace; }
            .hud-header-p2 { background: rgba(13, 17, 23, 0.94); border: 1.5px solid rgba(240, 185, 11, 0.45); border-radius: 12px; padding: 8px 18px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 6px 25px rgba(0, 0, 0, 0.8), 0 0 15px rgba(240, 185, 11, 0.2); backdrop-filter: blur(20px); }
            .left-brand { display: flex; align-items: center; gap: 12px; }
            .logo-icon { width: 34px; height: 34px; background: linear-gradient(135deg, #f0b90b, #d4a007); border-radius: 8px; display: flex; align-items: center; justify-content: center; font-family: 'Orbitron', sans-serif; font-weight: 900; color: #000; font-size: 1.05rem; box-shadow: 0 0 12px rgba(240,185,11,0.6); }
            .title-p2 { font-family: 'Orbitron', sans-serif; font-weight: 900; color: #ffffff; font-size: 1.05rem; letter-spacing: 1.5px; line-height: 1.1; }
            .hud-gold { color: #f0b90b; }
            .subtitle-p2 { font-size: 0.62rem; color: #848e9c; letter-spacing: 1px; }
            .header-clocks-container { display: flex; align-items: center; gap: 18px; background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(240, 185, 11, 0.25); padding: 5px 16px; border-radius: 8px; }
            .clock-item { display: flex; align-items: center; gap: 8px; }
            .clock-flag { font-family: 'Orbitron', sans-serif; font-size: 0.7rem; font-weight: 900; color: #f0b90b; }
            .clock-time { font-size: 1.1rem; font-weight: 800; color: #ffffff; letter-spacing: 1px; text-shadow: 0 0 8px rgba(255, 255, 255, 0.3); }
            .clock-divider { width: 1px; height: 20px; background: rgba(240, 185, 11, 0.3); }
            .right-status { display: flex; align-items: center; gap: 14px; padding-right: 120px; /* Laisse l'espace pour le bouton CSS */ }
            .status-badge { background: rgba(255,255,255,0.05); padding: 6px 12px; border-radius: 6px; border: 1px solid rgba(255,255,255,0.1); font-size: 0.75rem; color: #848e9c; display: flex; align-items: center; }
            .online-badge { background: rgba(14,203,129,0.12); padding: 6px 12px; border-radius: 20px; border: 1px solid rgba(14,203,129,0.3); display: flex; align-items: center; gap: 6px; font-weight: 700; color: #0ecb81; font-size: 0.75rem; }
            .online-dot { width: 6px; height: 6px; background: #0ecb81; border-radius: 50%; box-shadow: 0 0 8px #0ecb81; }
        </style>
    </head>
    <body>
        <div class="hud-header-p2">
            <div class="left-brand">
                <div class="logo-icon">⚡</div>
                <div>
                    <div class="title-p2">TERMINAL TRADER <span class="hud-gold">PRO</span></div>
                    <div class="subtitle-p2">QUANTITATIVE WORKSPACE</div>
                </div>
            </div>
            <div class="header-clocks-container">
                <div class="clock-item"><span class="clock-flag">🇫🇷 PARIS</span><span class="clock-time" id="p2-paris">--:--:--</span></div>
                <div class="clock-divider"></div>
                <div class="clock-item"><span class="clock-flag">🇺🇸 NEW YORK</span><span class="clock-time" id="p2-ny">--:--:--</span></div>
            </div>
            <div class="right-status">
                <div class="status-badge">MS SERVEUR : <span style="color:#00f3ff; font-weight:700; margin-left:4px;">__LATENCY__ ms</span></div>
                <div class="online-badge"><span class="online-dot"></span>ONLINE</div>
            </div>
        </div>
        <script>
            function updateP2Clocks() {
                const now = new Date();
                document.getElementById('p2-paris').innerText = now.toLocaleTimeString('fr-FR', { timeZone: 'Europe/Paris', hour: '2-digit', minute: '2-digit', second: '2-digit' });
                document.getElementById('p2-ny').innerText = now.toLocaleTimeString('en-US', { timeZone: 'America/New_York', hour12: false, hour: '2-digit', minute: '2-digit', second: '2-digit' });
            }
            setInterval(updateP2Clocks, 1000);
            updateP2Clocks();
        </script>
    </body>
    </html>
    """.replace("__LATENCY__", str(latency_ms))

    components.html(page2_header_html, height=62, scrolling=False)

    st.markdown("""
        <div class="hud-card" style="margin-top:10px;">
            <div class="hud-title" style="font-size:1.1rem; color:#f0b90b;">
                🚀 WORKSPACE QUANTITATIF PRÊT
            </div>
            <p style="color:#848e9c; margin-top:8px; font-size:0.85rem;">
                La navigation est réparée : le bouton fonctionne nativement avec Streamlit.
            </p>
        </div>
    """, unsafe_allow_html=True)
