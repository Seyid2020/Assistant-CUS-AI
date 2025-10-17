
import os

# Configuration de l'application
APP_NAME = "CUS Assistant"
APP_VERSION = "1.0.0"

# Email de notification
NOTIFICATION_EMAIL = "seyidebnou@gmail.com"

# Chemins des fichiers
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
KNOWLEDGE_FILE = os.path.join(DATA_DIR, "cus_knowledge.txt")

# Configuration OAuth Google
# Les tokens OAuth sont stockés dans /home/ubuntu/.config/abacusai_auth_secrets.json
# et seront gérés par les outils Google de la plateforme
GOOGLE_CREDENTIALS_PATH = "/home/ubuntu/.config/abacusai_auth_secrets.json"

# Configuration du RAG
EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
TOP_K_RESULTS = 3
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# Configuration Google Sheets pour les propositions
PROPOSALS_SHEET_NAME = "CUS_Propositions"
PROPOSALS_SHEET_HEADERS = [
    "Date de soumission",
    "Nom",
    "Email",
    "Organisation",
    "Type de proposition",
    "Description",
    "Statut"
]

# Types de rendez-vous disponibles
APPOINTMENT_TYPES = [
    "Consultation générale",
    "Collaboration recherche",
    "Visite du centre",
    "Présentation de projet",
    "Formation",
    "Autre"
]

# Types de propositions disponibles
PROPOSAL_TYPES = [
    "Collaboration académique",
    "Partenariat industriel",
    "Projet de recherche",
    "Stage/Formation",
    "Living Lab",
    "Autre"
]

# Couleurs du thème CUS
THEME_COLORS = {
    "primary": "#1e3c72",
    "secondary": "#2a5298",
    "accent": "#4a90e2",
    "success": "#4caf50",
    "warning": "#ff9800",
    "error": "#f44336"
}
