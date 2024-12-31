"""
Main file for the Streamlit app.
"""

import streamlit as st

from components.chat import display_chatbot_ui
from components.admin import display_admin_ui

# from utils import login_user


def main():
    # """Main function for the Streamlit app."""
    # # Initialize session state for authentication
    # if "authenticated" not in st.session_state:
    #     st.session_state.authenticated = False

    # # Login check
    # if not st.session_state.authenticated:
    #     st.header("Login")
    #     username = st.text_input("Username")
    #     password = st.text_input("Password", type="password")

    #     if st.button("Login"):
    #         if username and password:
    #             response = login_user(username, password)
    #             print(f"Response: {response}")
    #             if response["status"] == "success":
    #                 st.session_state.authenticated = True
    #                 st.success("Login successful!")
    #                 st.rerun()
    #             else:
    #                 st.error(response["message"])
    #         else:
    #             st.error("Please enter both username and password")
    #     return

    # # Show logout button in sidebar when authenticated
    # if st.sidebar.button("Logout"):
    #     st.session_state.authenticated = False
    #     st.rerun()

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Chat", "Admin"])

    if page == "Chat":
        display_chatbot_ui()
    else:
        display_admin_ui()


if __name__ == "__main__":
    main()
