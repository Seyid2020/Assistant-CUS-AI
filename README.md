
# 🏙️ Application CUS - Centre for Urban Systems

Application Streamlit professionnelle pour le Centre for Urban Systems (CUS) de l'Université Mohammed VI Polytechnique (UM6P).

## 📋 Fonctionnalités

### 🤖 Chat Intelligent (RAG)
- Système de questions-réponses basé sur la base de connaissances du CUS
- Recherche sémantique dans la documentation
- Citations de sources
- Interface conversationnelle en français

### 📅 Prise de Rendez-vous
- Formulaire de demande de rendez-vous
- Intégration automatique avec Google Calendar
- Notifications email automatiques
- Récapitulatif et confirmation

### 💡 Collecte de Propositions
- Formulaire de soumission de propositions de collaboration
- Enregistrement automatique dans Google Sheets
- Catégorisation par type de proposition
- Notifications email pour chaque soumission

### 📧 Notifications Email
- Envoi automatique via Gmail
- Templates HTML professionnels
- Notifications pour rendez-vous et propositions

## 🚀 Installation et Déploiement

### Prérequis

- Python 3.9 ou supérieur
- Compte Google avec accès aux APIs (Calendar, Sheets, Gmail)
- Tokens OAuth configurés

### Installation locale

1. **Cloner le projet**
```bash
cd /home/ubuntu/code_artifacts/cus-streamlit-app
```

2. **Créer un environnement virtuel**
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Configuration**

Créer un fichier `.streamlit/secrets.toml` avec:
```toml
NOTIFICATION_EMAIL = "seyidebnou@gmail.com"
```

5. **Lancer l'application**
```bash
streamlit run app.py
```

L'application sera accessible sur `http://localhost:8501`

## ☁️ Déploiement sur Streamlit Cloud

### Étape 1: Préparer le repository

1. Initialiser git (si ce n'est pas déjà fait):
```bash
git init
git add .
git commit -m "Initial commit - CUS Streamlit App"
```

2. Créer un repository sur GitHub et pusher le code:
```bash
git remote add origin https://github.com/votre-username/cus-streamlit-app.git
git push -u origin main
```

### Étape 2: Déployer sur Streamlit Cloud

1. Aller sur [share.streamlit.io](https://share.streamlit.io)
2. Se connecter avec GitHub
3. Cliquer sur "New app"
4. Sélectionner le repository `cus-streamlit-app`
5. Définir:
   - Main file path: `app.py`
   - Python version: 3.9

### Étape 3: Configurer les Secrets

Dans les paramètres de l'app sur Streamlit Cloud, ajouter dans "Secrets":

```toml
NOTIFICATION_EMAIL = "seyidebnou@gmail.com"

# Pour l'authentification Google (si nécessaire)
[google_credentials]
# Copier le contenu de votre fichier credentials.json
```

### Étape 4: Configuration Google OAuth

Pour que l'application accède aux services Google (Calendar, Sheets, Gmail):

1. **Google Cloud Console** ([console.cloud.google.com](https://console.cloud.google.com))
   - Créer un nouveau projet
   - Activer les APIs: Calendar, Sheets, Gmail
   - Créer des credentials OAuth 2.0
   - Télécharger le fichier `credentials.json`

2. **Configurer les scopes nécessaires**:
   - `https://www.googleapis.com/auth/calendar`
   - `https://www.googleapis.com/auth/spreadsheets`
   - `https://www.googleapis.com/auth/gmail.send`

3. **Note importante**: 
   - Pour le déploiement public, envisager d'utiliser un service backend séparé pour gérer l'authentification OAuth
   - Les tokens OAuth ne doivent jamais être commités dans le code
   - Utiliser les secrets de Streamlit Cloud pour stocker les credentials

## 📁 Structure du Projet

```
cus-streamlit-app/
├── app.py                      # Application principale
├── config.py                   # Configuration générale
├── requirements.txt            # Dépendances Python
├── README.md                   # Documentation
├── .streamlit/
│   └── config.toml            # Configuration Streamlit
├── data/
│   └── cus_knowledge.txt      # Base de connaissances
├── modules/
│   ├── __init__.py
│   ├── rag_chat.py            # Module de chat RAG
│   ├── appointment.py         # Module de rendez-vous
│   ├── proposal.py            # Module de propositions
│   └── google_services.py     # Intégration Google APIs
└── assets/
    └── logo_cus.png           # Logo du CUS (à ajouter)
```

## 🔧 Configuration

### Variables d'environnement

- `NOTIFICATION_EMAIL`: Email pour recevoir les notifications (par défaut: seyidebnou@gmail.com)
- `GOOGLE_CREDENTIALS_PATH`: Chemin vers les credentials Google OAuth

### Fichiers de configuration

- `.streamlit/config.toml`: Configuration Streamlit (thème, options)
- `config.py`: Configuration de l'application (types de rendez-vous, propositions, etc.)

## 🛠️ Technologies Utilisées

- **Streamlit**: Framework web Python
- **scikit-learn**: RAG et recherche sémantique (TF-IDF)
- **Google APIs**: Calendar, Sheets, Gmail
- **Python 3.9+**: Langage de programmation

## 📝 Utilisation

### Chat Intelligent

1. Accéder à l'onglet "🤖 Chat Intelligent"
2. Poser une question sur le CUS
3. Le système recherche dans la base de connaissances
4. Affiche la réponse avec les sources

### Prise de Rendez-vous

1. Accéder à l'onglet "📅 Prendre Rendez-vous"
2. Remplir le formulaire:
   - Informations personnelles
   - Date et heure souhaitées
   - Type et description du rendez-vous
3. Soumettre la demande
4. Recevoir une confirmation

### Soumettre une Proposition

1. Accéder à l'onglet "💡 Soumettre une Proposition"
2. Remplir le formulaire:
   - Informations personnelles et organisation
   - Type de proposition
   - Description détaillée
   - Domaines d'intérêt
3. Soumettre la proposition
4. Recevoir une confirmation

## 🔐 Sécurité

- Les tokens OAuth sont stockés de manière sécurisée
- Validation des emails
- Protection contre les injections
- Gestion des erreurs gracieuse

## 🐛 Dépannage

### L'application ne démarre pas

Vérifier que toutes les dépendances sont installées:
```bash
pip install -r requirements.txt
```

### Erreur d'authentification Google

Vérifier que:
- Les APIs sont activées dans Google Cloud Console
- Les credentials OAuth sont correctement configurés
- Les scopes nécessaires sont autorisés

### Le chat ne répond pas

Vérifier que:
- Le fichier `data/cus_knowledge.txt` existe
- Le fichier n'est pas vide
- Les permissions de lecture sont correctes

## 📞 Contact et Support

Pour toute question ou assistance:

- **Email**: seyidebnou@gmail.com
- **Site web**: [cus.um6p.ma](https://cus.um6p.ma)
- **Organisation**: Centre for Urban Systems, UM6P

## 📄 Licence

© 2024 Centre for Urban Systems - UM6P. Tous droits réservés.

## 🙏 Remerciements

Développé pour le Centre for Urban Systems de l'Université Mohammed VI Polytechnique.

---

**Version**: 1.0.0  
**Dernière mise à jour**: Octobre 2024  
**Statut**: Production Ready ✅
