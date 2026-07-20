import streamlit as st
from src.prediction import FoodPredictor


@st.cache_resource
def load_predictor():
    return FoodPredictor()
    
    
st.set_page_config(
    page_title="Fitometer",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}

.block-container{
    padding-top:1rem;
    padding-left:4rem;
    padding-right:4rem;
    padding-bottom:2rem;
}

</style>
""", unsafe_allow_html=True)


if "predictor" not in st.session_state:
    with st.spinner("Please wait...."):
        st.session_state["predictor"] = load_predictor()

query_page = st.query_params.get("page", "Home")
if "page" not in st.session_state:
    st.session_state.page = query_page

page = st.session_state.page


if page == "Home":

    from views.home import home
    home()

elif page == "Prediction":

    from views.prediction_page import prediction_page
    prediction_page()

elif page == "Nutrition":

    from views.nutrition_dashboard import nutrition_dashboard
    nutrition_dashboard()

elif page == "About":

    from views.about import about
    about()

