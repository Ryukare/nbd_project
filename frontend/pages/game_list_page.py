import streamlit as st
import pandas as pd

from frontend.components.dialogs import add_rating_dialog, change_rating_dialog
from services.game_service import get_all_games, delete_game
from services.rating_service import check_if_game_is_rated

def load_game_list_page():
    games = get_all_games(st.session_state.username)
    if len(games) == 0:
        st.info("There are no games in database")
        return

    col_title, col_rating, col_details, col_delete, col_edit, col_add = st.columns([3, 1, 1, 1, 1, 1])
    with col_title:
        st.title("All Games")
    with col_add:
        if st.button("Add Game"):
            st.session_state.page = "add_game"
            st.rerun()

    dataframe = pd.DataFrame(games)
    dataframe = dataframe[["title", "genre", "price", "rating", "your_rating"]]
    dataframe["price"] = "$" + dataframe["price"].astype(str)
    dataframe = dataframe.rename(columns={"your_rating": "your rating"})
    selection = st.dataframe(dataframe, on_select="rerun", selection_mode="single-row")
    rows = selection.get("selection", {}).get("rows", [])
    if rows:
        st.session_state.selected_game = games[rows[0]]

        with col_details:
            if st.button("Show Details"):
                st.session_state.page = "details"
                st.rerun()
        with col_rating:
            if st.button("Rate Game"):
                if check_if_game_is_rated(st.session_state.username, st.session_state.selected_game["title"]):
                    change_rating_dialog()
                else:
                    add_rating_dialog()
        with col_edit:
            if st.button("Edit Game"):
                st.session_state.page = "edit_game"
                st.rerun()
        with col_delete:
            if st.button("Delete Game"):
                delete_game(st.session_state.selected_game)
                st.rerun()
    else:
        st.session_state.selected_game = None