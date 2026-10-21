import streamlit as st
from services.user_service import validate_user, create_user, update_user, delete_user
import re

def load_login_form():
    st.title("Login")
    with st.form("login_from"):
        login = st.text_input("Username or Email")
        password = st.text_input("Password", type="password")

        col1, col2, _ = st.columns([1, 1, 5])

        with col1:
            back_button = st.form_submit_button("Go Back")
        with col2:
            submit_button = st.form_submit_button("Log In")

        if submit_button:
            correct_user = validate_user(login, password)
            if correct_user:
                st.session_state.user = correct_user
                st.session_state.username = correct_user["username"]
                st.session_state.page = st.session_state.navbar_selection
                st.rerun()
            else:
                st.error("Incorrect login or password")

        if back_button:
            st.session_state.page = st.session_state.navbar_selection
            st.rerun()

    col1, col2, _ = st.columns([2.7, 1, 3])

    with col1:
        st.markdown(
            """
                    <div style="height:40px; display:flex; align-items:center;">
                    <strong>If you don't have account register here: </strong>
                    </div>
                    """,
            unsafe_allow_html=True
        )
    with col2:
        if st.button("Register"):
            st.session_state.page = "register"
            st.rerun()

def load_register_form():
    st.title("Register")
    with st.form("register_form"):
        email = st.text_input("Email")
        login = st.text_input("Username")
        password = st.text_input("Password", type="password")

        col1, col2, _ = st.columns([1, 1, 5])

        with col1:
            back_button = st.form_submit_button("Go Back")
        with col2:
            submit_button = st.form_submit_button("Register")

        if submit_button:
            errors = []
            if not email:
                errors.append("Email is required")
            elif not re.match(r"^[\w.-]+@[\w.-]+\.\w+$", email):
                errors.append("Invalid email format")

            if not login:
                errors.append("Username is required")

            if not password:
                errors.append("Password is required")

            if errors:
                for err in errors:
                    st.error(err)
            else:
                try:
                    new_user = create_user(email, login, password)
                    st.session_state.user = new_user
                    st.session_state.username = new_user["username"]
                    st.session_state.page = st.session_state.navbar_selection
                    st.rerun()
                except ValueError as e:
                    msg = str(e)
                    if "email" in msg:
                        st.error("Account with this email already exists")
                    elif "username" in msg:
                        st.error("Account with this Username already exists")

        if back_button:
            st.session_state.page = st.session_state.navbar_selection
            st.rerun()

def load_profile_change_form():
    st.title("Change Account Data")
    user = st.session_state.user
    with st.form("change_data_form"):
        email = st.text_input("Email",  value=user.get("email", ""))
        login = st.text_input("Username", value=user.get("username", ""))
        password = st.text_input("Password", type="password", value=user.get("password", ""))

        col1, col2, col3, _ = st.columns([0.65, 0.95, 1.5, 1.5])

        with col1:
            back_button = st.form_submit_button("Go Back")
        with col2:
            delete_button = st.form_submit_button("Delete Account")
        with col3:
            submit_button = st.form_submit_button("Submit Changes")

        if submit_button:
            errors = []
            if not email:
                errors.append("Email is required")
            elif not re.match(r"^[\w.-]+@[\w.-]+\.\w+$", email):
                errors.append("Invalid email format")

            if not login:
                errors.append("Username is required")

            if not password:
                errors.append("Password is required")

            if errors:
                for err in errors:
                    st.error(err)
            else:
                try:
                    edited_user = update_user(user["username"], email, login, password)
                    st.session_state.user = edited_user
                    st.session_state.username = edited_user["username"]
                    st.session_state.page = st.session_state.navbar_selection
                    st.rerun()
                except ValueError as e:
                    msg = str(e)
                    if "email" in msg:
                        st.error("Account with this email already exists")
                    elif "username" in msg:
                        st.error("Account with this Username already exists")

        if delete_button:
            delete_user(user["username"])
            st.session_state.user = None
            st.session_state.username = None
            st.session_state.page = st.session_state.navbar_selection
            st.rerun()

        if back_button:
            st.session_state.page = st.session_state.navbar_selection
            st.rerun()