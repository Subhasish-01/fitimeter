import streamlit as st
from PIL import Image
from src.components.navbar import navbar

def prediction_page():

    navbar("Prediction")
    predictor = st.session_state["predictor"]
    st.markdown(
        """
        <h1 style="
            text-align:center;
            font-size:46px;
            font-weight:700;
            margin-bottom:10px;">
            Food Prediction
        </h1>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="
            text-align:center;
            color:#B5B5B5;
            font-size:18px;
            margin-bottom:25px;">
            Upload a food image to identify the dish using our AI model.
        </div>
        """,
        unsafe_allow_html=True,
    )


    uploaded_file = st.file_uploader(
        "Choose a Food Image",
        type=["jpg", "jpeg", "png"],
    )

    if uploaded_file is None:
        return

    image = Image.open(uploaded_file)

    if st.session_state.get("last_file") != uploaded_file.name:

        st.session_state["last_file"] = uploaded_file.name
        st.session_state["prediction_done"] = False


    left, center, right = st.columns([1, 2, 1])

    with center:

        with st.container(border=True):

            st.image(
                image,
                caption="Uploaded Image",
                use_container_width=True,
            )

    st.write("")

    if st.button(
        "Predict Food",
        use_container_width=True,
    ):

        with st.spinner("Predicting..."):

            food_name, confidence = predictor.predict(image)

            st.session_state["food_name"] = food_name
            st.session_state["confidence"] = confidence
            st.session_state["prediction_done"] = True

    if not st.session_state.get("prediction_done", False):
        return

    food_name = st.session_state["food_name"]
    confidence = st.session_state["confidence"]

    st.success("Prediction completed successfully.")

    st.markdown("## Prediction Result")

    st.write(
        f"""
The uploaded image has been identified as **{food_name.title()}**
with **{confidence:.2f}%** confidence.
"""
    )

    st.progress(confidence / 100)

    st.caption(f"Model Confidence : {confidence:.2f}%")

    st.write("")

    with st.container(border=True):

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Prediction",
                food_name.title(),
            )

        with col2:

            st.metric(
                "Confidence",
                f"{confidence:.2f}%",
            )

    st.write("")

    with st.container(border=True):

        grams = st.number_input(
            "Serving Size (grams)",
            min_value=1,
            value=100,
            step=10,
        )

    st.write("")

    if st.button(
        "Analyze Nutrition",
        use_container_width=True,
    ):

        st.session_state["grams"] = grams
        st.session_state.page = "Nutrition"
        st.query_params["page"] = "Nutrition"
        st.rerun()