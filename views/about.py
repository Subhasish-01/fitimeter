import streamlit as st
from src.components.navbar import navbar


def about():

    navbar("About")

    st.markdown(
        """
        <h1 style="text-align:center;">
            About Fitometer
        </h1>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="text-align:center; color:#B5B5B5; font-size:18px;">
        AI-powered food recognition and nutrition analysis platform.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    st.write("")


    with st.container(border=True):

        st.subheader("📌 Project Overview")

        st.write(
            """
            Fitometer is an AI-powered web application that identifies food from an image
            and provides detailed nutritional information based on the selected serving size.

            The application uses a deep learning model trained on the Food-101 dataset and
            combines it with a nutrition database to estimate calories, protein, carbohydrates,
            fat, fiber, sugar, and sodium.
            """
        )

    st.write("")

    # ---------------- Features ---------------- #

    with st.container(border=True):

        st.subheader("🚀 Features")

        st.markdown(
            """
            - AI-based Food Recognition
            - Image Upload Support
            - Nutrition Analysis
            - Serving Size Calculator
            - Interactive Charts
            - Nutrition Summary Table
            - Modern Streamlit Interface
            """
        )


  