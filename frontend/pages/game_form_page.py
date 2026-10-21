import streamlit as st
from datetime import date

from services.game_service import create_game, update_game

def load_game_form():
    mode = st.session_state.page

    if mode == "edit_game":
        st.title("Edit Game")
        game = st.session_state.selected_game
    else:
        st.title("Add New Game")
        game = {}

    with st.form("game_form"):

        title = st.text_input("Title", value=game.get("title", ""))
        genre = st.text_input("Genre", value=game.get("genre", ""))
        developer = st.text_input("Developer", value=game.get("developer", ""))
        publisher = st.text_input("Publisher", value=game.get("publisher", ""))

        release_date_val = game.get("releaseDate")
        if release_date_val is None:
            release_date_input = date.today()
        else:
            release_date_input = date(
                release_date_val.year,
                release_date_val.month,
                release_date_val.day
            )
        release_date = st.date_input(
            "Release Date",
            value=release_date_input
        )

        price = st.number_input(
            "Price",
            min_value=0.0,
            value=float(game.get("price", 0))
        )

        platforms = st.multiselect(
            "Platforms",
            ["Steam", "Epic Games Store", "GOG", "PlayStation", "Xbox", "Nintendo Switch"],
            default=game.get("platforms", [])
        )

        description = st.text_area(
            "Description",
            value=game.get("description", "")
        )

        col1, col2, _ = st.columns([0.7, 1, 3.2])

        with col1:
            if st.form_submit_button("Go Back"):
                st.session_state.page = "list"
                st.rerun()

        with col2:
            submitted = st.form_submit_button("Save Changes" if mode == "edit_game" else "Add Game")

        if submitted:
            if not title or not genre or not platforms or not description or not publisher or not developer:
                st.error("You have left empty spaces")
                return

            game_data = {
                "title": title,
                "genre": genre,
                "developer": developer,
                "publisher": publisher,
                "releaseDate": release_date.isoformat(),
                "price": price,
                "platforms": platforms,
                "description": description,
            }

            try:
                if mode == "edit_game":
                    update_game(game["title"], game_data)
                else:
                    create_game(game_data)
                st.session_state.page = "list"
                st.rerun()
            except ValueError as e:
                st.error(str(e))