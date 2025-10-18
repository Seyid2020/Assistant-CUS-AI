import streamlit as st

def display_chat_interface():
    st.header("🤖 Chat Intelligent")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []  # Historique des messages

    user_input = st.text_input("Posez votre question ici :", key="user_input")

    if user_input:
        # Ajouter la question de l'utilisateur à l'historique
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Générer une réponse simulée
        response = f"Réponse simulée: Vous avez demandé : {user_input}"
        st.session_state.messages.append({"role": "assistant", "content": response})

    # Afficher l'historique complet
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"**Vous :** {msg['content']}")
        else:
            st.markdown(f"**Assistant :** {msg['content']}")
