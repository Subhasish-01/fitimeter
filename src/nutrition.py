import pandas as pd

from src.utils import read_yaml

config = read_yaml("config/config.yaml")


class NutritionDatabase:

    def __init__(self):
        self.df = pd.read_csv(config["nutrition_csv"])

    def get_food(self, food_name):

        food = self.df[
            self.df["food_name"].str.lower() == food_name.lower()
        ]

        if food.empty:
            return None

        return food.iloc[0]