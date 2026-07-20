import streamlit as st


def navbar(active_page):

    col1, col2, col3, col4 = st.columns([6, 1.2, 1.5, 1])

    with col1:
        st.markdown(
            """
            <h2 style="
                margin:0;
                font-weight:700;
                letter-spacing:0.5px;
            ">
                Fitometer
            </h2>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        if st.button(
            "Home",
            use_container_width=True,
            disabled=(active_page == "Home"),
            key="nav_home",
        ):
            st.session_state.page = "Home"
            st.query_params["page"] = "Home"
            st.rerun()

    with col3:
        if st.button(
            "Prediction",
            use_container_width=True,
            disabled=(active_page == "Prediction"),
            key="nav_prediction",
        ):
            st.session_state.page = "Prediction"
            st.query_params["page"] = "Prediction"
            st.rerun()

    with col4:
        if st.button(
            "About",
            use_container_width=True,
            disabled=(active_page == "About"),
            key="nav_about",
        ):
            st.session_state.page = "About"
            st.query_params["page"] = "About"
            st.rerun()

    st.divider()