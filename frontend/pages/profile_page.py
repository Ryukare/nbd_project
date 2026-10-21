import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

from frontend.components.dialogs import change_rating_dialog
from services.rating_service import get_rated_games
from services.follow_service import get_followed_accounts, get_followers_accounts
from frontend.components.user_grid import display_user_grid

def load_profile_page():
    rated_games = get_rated_games(st.session_state.username)
    following = get_followed_accounts(st.session_state.username)
    followers = get_followers_accounts(st.session_state.username)

    st.title("Profile")
    col_image, col_username = st.columns([2, 15])

    with col_image:
        st.image("https://cdn-icons-png.flaticon.com/512/847/847969.png",width=75)

    with col_username:
        st.markdown(
            f"""
            <div style="height:75px; display:flex; align-items:center;">
                <strong>{st.session_state.username}</strong>
            </div>
            """,
            unsafe_allow_html=True
        )

    col_games, col_following, col_followers, _ = st.columns([4, 4, 4, 6])

    with col_games:
        st.markdown(
            f"""
                    <div style="height:50px; display:flex; align-items:center;">
                        <strong>Rated Games: {len(rated_games)}</strong>
                    </div>
                    """,
            unsafe_allow_html=True
        )

    with col_following:
        st.markdown(
            f"""
                    <div style="height:50px; display:flex; align-items:center;">
                        <strong>Following: {len(following)}</strong>
                    </div>
                    """,
            unsafe_allow_html=True
        )

    with col_followers:
        st.markdown(
            f"""
                    <div style="height:50px; display:flex; align-items:center;">
                        <strong>Followers: {len(followers)}</strong>
                    </div>
                    """,
            unsafe_allow_html=True
        )

    selected_profile_page = option_menu(
        menu_title=None,
        options=["Games", "Following", "Followers"],
        icons=["controller", "file-person", "file-person-fill"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal"
    )

    if selected_profile_page == "Games":
        rated_games_list(rated_games)
    elif selected_profile_page == "Following":
        following_accounts_list(following)
    elif selected_profile_page == "Followers":
        followers_accounts_list(following, followers)

def rated_games_list(rated_games):
    col_title, col_details, col_rating = st.columns([5, 1, 1])
    with col_title:
        st.title("Rated Games")
    if len(rated_games) == 0:
        st.info("You have not rated any games")
    else:
        dataframe = pd.DataFrame(rated_games)
        dataframe = dataframe[["title", "genre", "price", "rating", "your_rating"]]
        dataframe["price"] = "$" + dataframe["price"].astype(str)
        dataframe = dataframe.rename(columns={"your_rating": "your rating"})
        selection = st.dataframe(dataframe, on_select="rerun", selection_mode="single-row")
        rows = selection.get("selection", {}).get("rows", [])

        if rows:
            st.session_state.selected_game = rated_games[rows[0]]
            with col_details:
                if st.button("Show Details"):
                    st.session_state.page = "details"
                    st.rerun()
            with col_rating:
                if st.button("Change Rating"):
                    change_rating_dialog()
        else:
            st.session_state.selected_game = None

def following_accounts_list(following):
    st.title("Accounts you follow")

    if len(following) == 0:
        st.info("You are not following any accounts")

    display_user_grid("followed", following)

def followers_accounts_list(following, followers):
    st.title("Accounts you are followed by")
    if len(followers) == 0:
        st.info("You are not followed by any accounts")

    display_user_grid("follower", followers, following)

