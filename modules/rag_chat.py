import streamlit as st

def display_chat_interface():
    st.subheader("💬 Assistant Intelligent CUS")
    st.info("Cet assistant répond à vos questions sur les projets, les indicateurs urbains et les activités du Centre for Urban Systems.")

    user_input = st.text_input("Posez votre question ici :")

    if user_input:
        st.write("🤖 Réponse : Merci pour votre question ! Le moteur d’intelligence CUS l’analysera prochainement.")

