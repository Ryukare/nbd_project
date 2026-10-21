import streamlit as st
from services.rating_service import create_rating, delete_rating, update_rating

def show_rating():
    st.write(st.session_state.selected_game["title"])

    rates = {
        "(10) Masterpiece": 10,
        "(9) Excellent": 9,
        "(8) Great": 8,
        "(7) Good": 7,
        "(6) Decent": 6,
        "(5) Average": 5,
        "(4) Below Average": 4,
        "(3) Bad": 3,
        "(2) Terrible": 2,
        "(1) Abysmal": 1,
    }
    selection = st.selectbox("Pick Your Rate", list(rates.keys()))
    return rates, selection

@st.dialog("GAME RATING")
def add_rating_dialog():
    rates, selection = show_rating()

    _, col1, col2 = st.columns([3, 1, 1])
    with col1:
        if st.button("Cancel"):
            st.rerun()
    with col2:
        if st.session_state.username is None:
            if st.button("Login"):
                st.session_state.page = "login"
                st.rerun()
        else:
            if st.button("Submit"):
                create_rating(st.session_state.username, st.session_state.selected_game["title"], rates[selection])
                st.rerun()

@st.dialog("GAME RATING")
def change_rating_dialog():
    rates, selection = show_rating()

    _, col1, col2, col3 = st.columns([0.75, 0.75, 1.1, 1.1])
    with col1:
        if st.button("Cancel"):
            st.rerun()
    with col2:
        if st.button("Delete Rating"):
            delete_rating(st.session_state.username, st.session_state.selected_game["title"])
            st.rerun()
    with col3:
        if st.button("Change Rating"):
            update_rating(st.session_state.username, st.session_state.selected_game["title"], rates[selection])
            st.rerun()