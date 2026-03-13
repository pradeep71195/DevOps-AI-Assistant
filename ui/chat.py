import streamlit as st
import requests

st.title("DevOps AI Assistant")

question = st.text_input("Ask a DevOps question")

if question:
    r = requests.post(
        "http://localhost:8000/chat",
        params={"prompt": question}
    )

    st.write(r.json()["response"])