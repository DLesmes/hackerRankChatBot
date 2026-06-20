import streamlit as st
from openai import OpenAI

from src.agent import get_agent

st.set_page_config(
    page_title="Chat Playground", layout="wide", initial_sidebar_state="collapsed"
)
st.title("HackerReport Engine")


if "messages" not in st.session_state:
    st.session_state.messages = []

if "agent" not in st.session_state:
    st.session_state.agent = get_agent()


def get_agent_response(message: str) -> str:
    try:
        result = st.session_state.agent.query(message)
        return result.response
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None


if not st.session_state.messages:
    st.write("Type in your query to test your engine.")
else:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("Write your query ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = get_agent_response(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()
