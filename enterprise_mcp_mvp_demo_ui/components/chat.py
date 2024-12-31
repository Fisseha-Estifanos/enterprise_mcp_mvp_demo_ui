"""
Chat page for the Streamlit app.
"""

import streamlit as st

from utils import get_users, pass_question_to_router


def display_chatbot_ui():
    """Display the chatbot UI."""
    st.title("Enterprise MCP MVP demo")

    users = get_users()
    if len(users) == 0:
        st.error("No users found")
        return

    usernames = []
    for user in users["data"]:
        usernames.append(user["username"])
    selected_user = st.sidebar.selectbox("Select a user", usernames)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            answer = pass_question_to_router(
                username=selected_user,
                question=prompt,
            )
            st.write(answer)
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer,
                }
            )
