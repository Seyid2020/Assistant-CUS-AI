import streamlit as st

def get_answer_from_knowledge(question):
    # Ouvre le fichier de connaissance
    with open("data/cus_knowledge.txt", "r", encoding="utf-8") as f:
        knowledge = f.read()
    
    # Recherche simple : si une phrase du fichier contient un mot clé de la question
    for line in knowledge.split("\n"):
        if question.lower() in line.lower():
            return line
    return "Désolé, je n'ai pas trouvé de réponse dans la base de connaissances."

def display_chat_interface():
    st.header("🤖 Chat Intelligent")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    user_input = st.text_input("Posez votre question ici :", key="user_input")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Cherche une réponse réelle
        response = get_answer_from_knowledge(user_input)
        st.session_state.messages.append({"role": "assistant", "content": response})

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"**Vous :** {msg['content']}")
        else:
            st.markdown(f"**Assistant :** {msg['content']}")
