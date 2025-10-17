# streamlit_app.py
import streamlit as st
from datetime import datetime
import pandas as pd
import io
import base64

# ----------------------------
# Configuration & Constantes
# ----------------------------
st.set_page_config(
    page_title="Assistant CUS AI – UM6P",
    page_icon=":compass:",
    layout="centered",
    initial_sidebar_state="expanded",
)

# --- Replace these URLs with your real logos (host them on GitHub / UM6P CDN / S3)
LOGO_UM6P = "https://raw.githubusercontent.com/Seyid2020/Assistant-CUS-AI/main/assets/um6p_logo.png"
LOGO_CUS = "https://raw.githubusercontent.com/Seyid2020/Assistant-CUS-AI/main/assets/cus_logo.png"
# If you don't have assets folder, either add them or replace with public URLs.

# Abacus chat appId (the one you provided)
ABACUS_APP_ID = "8b66e9b1e"
ABACUS_IFRAME = f"https://apps.abacus.ai/chatllm/?appId={ABACUS_APP_ID}&hideTopBar=2"

# UM6P primary color (used for borders / accents)
PRIMARY_COLOR = "#006666"

# ----------------------------
# Styles
# ----------------------------
st.markdown(
    f"""
    <style>
    /* General */
    .header {{
        text-align: center;
        padding: 6px 10px 4px 10px;
        margin-bottom: 8px;
    }}
    .app-title {{
        font-size:28px;
        font-weight:700;
        color:{PRIMARY_COLOR};
        margin-bottom:2px;
    }}
    .app-subtitle {{
        font-size:14px;
        color:#333333;
        margin-top:0;
    }}
    .card {{
        border: 1px solid #efefef;
        padding: 12px;
        border-radius: 10px;
        background: #ffffff;
        box-shadow: 0 2px 6px rgba(0,0,0,0.03);
    }}
    .logo-row {{
        display:flex;
        align-items:center;
        justify-content:center;
        gap:18px;
        margin-bottom:12px;
    }}
    .logo-img {{
        height:56px;
    }}
    /* iframe responsiveness in Streamlit */
    .iframe-container {{
        display:flex;
        justify-content:center;
    }}
    /* Sidebar link style */
    .sidebar-heading {{
        font-weight:700;
        color:{PRIMARY_COLOR};
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------
# Header
# ----------------------------
st.markdown("<div class='header'>", unsafe_allow_html=True)
st.markdown(
    """
    <div class="logo-row">
        <img class="logo-img" src="{logo_cus}" alt="CUS logo">
        <div>
            <div class="app-title">Assistant CUS AI</div>
            <div class="app-subtitle">Centre of Urban Systems — UM6P · Diagnostic urbain intelligent</div>
        </div>
        <img class="logo-img" src="{logo_um6p}" alt="UM6P logo">
    </div>
    """.format(logo_cus=LOGO_CUS, logo_um6p=LOGO_UM6P),
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.markdown(f"<div class='sidebar-heading'>Navigation</div>", unsafe_allow_html=True)
page = st.sidebar.radio("", ["Assistant", "Rendez-vous", "Propositions", "À propos"], index=0)

st.sidebar.markdown("---")
st.sidebar.markdown("🔗 Liens utiles")
st.sidebar.markdown("- [Centre of Urban Systems (CUS) — UM6P](https://www.um6p.ma/)")
st.sidebar.markdown("- [Publications CUS (Zenodo / Reports)](#)")
st.sidebar.markdown("- Contact : **cus@um6p.ma**")
st.sidebar.markdown("---")
st.sidebar.markdown("⚙️ Déploiement")
st.sidebar.markdown("- `appId`: " + ABACUS_APP_ID)
st.sidebar.markdown("- Status: Active")
st.sidebar.markdown("---")
st.sidebar.markdown("© Centre of Urban Systems — UM6P")

# ----------------------------
# Helper functions
# ----------------------------
def csv_download_link(df: pd.DataFrame, filename: str, link_text: str):
    """Create a link to download a dataframe as CSV"""
    csv = df.to_csv(index=False).encode("utf-8")
    b64 = base64.b64encode(csv).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{link_text}</a>'
    return href

def save_submission_local(df: pd.DataFrame, path="submissions.csv"):
    """Append submissions to a local CSV file (works in Streamlit Cloud too)."""
    try:
        # if exists, append; otherwise create
        existing = pd.read_csv(path)
        df_all = pd.concat([existing, df], ignore_index=True)
    except FileNotFoundError:
        df_all = df
    df_all.to_csv(path, index=False)
    return path

# ----------------------------
# Pages
# ----------------------------
if page == "Assistant":
    st.markdown("### 💬 Discussion — Assistant CUS AI")
    st.markdown(
        """
        <div class="card">
            <p>Posez vos questions sur le diagnostic urbain, les 7 dimensions, ou nos publications. L'Assistant utilise la base de connaissances CUS (RAG).</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # iframe (centered)
    st.markdown('<div class="iframe-container">', unsafe_allow_html=True)
    st.markdown(
        f"""
        <iframe
            src="{ABACUS_IFRAME}"
            width="820"
            height="700"
            style="border: 3px solid {PRIMARY_COLOR}; border-radius: 12px;"
        ></iframe>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Rendez-vous":
    st.markdown("### 📅 Prise de rendez-vous")
    st.markdown(
        """
        <div class="card">
            <p>Remplissez ce formulaire pour demander un rendez-vous (consultation, démonstration ou réunion). Vous pourrez télécharger la demande au format CSV. Pour intégration Google Calendar / Mail, voir les commentaires dans le code.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("rdv_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Nom et prénom", "")
            org = st.text_input("Organisation", "")
            email = st.text_input("Email de contact", "")
        with col2:
            phone = st.text_input("Téléphone", "")
            date = st.date_input("Date souhaitée", datetime.today())
            time = st.time_input("Heure souhaitée", datetime.now().time())
        purpose = st.selectbox("Objet du rendez-vous", ["Démonstration Outil", "Présentation Résultats", "Collaboration", "Autre"])
        notes = st.text_area("Informations complémentaires", "", max_chars=1000)
        submitted = st.form_submit_button("Envoyer la demande")

    if submitted:
        df = pd.DataFrame([{
            "timestamp": datetime.utcnow().isoformat(),
            "name": name,
            "organisation": org,
            "email": email,
            "phone": phone,
            "preferred_date": date.isoformat(),
            "preferred_time": time.isoformat(),
            "purpose": purpose,
            "notes": notes
        }])
        saved_path = save_submission_local(df, path="rdv_submissions.csv")
        st.success("✅ Demande enregistrée localement.")
        st.markdown(f"- Fichier sauvegardé : `{saved_path}`")
        st.markdown(csv_download_link(df, "rdv_request.csv", "⬇️ Télécharger la demande (CSV)"), unsafe_allow_html=True)

        st.info("⚠️ Optionnel : pour automatiser l'ajout au Google Calendar ou envoyer un email, intégrez l'API Google Calendar / SMTP (voir commentaires dans le code).")

elif page == "Propositions":
    st.markdown("### 💡 Propositions & Collaborations")
    st.markdown(
        """
        <div class="card">
            <p>Soumettez une proposition de collaboration, une idée de projet, ou téléchargez un document (PDF, DOCX).</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("proposal_form"):
        title = st.text_input("Titre du projet / proposition")
        contact = st.text_input("Contact (email)")
        category = st.selectbox("Catégorie", ["Recherche", "Pilotage", "Financement", "Autre"])
        summary = st.text_area("Résumé (200 mots max)", max_chars=2000)
        doc = st.file_uploader("Télécharger un document (optionnel)", type=["pdf", "docx", "xlsx"])
        submit_prop = st.form_submit_button("Soumettre la proposition")

    if submit_prop:
        dfp = pd.DataFrame([{
            "timestamp": datetime.utcnow().isoformat(),
            "title": title,
            "contact": contact,
            "category": category,
            "summary": summary,
            "filename": doc.name if doc else ""
        }])
        saved_path = save_submission_local(dfp, path="proposals_submissions.csv")
        st.success("✅ Proposition enregistrée localement.")
        st.markdown(f"- Fichier sauvegardé : `{saved_path}`")
        st.markdown(csv_download_link(dfp, "proposal_submission.csv", "⬇️ Télécharger la proposition (CSV)"), unsafe_allow_html=True)
        if doc:
            st.success(f"📎 Document reçu : {doc.name} (taille: {doc.size} octets)")
            # store file if needed
            # with open("uploads/" + doc.name, "wb") as f:
            #     f.write(doc.getbuffer())

elif page == "À propos":
    st.markdown("### ℹ️ À propos — Centre of Urban Systems (CUS)")
    st.markdown(
        """
        <div class="card">
            <p><strong>Mission:</strong> Rendre le diagnostic urbain rapide, accessible et contextualisé pour les municipalités, bailleurs et cabinets en Afrique.</p>
            <p><strong>Contact:</strong> cus@um6p.ma</p>
            <p><strong>Auteurs & équipe:</strong> Centre of Urban Systems - UM6P</p>
            <p><strong>Remarque technique:</strong> L'Assistant CUS est servi par Abacus.AI (RAG). Pour une intégration complète (Google Calendar, Gmail, Google Sheets), décommentez et configurez les fonctions indiquées dans le code.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ----------------------------
# Footer (small)
# ----------------------------
st.markdown("---")
st.markdown(
    """
    <div style="text-align:center; font-size:12px; color:#555;">
        Développé pour le Centre of Urban Systems — UM6P · Assistant CUS AI · {year}
    </div>
    """.format(year=datetime.now().year),
    unsafe_allow_html=True,
)
