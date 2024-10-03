import streamlit as st
from langchain_openai.chat_models import ChatOpenAI

st.title("🦜🔗 Quickstart App")

def generate_response(input_text):
    model = ChatOpenAI(model='gpt-4o-mini-2024-07-18', max_tokens=1024, api_key='sk-WjFjU5gAjCTONWmXtUsUksWsO6GHbJvo', base_url = 'https://api.proxyapi.ru/openai/v1')
    st.info(model.invoke(input_text).content)


with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What are the three key pieces of advice for learning how to code?",
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text)
