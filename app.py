import streamlit as st

def show_welcome_page():
    
    # 1. Injection du CSS pour un rendu ultra-propre et minimaliste
    st.markdown("""
        <style>
        /* On remonte un peu le contenu pour éviter le gros vide en haut de Streamlit */
        .block-container {
            padding-top: 2rem !important;
        }
        
        /* Le cadre de la barre */
        .pro-banner {
            background-color: #0E1117; /* Fond sombre naturel */
            border: 1px solid #3A3A3A; /* Bordure grise très fine */
            border-left: 4px solid #D4AF37; /* Accent OR élégant sur la gauche */
            padding: 25px 40px;
            border-radius: 4px; /* Coins légèrement arrondis, très pro */
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 40px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
        }
        
        /* Le texte principal */
        .pro-title {
            color: #FFFFFF;
            font-family: 'Courier New', Courier, monospace; /* Typographie style Terminal/Code */
            font-size: 28px;
            font-weight: 600;
            margin: 0;
            letter-spacing: 2px;
        }
        
        /* Le texte doré */
        .pro-highlight {
            color: #D4AF37; /* Un vrai Or métallique, pas jaune */
            font-weight: 900;
        }
        
        /* Le statut à droite */
        .pro-status {
            color: #848e9c;
            font-size: 13px;
            font-family: 'Courier New', Courier, monospace;
            text-align: right;
            margin: 0;
        }
        </style>

        <!-- 2. La structure HTML de la barre -->
        <div class="pro-banner">
            <div>
                <p class="pro-title">TERMINAL <span class="pro-highlight">PRO TRADER</span></p>
            </div>
            <div>
                <p class="pro-status">VER 2.0.4<br><span style="color:#0ecb81;">● SYSTEM READY</span></p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 3. Le bouton Streamlit (Propre, centré en dessous)
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        if st.button("INITIALISER LE WORKSPACE", use_container_width=True):
            st.session_state.page = "hub"
            st.rerun()

# Test direct si tu lances ce code
if "page" not in st.session_state:
    st.session_state.page = "welcome"

if st.session_state.page == "welcome":
    show_welcome_page()
