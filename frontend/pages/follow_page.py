import streamlit as st
from frontend.components.user_grid import display_user_grid
from services.user_service import get_all_users
from services.follow_service import get_not_followed_accounts

def follow_list():
    st.title("Accounts to follow")
    if st.session_state.username is None:
        accounts = get_all_users()
        display_user_grid("not_followed", accounts)
    else:
        accounts = get_not_followed_accounts(st.session_state.username)
        if len(accounts) == 0:
            st.info("There are no accounts to follow")

        display_user_grid("not_followed", accounts)