

import streamlit as st

def display_appointment_form():
    st.subheader("📅 Prendre Rendez-vous avec le CUS")

    name = st.text_input("Nom complet")
    email = st.text_input("Adresse e-mail")
    date = st.date_input("Date souhaitée")
    message = st.text_area("Objet du rendez-vous")

    if st.button("Envoyer la demande"):
        if name and email and message:
            st.success(f"✅ Merci {name}, votre demande de rendez-vous a été soumise avec succès.")
        else:
            st.error("⚠️ Merci de remplir tous les champs avant de soumettre.")

