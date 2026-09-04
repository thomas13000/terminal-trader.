import streamlit as st

st.set_page_config(
    page_title="TERMINAL TRADER PRO",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 1. Gestion stricte de la navigation dans Streamlit
if "page" not in st.session_state:
    st.session_state.page = st.query_params.get("page", "welcome")

# ==========================================
# PAGE 1 : WELCOME SCREEN (GLOBE 3D)
# ==========================================
if st.session_state.page == "welcome":
    
    st.markdown("""
        <style>
            header, footer, [data-testid="stHeader"] { 
                display: none !important; 
                visibility: hidden !important; 
            }
            html, body, .stApp {
                background-color: #080b10 !important;
                overflow: hidden !important;
            }
            .block-container {
                padding: 0 !important;
                margin: 0 !important;
            }
            /* Style pour le bouton Streamlit natif sous le globe */
            div.stButton > button {
                width: 100%;
                background: linear-gradient(135deg, #f0b90b 0%, #d4a007 100%);
                color: #000000 !important;
                font-weight: 900;
                border: none;
                padding: 12px 20px;
                border-radius: 8px;
                cursor: pointer;
                letter-spacing: 1px;
            }
        </style>
    """, unsafe_allow_html=True)

    welcome_html_code = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body, html { margin: 0; padding: 0; width: 100vw; height: 100vh; overflow: hidden; background: #080b10; color: #fff; font-family: sans-serif; }
        #canvas { width: 100vw; height: 100vh; display: block; }
        .overlay { position: fixed; top: 20px; left: 20px; z-index: 10; font-weight: bold; letter-spacing: 2px; }
        .hint { position: fixed; bottom: 30px; left: 50%; transform: translateX(-50%); z-index: 10; background: rgba(0,0,0,0.7); padding: 10px 20px; border-radius: 20px; border: 1px solid #f0b90b; color: #f0b90b; font-family: monospace; }
    </style>
</head>
<body>
    <div class="overlay">⚡ TERMINAL TRADER PRO</div>
    <div class="hint">Appuie sur [ ENTRÉE ] ou clique sur le bouton ci-dessous pour continuer</div>
    <canvas id="canvas"></canvas>

    <script>
        // Force le focus dans l'iframe pour capturer la touche Entrée immédiatement
        window.focus();
        document.addEventListener('click', () => { window.focus(); });

        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
        camera.position.z = 25;

        const renderer = new THREE.WebGLRenderer({ canvas: document.getElementById('canvas'), antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);

        const geo = new THREE.SphereGeometry(8, 32, 32);
        const mat = new THREE.MeshBasicMaterial({ color: 0xf0b90b, wireframe: true });
        const sphere = new THREE.Mesh(geo, mat);
        scene.add(sphere);

        function animate() {
            requestAnimationFrame(animate);
            sphere.rotation.y += 0.005;
            renderer.render(scene, camera);
        }
        animate();

        // Capture de la touche Entrée
        window.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                window.top.location.href = window.top.location.pathname + '?page=hub';
            }
        });
    </script>
</body>
</html>
    """

    st.components.v1.html(welcome_html_code, height=600)

    # Bouton Streamlit direct (garantit le passage à la page 2 à 100%)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 ENTRER DANS LE TERMINAL (PAGE VIERGE)"):
            st.query_params["page"] = "hub"
            st.session_state.page = "hub"
            st.rerun()

# ==========================================
# PAGE 2 : PAGE VIERGE
# ==========================================
elif st.session_state.page == "hub":
    
    if st.button("← Retour à l'accueil"):
        st.query_params["page"] = "welcome"
        st.session_state.page = "welcome"
        st.rerun()

    st.title("🚀 Page Vierge (Hub)")
    st.write("Tu es arrivé sur la page 2. Tu peux maintenant coder ce que tu veux ici !")
