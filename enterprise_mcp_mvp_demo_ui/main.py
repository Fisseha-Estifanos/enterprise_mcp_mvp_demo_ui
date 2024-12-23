import streamlit as st

from utils import pass_question_to_router, get_all_users


def display_chatbot_ui():
    st.title("Enterprise MCP MVP demo")

    users = get_all_users()
    if len(users) == 0:
        st.error("No users found")
        return

    usernames = []
    for user in users:
        if isinstance(user, dict) and "username" in user:
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


def main():
    display_chatbot_ui()


if __name__ == "__main__":
    main()
