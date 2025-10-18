import streamlit as st

def display_proposal_form():
    st.subheader("💡 Soumettre une Proposition de Projet")

    name = st.text_input("Nom complet")
    email = st.text_input("Adresse e-mail")
    project_title = st.text_input("Titre du projet")
    description = st.text_area("Description du projet")

    if st.button("Soumettre la proposition"):
        if name and email and project_title and description:
            st.success("🚀 Merci ! Votre proposition a été soumise avec succès.")
        else:
            st.error("⚠️ Veuillez remplir tous les champs avant de soumettre.")
