import streamlit as st
from langchain_community.chat_models import ChatOllama

st.title('Streamlit & 🦜🔗  App')


def generate_response(input_text):
    llm = ChatOllama(base_url="http://localhost:11434", model="gemma:7b", temperature=0)
    response = llm.invoke(input_text)
    st.info(response.content)

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    
    if submitted:
        generate_response(text)