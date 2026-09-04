# ==========================================
# 2. PAGE 1 : ACCUEIL
# ==========================================
def show_welcome_page():
    
    # 1. LA BANNIÈRE SUPÉRIEURE (Cadre doré propre et professionnel)
    st.markdown("""
        <div style="
            border: 2px solid #f0b90b;
            border-radius: 12px;
            padding: 30px;
            background: linear-gradient(180deg, rgba(240, 185, 11, 0.08) 0%, rgba(13, 17, 23, 0) 100%);
            box-shadow: 0 0 30px rgba(240, 185, 11, 0.15);
            text-align: center;
            margin-top: 10px;
            margin-bottom: 50px;
        ">
            <h1 style="
                color: #ffffff; 
                margin: 0; 
                font-size: 3.5rem; 
                font-weight: 900; 
                letter-spacing: 3px;
            ">
                TERMINAL TRADER <span style="color: #f0b90b; text-shadow: 0 0 15px rgba(240,185,11,0.6);">PRO</span>
            </h1>
            <p style="
                color: #848e9c; 
                margin-top: 12px; 
                margin-bottom: 0; 
                font-size: 1.1rem; 
                letter-spacing: 5px; 
                font-weight: bold;
            ">
                ÉCOSYSTÈME DE TRADING QUANTITATIF
            </p>
        </div>
    """, unsafe_allow_html=True)

    # 2. LE BOUTON D'ENTRÉE (Centré en dessous)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.write("") # Un peu d'espace vertical
        
        # Un peu de CSS pour rendre le gros bouton de la page d'accueil unique
        st.markdown("""
            <style>
            /* Cible spécifiquement le bouton de la page d'accueil */
            div[data-testid="stButton"] button {
                height: 60px;
                font-size: 1.2rem !important;
                border: 2px solid #f0b90b !important;
                background-color: transparent !important;
                color: #f0b90b !important;
                text-transform: uppercase;
                letter-spacing: 2px;
            }
            div[data-testid="stButton"] button:hover {
                background-color: #f0b90b !important;
                color: #000000 !important;
                box-shadow: 0 0 20px rgba(240, 185, 11, 0.5) !important;
            }
            </style>
        """, unsafe_allow_html=True)

        if st.button("INITIALISER LE SYSTÈME 🚀", use_container_width=True):
            st.session_state.page = "hub"
            st.rerun()
