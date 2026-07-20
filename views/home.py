import streamlit as st
from src.components.navbar import navbar


def home():

    navbar("Home")

    st.markdown(
        """
        <h1 style="
            text-align:center;
            font-size:56px;
            font-weight:700;
            margin-bottom:12px;">
            Know What's On Your Plate Instantly
        </h1>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="
            max-width:760px;
            margin:auto;
            text-align:center;
            color:#B5B5B5;
            font-size:20px;
            line-height:1.8;">
            Upload any food image and receive instant AI-powered food recognition
            with detailed nutritional insights to support healthier food choices.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    st.write("")

    left, center, right = st.columns([2.8, 2, 2.8])

    with center:
        if st.button(
            "Start Prediction",
            use_container_width=True,
        ):
            st.session_state.page = "Prediction"
            st.rerun()

    st.write("")
    st.write("")
    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):

            st.markdown("### AI Food Recognition")

            st.write(
                """
                Identify food items accurately from a single uploaded image
                using a deep learning model trained on Food-101.
                """
            )

    with col2:
        with st.container(border=True):

            st.markdown("### Nutrition Analysis")

            st.write(
                """
                View calories, protein, carbohydrates, fats,
                fiber, sugar and sodium according to the
                selected serving size.
                """
            )

    with col3:
        with st.container(border=True):

            st.markdown("### Instant Results")

            st.write(
                """
                Get predictions and complete nutritional
                information within seconds through an
                interactive dashboard.
                """
            )