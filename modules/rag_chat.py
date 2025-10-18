import streamlit as st

def display_chat_interface():
    st.header("🤖 Chat Intelligent")
    user_input = st.text_input("Posez votre question ici :")
    if user_input:
        # Ici, tu peux intégrer ta logique RAG ou une réponse simulée pour l'instant
        st.markdown(f"**Réponse simulée:** Vous avez demandé : {user_input}")

