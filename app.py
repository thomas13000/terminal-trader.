import streamlit as st

st.set_page_config(
    page_title="TERMINAL TRADER PRO",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Gestion de l'état de la page dans Streamlit
if "page" not in st.session_state:
    st.session_state.page = "welcome"

# ==========================================
# PAGE 1 : WELCOME SCREEN
# ==========================================
if st.session_state.page == "welcome":
    
    # Injection du CSS global dans le DOM principal de Streamlit
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;900&family=JetBrains+Mono:wght@400;600;700;800&family=Orbitron:wght@500;700;900&display=swap');

            header, footer, [data-testid="stHeader"] { 
                display: none !important; 
                visibility: hidden !important; 
            }
            
            html, body, .stApp {
                background-color: #080b10 !important;
                overflow: hidden !important;
                color: #eaecef !important;
                font-family: 'Inter', sans-serif !important;
            }

            /* Arrière-plan du Globe 3D */
            .globe-iframe {
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw;
                height: 100vh;
                border: none;
                z-index: 0;
            }

            /* Overlay HUD */
            .hud-grid-overlay {
                position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 1; pointer-events: none;
                background: 
                    radial-gradient(circle at 50% 50%, transparent 35%, rgba(8, 11, 16, 0.88) 90%),
                    linear-gradient(to right, rgba(255,255,255,0.015) 1px, transparent 1px),
                    linear-gradient(to bottom, rgba(255,255,255,0.015) 1px, transparent 1px);
                background-size: 100% 100%, 50px 50px, 50px 50px;
            }

            .corner-reticle {
                position: fixed; width: 36px; height: 36px; z-index: 10; pointer-events: none;
                border: 2px solid rgba(240, 185, 11, 0.4);
            }
            .corner-tl { top: 20px; left: 20px; border-right: none; border-bottom: none; }
            .corner-tr { top: 20px; right: 20px; border-left: none; border-bottom: none; }
            .corner-bl { bottom: 20px; left: 20px; border-right: none; border-top: none; }
            .corner-br { bottom: 20px; right: 20px; border-left: none; border-top: none; }

            /* Panneau Gauche */
            .left-hero-panel {
                position: fixed; top: 105px; left: 40px; width: 380px; z-index: 20;
                background: rgba(13, 17, 23, 0.82); border: 1px solid rgba(240, 185, 11, 0.25); border-radius: 18px;
                padding: 26px; backdrop-filter: blur(20px); box-shadow: 0 10px 40px rgba(0, 0, 0, 0.7);
                display: flex; flex-direction: column; gap: 18px;
            }

            .panel-badge {
                display: inline-flex; align-items: center; gap: 8px; font-family: 'JetBrains Mono', monospace;
                font-size: 0.65rem; font-weight: 700; letter-spacing: 2px; color: #f0b90b;
                background: rgba(240, 185, 11, 0.1); padding: 5px 12px; border-radius: 20px;
                border: 1px solid rgba(240, 185, 11, 0.3); width: fit-content;
            }

            .clock-section {
                display: grid; grid-template-columns: 1fr 1fr; gap: 12px;
                background: rgba(8, 11, 16, 0.6); border: 1px solid rgba(255, 255, 255, 0.08);
                border-radius: 12px; padding: 12px;
            }
            .clock-block { display: flex; flex-direction: column; }
            .clock-label { font-family: 'JetBrains Mono', monospace; font-size: 0.62rem; color: #848e9c; letter-spacing: 1px; }
            .clock-time { font-family: 'JetBrains Mono', monospace; font-size: 1.4rem; font-weight: 800; color: #fff; }

            /* Style personnalisé du vrai bouton Streamlit */
            div.stButton > button {
                width: 100% !important;
                background: linear-gradient(135deg, #f0b90b 0%, #d4a007 100%) !important;
                color: #080b10 !important;
                font-family: 'Orbitron', sans-serif !important;
                font-size: 0.85rem !important;
                font-weight: 900 !important;
                letter-spacing: 2px !important;
                border-radius: 12px !important;
                padding: 16px 20px !important;
                border: none !important;
                box-shadow: 0 0 25px rgba(240, 185, 11, 0.45) !important;
                cursor: pointer !important;
                transition: all 0.3s ease !important;
            }
            div.stButton > button:hover {
                transform: translateY(-2px) scale(1.01) !important;
                box-shadow: 0 0 35px rgba(240, 185, 11, 0.7) !important;
                color: #000000 !important;
            }
        </style>

        <div class="hud-grid-overlay"></div>
        <div class="corner-reticle corner-tl"></div>
        <div class="corner-reticle corner-tr"></div>
        <div class="corner-reticle corner-bl"></div>
        <div class="corner-reticle corner-br"></div>
    """, unsafe_allow_html=True)

    # 1. Globe 3D en arrière-plan (Iframe)
    globe_code = """
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <style>
            body { margin: 0; overflow: hidden; background: #080b10; }
            canvas { width: 100vw; height: 100vh; display: block; }
        </style>
    </head>
    <body>
        <canvas id="canvas"></canvas>
        <script>
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.z = 25;
            const renderer = new THREE.WebGLRenderer({ canvas: document.getElementById('canvas'), antialias: true });
            renderer.setSize(window.innerWidth, window.innerHeight);

            const geo = new THREE.SphereGeometry(8, 32, 32);
            const mat = new THREE.MeshBasicMaterial({ color: 0xf0b90b, wireframe: true, transparent: true, opacity: 0.6 });
            const sphere = new THREE.Mesh(geo, mat);
            scene.add(sphere);

            function animate() {
                requestAnimationFrame(animate);
                sphere.rotation.y += 0.003;
                renderer.render(scene, camera);
            }
            animate();
            window.addEventListener('resize', () => {
                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, window.innerHeight);
            });
        </script>
    </body>
    </html>
    """
    st.components.v1.html(globe_code, height=1000)

    # 2. Structure HUD & Bouton natif Streamlit
    with st.container():
        st.markdown("""
            <div class="left-hero-panel">
                <div class="panel-badge">● SESSION EN DIRECT</div>
                <div class="clock-section">
                    <div class="clock-block">
                        <span class="clock-label">TERMINAL</span>
                        <span class="clock-time">READY</span>
                    </div>
                    <div class="clock-block">
                        <span class="clock-label">STATUS</span>
                        <span class="clock-time" style="color:#0ecb81;">ONLINE</span>
                    </div>
                </div>
        """, unsafe_allow_html=True)
        
        # Le bouton natif qui contrôle directement Python
        if st.button("ENTRER DANS LE TERMINAL ➔"):
            st.session_state.page = "hub"
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# PAGE 2 : PAGE VIERGE (HUB)
# ==========================================
elif st.session_state.page == "hub":
    
    st.markdown("""
        <style>
            header[data-testid="stHeader"], footer { visibility: hidden !important; }
            .stApp { background-color: #080b10 !important; color: #eaecef !important; }
        </style>
    """, unsafe_allow_html=True)

    if st.button("← Retour au Globe"):
        st.session_state.page = "welcome"
        st.rerun()

    st.title("🚀 Page Vierge (Hub)")
    st.write("Le passage à la page 2 fonctionne désormais instantanément !")
