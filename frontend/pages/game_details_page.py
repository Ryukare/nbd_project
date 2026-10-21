import streamlit as st

def load_game_details_page():
    game = st.session_state.selected_game
    st.title(f"{game['title']}")
    st.markdown(f"**Genre:** {game['genre']}")
    st.markdown(f"**Developer:** {game.get('developer', '-')}")
    st.markdown(f"**Publisher:** {game.get('publisher', '-')}")
    st.markdown(f"**Release Date:** {game.get('releaseDate', '-')}")
    st.markdown(f"**Price:** {game['price']}$")
    st.markdown(f"**Platforms:** {', '.join(game['platforms'])}")
    st.markdown("**Description:**")
    st.info(game.get("description", "No Description"))
    st.markdown(f"**Rating:** {game.get('rating', '-')}")

    if st.button("Go Back"):
        st.session_state.page = "list"
        st.session_state.selected_game = None
        st.rerun()