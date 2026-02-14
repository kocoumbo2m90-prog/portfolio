import streamlit as st
from datetime import datetime
import pandas as pd
import base64

# Configuration de la page
st.set_page_config(
    page_title="Portfolio - Malick MANE",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Charger et encoder l'image de fond
try:
    with open("imagecv.jpg", "rb") as f:
        img_data = base64.b64encode(f.read()).decode()
        bg_image = f"data:image/jpeg;base64,{img_data}"
except:
    bg_image = ""

# CSS personnalisé avec image de fond
st.markdown(f"""
<style>
    * {{
        font-family: Arial, sans-serif;
    }}
    .stApp {{
        /* Superposition semi-transparente + image de fond pour atténuer l'image */
        background-image: linear-gradient(rgba(255,255,255,0.6), rgba(255,255,255,0.6)), url('{bg_image}');
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }}
    body {{
        background-color: transparent;
        color: #333;
        font-size: 1.1rem;
    }}
    .main {{
        background-color: transparent;
    }}
    .main-header {{
        text-align: center;
        padding: 2rem 0;
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 0;
        color: #000;
        margin-bottom: 2rem;
        border-bottom: 2px solid #e0e0e0;
    }}
    .main-header h1 {{
        margin: 0;
        font-size: 3.2rem;
        font-weight: 700;
        letter-spacing: 1px;
    }}
    .main-header p {{
        margin: 0.5rem 0 0 0;
        font-size: 1.3rem;
        opacity: 0.7;
        font-weight: 500;
        letter-spacing: 0.5px;
    }}
    .section-title {{
        font-size: 1.8rem;
        font-weight: 700;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-left: 4px solid #000;
        padding-left: 1rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #000;
    }}
    .experience-card {{
        background: rgba(255, 255, 255, 0.95);
        padding: 1.5rem;
        border-radius: 0;
        margin: 1rem 0;
        border-left: 3px solid #999;
        border-bottom: 1px solid #e0e0e0;
    }}
    .experience-card h4 {{
        margin: 0 0 0.5rem 0;
        font-size: 1.3rem;
        font-weight: 700;
        color: #000;
    }}
    .experience-card p {{
        margin: 0.3rem 0;
        font-size: 1.05rem;
        color: #666;
    }}
    .stat-box {{
        background: rgba(255, 255, 255, 0.95);
        color: #000;
        padding: 1.5rem;
        border-radius: 0;
        text-align: center;
        margin: 0.5rem;
        border: 1px solid #e0e0e0;
    }}
    .stat-box h3 {{
        margin: 0;
        font-size: 2.5rem;
        font-weight: 700;
        color: #000;
    }}
    .stat-box p {{
        margin: 0.5rem 0 0 0;
        opacity: 0.7;
        font-size: 1rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}
    [data-testid="stTabs"] {{
        font-size: 1.3rem !important;
    }}
    [data-testid="stTabs"] h4 {{
        font-size: 1.4rem !important;
        font-weight: 700 !important;
        color: #000 !important;
    }}
    [data-testid="stTabs"] p {{
        font-size: 1.15rem !important;
        color: #333 !important;
    }}
    .skill-list {{
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
    }}
    .skill-item {{
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }}
    .skill-dot {{
        width: 8px;
        height: 8px;
        background-color: #000;
        border-radius: 50%;
    }}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### 📋 INFORMATIONS")
    st.markdown("---")
    
    try:
        st.image("kocoumbo.jpg", caption='Malick MANE', width=200)
    except:
        st.info("📸 Photo non disponible")
    
    st.markdown("**📍 LOCALISATION**")
    st.write("Dakar, Sénégal")
    
    st.markdown("**📞 CONTACT**")
    st.write("Tel: +221 772 414 357")
    st.write("Email: kocoumbo2m90@gmail.com")
    
    st.markdown("---")
    st.markdown("**🗣️ LANGUES**")
    st.write("🇫🇷 Français: Avancé")
    st.write("🇬🇧 Anglais: Courant")
    st.write("🇩🇪 Allemand: Moyen")
    
    st.markdown("---")
    st.markdown("**⭐ STATUT**")
    st.write("Sous-Officier Supérieur\nArmée de Terre")

# En-tête principal
st.markdown("""
<div class="main-header">
    <h1>MALICK MANE</h1>
    <p>Sous-Officier Supérieur | Technicien Superieur en Transport-logistique et Transit | Gestionnaire d'Entreprise | Géomaticien</p>
</div>
""", unsafe_allow_html=True)

# Statistiques clés
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
    <div class="stat-box">
        <h3>15+</h3>
        <p>ANNÉES D'EXPÉRIENCE</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="stat-box">
        <h3>5</h3>
        <p>DOMAINES DE COMPÉTENCE</p>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="stat-box">
        <h3>8</h3>
        <p>DIPLÔMES & CERTIFICATS</p>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown("""
    <div class="stat-box">
        <h3>3</h3>
        <p>LANGUES MAÎTRISÉES</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# À propos
st.markdown('<div class="section-title">👤 À Propos</div>', unsafe_allow_html=True)
st.markdown("""
Issu de la **34ème promotion** de l'École Nationale des Sous-Officiers d'Active (ENSOA/Kaolack), 
je suis actuellement **Sous-Officier Supérieur** dans l'Armée de Terre sénégalaise. 

Mon parcours professionnel diversifié m'a permis d'acquérir des compétences dans plusieurs domaines:

- 🎓 **Technicien Supérieur** en Transport Logistique et Transit
- 🏢 **Ingénieur** en Gestion des Entreprises
- 🗺️ **Technicien Supérieur** en Géomatique
- ⚔️ **Sous-Officier Militaire** spécialisé en Renseignement
""")

st.markdown("---")

# Onglets principaux
tab1, tab2, tab3, tab4, tab5 = st.tabs(["FORMATIONS", "EXPÉRIENCES", "COMPÉTENCES", "RÉALISATIONS", "PROJETS"])

# Tab 1: Formations
with tab1:
    st.markdown('<div class="section-title">🎓 Formation et Diplômes</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🎖️ Formations Militaires")
        formations_mil = [
            ("2023", "Certification Opérateur Mini-Drone", "Armée de Terre"),
            ("2019", "Brevet de Spécialité N°1 RENSEIGNEMENT", "Armée de Terre"),
            ("2017", "Certificat d’Aptitude technique N°2 TRAIN", "Armée de Terre"),
            ("2016", "Certificat Inter-Arme (CIA)", "ENSOA"),
            ("2016", "DAGSOA (Diplôme Aptitude Grade SoA)", "Armée de Terre"),
            ("2015", "Brevet Parachutiste", "École Militaire"),
            ("2015", "Brevet Commando", "École Militaire"),
            ("2014-2016", "Formation Sous-Officiers Armée", "ENSOA Kaolack"),
        ]
        for year, diploma, institution in formations_mil:
            st.write(f"✓ **{year}** - {diploma}")
            st.caption(f"📍 {institution}")
            st.write("")
    
    with col2:
        st.markdown("#### 📚 Formations Académiques")
        formations_acad = [
            ("2023", "Licence Gestion des Entreprises", "ISM Ziguinchor"),
            ("2013", "BTS Transport et Logistique", "ITECOM"),
            ("2013", "DTS Transport-Logistique/Douane", "ITECOM"),
            ("2013", "Bac+3 Anglais", "UCAD"),
            ("2010", "Baccalauréat Série L2", "Lycée Seydina Limamoulaye"),
            
        ]
        for year, diploma, institution in formations_acad:
            st.write(f"✓ **{year}** - {diploma}")
            st.caption(f"📍 {institution}")
            st.write("")

# Tab 2: Expériences
with tab2:
    st.markdown('<div class="section-title">💼 Expériences Professionnelles</div>', unsafe_allow_html=True)
    
    experiences = [
        {
            "period": "2020-2022",
            "title": "Sous-Officier Renseignement",
            "company": "Zone Militaire N°5 (Casamance/Ziguinchor)",
            "tasks": [
                "Analyse et exploitation de données militaires opérationnelles",
                "Mise à jour de bases de données sensibles",
                "Chef de groupe - Mission DETSEN 7 MICEGA en Gambie",
                "Sécurité du Président Gambien (Palais Présidentiel, Banjul)"
            ]
        },
        {
            "period": "2019-2020",
            "title": "Adjudant Centre FRAC",
            "company": "Bataillon du TRAIN",
            "tasks": [
                "Suivi et contrôle du personnel en formation",
                "Formation à la conduite (poids lourd, léger, VIP)",
                "Gestion des stagiaires militaires"
            ]
        },
        {
            "period": "2017-2019",
            "title": "Encadreur",
            "company": "ENSOA (37e Promotion)",
            "tasks": [
                "Formation des nouveaux sous-officiers",
                "Gradé de contact pour la promotion",
                "Instruction militaire générale"
            ]
        },
        {
            "period": "2016-2017",
            "title": "Chef de Peloton Transport",
            "company": "Bataillon du TRAIN",
            "tasks": [
                "Gestion logistique de transport de personnel",
                "Missions de ventilation inter-zones",
                "Soutien logistique opérationnel"
            ]
        },
        {
            "period": "2012-2013",
            "title": "Responsable Entrepôt Industriel",
            "company": "SIGELEC",
            "tasks": [
                "Gestion du régime suspensif (S32O/C303)",
                "Fabrication de piles HELLESSENS R6 et R20",
                "Suivi des stocks et inventaires"
            ]
        },
        {
            "period": "2013",
            "title": "Opérateur de Saisie",
            "company": "People No Limite (PNL)",
            "tasks": [
                "6ème édition d'Africités",
                "Gestion des données événementielles"
            ]
        }
    ]
    
    for exp in experiences:
        with st.container():
            st.markdown(f"""
            <div class="experience-card">
                <h4>{exp['title']}</h4>
                <p><strong>Période:</strong> {exp['period']}</p>
                <p><strong>Entreprise:</strong> {exp['company']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.write("**Responsabilités:**")
            for task in exp['tasks']:
                st.write(f"• {task}")
            st.write("")

# Tab 3: Compétences
with tab3:
    st.markdown('<div class="section-title">🛠️ Compétences Professionnelles</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### ⚙️ Logistique & Transport")
        st.markdown("""
        - Gestion de stocks de matières premières
        - Suivi des sommiers et inventaires
        - Régularisation douane des produits importés
        - Mise à la consommation produits finis
        - Gestion de flotte de transport
        """)
        
        st.markdown("### ⚔️ Compétences Militaires")
        st.markdown("""
        - Chef de Section Infanterie
        - Chef de Peloton Transport
        - Technicien Renseignement Militaire Opérationnel
        - Opérateur Mini-Drone
        - Chef Bureau Opérations & Instruction
        """)
        
        st.markdown("### 🏢 Gestion & Management")
        st.markdown("""
        - Travail en équipe
        - Conception de projets
        - Pilotage et suivi de projets
        - Création d'entreprise
        - Gestion Ressources Humaines
        - Comptabilité
        """)
    
    with col2:
        st.markdown("### 🗺️ Géomatique")
        st.markdown("""
        - ArcGIS (Création cartes thématiques)
        - QGIS (Gestion bases données géographiques)
        - Topographie et levés topographiques
        - AutoCAD
        - SketchUp
        - Analyse spatiale
        """)
        
        st.markdown("### 💻 Informatique & Tech")
        st.markdown("""
        - Suite bureautique Microsoft Office
        - Python & Streamlit
        - Pandas & Analyse données
        - Bases de données SQL
        - Systèmes d'exploitation (Windows, Linux)
        """)
        
        st.markdown("### 📅 Soft Skills")
        st.markdown("""
        - Leadership et commandement
        - Communication interculturelle
        - Résolution de problèmes
        - Adaptabilité aux changements
        - Prise de décision
        """)

# Tab 4: Réalisations
with tab4:
    st.markdown('<div class="section-title">🏆 Réalisations Majeures</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🎖️ Missions & Déploiements")
        st.info("""
        **Mission DETSEN 7 MICEGA (2023-2024)**
        - Chef de groupe 3e section compagnie mecanisé lors mission CEDEAO en Gambie
        - Assurer la sécurité du Président Gambien Adama BARRO
        - Opérations de sécurisation Palais Présidentiel de Banjul
        - **Lettre de félicitations reçue**
        """)
        
        st.success("""
        **Leadership en Formation**
        - Encadrement de 150+ sous-officiers
        - 37e promotion ENSOA (2017-2019)
        - Taux de réussite: 95%+
        """)
    
    with col2:
        st.markdown("### 📊 Projets Réussis")
        st.warning("""
        **Gestion Logistique Optimisée**
        - Réduction coûts transport: -25%
        - Amélioration délais livraison
        - Digitalisation processus
        """)
        
        st.info("""
        **Formation à la Conduite**
        - Formation de 500+ conducteurs
        - Zéro accident en mission
        - Certification VIP driving
        """)

# Tab 5: Projets
with tab5:
    st.markdown('<div class="section-title">📊 Projets en Cours & Portfolio Technique</div>', unsafe_allow_html=True)
    
    st.markdown("### 🔨 Projets de Développement")
    
    project1 = st.container()
    with project1:
        st.markdown("#### 📱 Portfolio Streamlit (Ce projet!)")
        st.write("""
        Développement d'un portfolio interactif en Python avec Streamlit pour présenter
        mon expérience multidomaine de manière moderne et professionnelle.
        """)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Langage", "Python")
        with col2:
            st.metric("Framework", "Streamlit")
        with col3:
            st.metric("Statut", "✅ Actif")
    
    st.markdown("---")
    
    st.markdown("### 🎓 Domaines d'Intérêt")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        #### 🗺️ SIG & Géomatique
        - Applications cartographiques
        - Analyse spatiale
        - Télédétection
        - Gestion données géospatiales
        """)
    
    with col2:
        st.markdown("""
        #### 📊 Data & Analytics
        - Analyse de données
        - Visualisation
        - Business Intelligence
        - Reporting automatisé
        """)
    
    with col3:
        st.markdown("""
        #### 🚀 Web & Apps
        - Applications Python
        - Interfaces Streamlit
        - Automation scripts
        - Outils bureautiques
        """)

st.markdown("---")

# Footer
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("**📧 Email**\nkocoumbo2m90@gmail.com")
with col2:
    st.markdown("**📞 Téléphone**\n+221 772 414 357")
with col3:
    st.markdown("**📍 Localisation**\nDakar, Sénégal")

st.markdown("---")
st.markdown("""
<p style="text-align: center; color: #999; font-size: 0.9rem;">
    © 2026 Malick MANE | Portfolio Professionnel
</p>
""", unsafe_allow_html=True)
