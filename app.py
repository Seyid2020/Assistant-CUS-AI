
import streamlit as st
import os
from pathlib import Path
from modules.rag_chat import display_chat_interface
from modules.appointment import display_appointment_form
from modules.proposal import display_proposal_form

# Configuration de la page
st.set_page_config(
    page_title="Centre for Urban Systems - CUS",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé pour un design professionnel
st.markdown("""
    <style>
    /* Style général */
    .main {
        padding: 0rem 1rem;
    }
    
    /* En-tête principal */
    .header-container {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .header-title {
        color: white;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
        text-align: center;
    }
    
    .header-subtitle {
        color: #e0e0e0;
        font-size: 1.2rem;
        text-align: center;
    }
    
    /* Cartes de navigation */
    .nav-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #2a5298;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
        transition: transform 0.3s ease;
    }
    
    .nav-card:hover {
        transform: translateX(5px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }
    
    /* Messages de succès et d'erreur */
    .stAlert {
        border-radius: 10px;
    }
    
    /* Boutons */
    .stButton>button {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    /* Champs de formulaire */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        border-radius: 5px;
        border: 2px solid #e0e0e0;
    }
    
    .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {
        border-color: #2a5298;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background-color: #f8f9fa;
    }
    
    /* Section de chat */
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
    
    .user-message {
        background-color: #e3f2fd;
        border-left: 4px solid #2196f3;
    }
    
    .assistant-message {
        background-color: #f5f5f5;
        border-left: 4px solid #2a5298;
    }
    </style>
""", unsafe_allow_html=True)

def main():
    # En-tête avec logo
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
            <div class="header-container">
                <div class="header-title">🏙️ Centre for Urban Systems</div>
                <div class="header-subtitle">UM6P - Innovation & Recherche Urbaine</div>
            </div>
        """, unsafe_allow_html=True)
    
    # Sidebar pour la navigation
    with st.sidebar:
        st.markdown("### 📋 Navigation")
        st.markdown("---")
        
        page = st.radio(
            "",
            ["🤖 Chat Intelligent", "📅 Prendre Rendez-vous", "💡 Soumettre une Proposition"],
            label_visibility="collapsed"
        )
        
        st.markdown("---")
        st.markdown("### ℹ️ À propos")
        st.markdown("""
        Le **Centre for Urban Systems (CUS)** de l'UM6P est dédié à la recherche, 
        à l'éducation et à l'innovation dans le domaine des sciences urbaines.
        
        **Nos piliers:**
        - 🔬 Recherche
        - 🎓 Éducation  
        - 💼 Expertise
        - 🚀 Innovation
        """)
        
        st.markdown("---")
        st.markdown("### 📞 Contact")
        st.markdown("📧 seyidebnou@gmail.com")
        st.markdown("🌐 [cus.um6p.ma](https://cus.um6p.ma)")
    
    # Affichage de la page sélectionnée
    if page == "🤖 Chat Intelligent":
        display_chat_interface()
    elif page == "📅 Prendre Rendez-vous":
        display_appointment_form()
    elif page == "💡 Soumettre une Proposition":
        display_proposal_form()

if __name__ == "__main__":
    main()
