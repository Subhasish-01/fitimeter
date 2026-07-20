import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

from src.components.navbar import navbar
from src.nutrition import NutritionDatabase
from src.calculator import NutritionCalculator

db = NutritionDatabase()


def nutrition_dashboard():

    navbar("Prediction")

    if "food_name" not in st.session_state or "grams" not in st.session_state:
        st.warning("Please predict a food first.")
        return

    food_name = st.session_state["food_name"]
    grams = st.session_state["grams"]

    food = db.get_food(food_name)

    if food is None:
        st.error("Nutrition data not found.")
        return

    nutrients = NutritionCalculator.calculate(food, grams)
    nutrients = {k: round(v, 2) for k, v in nutrients.items()}

    st.markdown(
        """
        <h1 style="text-align:center;">
            Nutrition Dashboard
        </h1>
        """,
        unsafe_allow_html=True,
    )

    st.write("")


    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.metric("Food", food_name.title())

    with col2:
        with st.container(border=True):
            st.metric("Serving Size", f"{grams} g")

    st.write("")
    st.write("")

    left, right = st.columns(2)

    with left:

        with st.container(border=True):

            fig, ax = plt.subplots(figsize=(5, 4))

            fig.patch.set_facecolor("#0E1117")
            ax.set_facecolor("#0E1117")

            labels = ["Protein", "Carbs", "Fat"]

            values = [
                nutrients["Protein"],
                nutrients["Carbs"],
                nutrients["Fat"],
            ]

            ax.pie(
                values,
                labels=labels,
                autopct="%1.1f%%",
                startangle=90,
                textprops={"color": "white"},
            )

            ax.set_title(
                "Macronutrient Distribution",
                color="white",
            )

            st.pyplot(fig, use_container_width=True)

    with right:

        with st.container(border=True):

            fig, ax = plt.subplots(figsize=(5, 4))

            fig.patch.set_facecolor("#0E1117")
            ax.set_facecolor("#0E1117")

            names = list(nutrients.keys())
            values = list(nutrients.values())

            ax.bar(names, values)

            ax.set_title(
                "Nutrition Values",
                color="white",
            )

            ax.set_ylabel(
                "Value",
                color="white",
            )

            ax.tick_params(colors="white")

            plt.xticks(rotation=30)

            st.pyplot(fig, use_container_width=True)

    st.write("")
    st.write("")

    with st.container(border=True):

        st.subheader("Nutrition Details")

        table = pd.DataFrame(
            {
                "Nutrient": [
                    "Calories",
                    "Protein",
                    "Fat",
                    "Carbs",
                    "Fiber",
                    "Sugar",
                    "Sodium",
                ],
                "Value": [
                    f"{nutrients['Calories']:.2f} kcal",
                    f"{nutrients['Protein']:.2f} g",
                    f"{nutrients['Fat']:.2f} g",
                    f"{nutrients['Carbs']:.2f} g",
                    f"{nutrients['Fiber']:.2f} g",
                    f"{nutrients['Sugar']:.2f} g",
                    f"{nutrients['Sodium']:.2f} mg",
                ],
            }
        )

        st.dataframe(
            table.set_index("Nutrient"),
            use_container_width=True,
        )

    st.write("")


    if st.button(
        "← Back to Prediction",
        use_container_width=True,
    ):
        st.session_state.page = "Prediction"
        st.query_params["page"] = "Prediction"
        st.rerun()