from streamlit_option_menu import option_menu

from services.recommendation_service import get_highly_recommended_games, get_games_recommended_by_similar_users
import streamlit as st
import pandas as pd

def load_recommended_page():
    selected_profile_page = option_menu(
        menu_title=None,
        options=["Highly Recommended", "Similar Users Recommended"],
        icons=["file-person", "file-person-fill"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal"
    )

    if selected_profile_page == "Highly Recommended":
        highly_recommended_list()
    elif selected_profile_page == "Similar Users Recommended":
        similar_users_recommended_list()

def highly_recommended_list():
    games = get_highly_recommended_games(st.session_state.username)
    if len(games) == 0:
        st.info("There are no games recommended for you")
    else:
        dataframe = pd.DataFrame(games)
        dataframe = dataframe.rename(columns={"following_count": "following accounts rates"})
        st.dataframe(dataframe)

def similar_users_recommended_list():
    games = get_games_recommended_by_similar_users(st.session_state.username)
    if len(games) == 0:
        st.info("There are no games recommended for you")
    else:
        dataframe = pd.DataFrame(games)
        dataframe = dataframe.rename(columns={"similar_users": "Similar users"})
        st.dataframe(dataframe)