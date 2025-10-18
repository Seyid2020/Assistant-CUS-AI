
import streamlit as st

def display_appointment_form():
    st.header("📅 Prendre Rendez-vous")
    
    name = st.text_input("Nom complet")
    email = st.text_input("Email")
    date = st.date_input("Date du rendez-vous")
    time = st.time_input("Heure du rendez-vous")
    reason = st.text_area("Objet du rendez-vous")
    
    if st.button("Soumettre"):
        st.success(f"Rendez-vous enregistré pour {name} le {date} à {time}.")


