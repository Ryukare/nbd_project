import streamlit as st
from streamlit_option_menu import option_menu

from frontend.pages.follow_page import follow_list
from frontend.pages.game_list_page import load_game_list_page
from frontend.pages.game_details_page import load_game_details_page
from frontend.pages.game_form_page import load_game_form
from frontend.pages.login_page import load_login_form, load_register_form, load_profile_change_form
from frontend.pages.profile_page import load_profile_page
from frontend.pages.recommended_page import load_recommended_page

if "page" not in st.session_state:
    st.session_state.page = "list"
if "navbar_selection" not in st.session_state:
    st.session_state.navbar_selection = "list"
if "selected_game" not in st.session_state:
    st.session_state.selected_game = None
if "username" not in st.session_state:
    st.session_state.username = None
if "user" not in st.session_state:
    st.session_state.user = None

st.set_page_config(page_title="My Game List")

if st.session_state.page == "login":
    load_login_form()
elif st.session_state.page == "register":
    load_register_form()
elif st.session_state.page == "change_user_data":
    load_profile_change_form()
else:
    with st.sidebar:
        st.title("My Game List")

        selected_label = option_menu(
            menu_title=None,
            options=["Game List", "Recommended", "Follow", "Profile"],
            icons=["card-list", "list", "person-add", "person"],
            menu_icon="cast",
            default_index=0,
            orientation="vertical"
        )

        if selected_label == "Game List":
            st.session_state.navbar_selection = "list"
        elif selected_label == "Recommended":
            st.session_state.navbar_selection = "recommended"
        elif selected_label == "Follow":
            st.session_state.navbar_selection = "follow"
        elif selected_label == "Profile":
            st.session_state.navbar_selection = "profile"

        st.divider()

        st.title("**Account**")
        if st.session_state.username:
            st.markdown(f"Logged as **{st.session_state.username}**")
            col1, col2, _ = st.columns([3, 2, 0.7])
            with col1:
                if st.button("Change Data", key="btn_change"):
                    st.session_state.page = "change_user_data"
                    st.rerun()
            with col2:
                if st.button("Logout", key="btn_logout"):
                    st.session_state.username = None
                    st.rerun()

        else:
            col1, col2, _ = st.columns([2.2, 2, 1])
            with col1:
                if st.button("Register", key="btn_register"):
                    st.session_state.page = "register"
                    st.rerun()
            with col2:
                if st.button("Login", key="btn_login"):
                    st.session_state.page = "login"
                    st.rerun()

    if st.session_state.navbar_selection == "list":
        if st.session_state.page == "details":
            load_game_details_page()
        elif st.session_state.page == "edit_game" or st.session_state.page == "add_game":
            load_game_form()
        else:
            st.session_state.page = "list"
            load_game_list_page()
    elif st.session_state.navbar_selection == "recommended":
        if st.session_state.username is None:
            st.session_state.page = "login"
            st.rerun()
        else:
            st.session_state.page = "recommended"
            load_recommended_page()
    elif st.session_state.navbar_selection == "follow":
        st.session_state.page = "follow"
        follow_list()
    elif st.session_state.navbar_selection == "profile":
        if st.session_state.username is None:
            st.session_state.page = "login"
            st.rerun()
        if st.session_state.page == "details":
            load_game_details_page()
        else:
            st.session_state.page = "profile"
            load_profile_page()