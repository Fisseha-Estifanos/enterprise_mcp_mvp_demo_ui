import streamlit as st

from utils import pass_question_to_router


def display_chatbot_ui():
    st.title("Enterprise MCP MVP demo")

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
            # TODO : get user name here
            answer = pass_question_to_router(
                username="user2",
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
