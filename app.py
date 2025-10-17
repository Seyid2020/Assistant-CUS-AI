import streamlit as st

st.set_page_config(page_title="Assistant CUS AI", layout="centered")

st.markdown("""
<h2 style='text-align:center; color:#006666;'>🤖 Assistant CUS AI</h2>
<p style='text-align:center;'>Bienvenue dans votre assistant intelligent pour le Centre des Systèmes Urbains (CUS) - UM6P.</p>
""", unsafe_allow_html=True)

st.markdown("""
<iframe 
    src="https://apps.abacus.ai/chatllm/?appId=15e8751540&hideTopBar=2"
    width="420"
    height="600"
    style="border: 2px solid #006666; border-radius: 12px;"
></iframe>
""", unsafe_allow_html=True)
