import streamlit as st
from services.follow_service import create_follow, delete_follow

def display_user_grid(user_type, users, logged_account_follows = None):

    num_cols = 2
    for i in range(0, len(users), num_cols):
        row_accounts = users[i:i + num_cols]
        cols = st.columns(num_cols)

        for col, account in zip(cols, row_accounts):

            with col:
                col_image, col_user, col_follow_button = st.columns([0.8, 2, 1.1])
                with col_image:
                    st.image(
                        "https://cdn-icons-png.flaticon.com/512/847/847969.png",
                        width=50
                    )
                with col_user:
                    st.markdown(
                        f"""
                                <div style="height:50px; display:flex; align-items:center;">
                                    <strong>{account["username"]}</strong>
                                </div>
                                """,
                        unsafe_allow_html=True
                    )
                with col_follow_button:

                    if logged_account_follows is not None:
                        followed_usernames = {
                            u["username"] for u in logged_account_follows
                        }
                        is_logged_account_follow = account["username"] in followed_usernames

                    if user_type == "followed":
                        label = "Unfollow"
                    elif user_type == "not_followed":
                        label = "Follow"
                    else:
                        label = "Unfollow" if is_logged_account_follow else "Follow"

                    follow_button = st.button(label, key=f"follow_{account}")
                    if follow_button:
                        if st.session_state.username is None:
                            st.session_state.page = "login"
                            st.rerun()
                        if user_type == "followed":
                            delete_follow(st.session_state.username, account["username"])
                        elif user_type == "not_followed":
                            create_follow(st.session_state.username, account["username"])
                        else:
                            if is_logged_account_follow:
                                delete_follow(st.session_state.username, account["username"])
                            else:
                                create_follow(st.session_state.username, account["username"])
                        st.rerun()