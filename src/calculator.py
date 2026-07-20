class NutritionCalculator:

    @staticmethod
    def calculate(food, grams):

        factor = grams / 100

        nutrients = {
            "Calories": round(food["calories_per_100g"] * factor, 2),
            "Protein": round(food["protein_g_per_100g"] * factor, 2),
            "Fat": round(food["fat_g_per_100g"] * factor, 2),
            "Carbs": round(food["carbs_g_per_100g"] * factor, 2),
            "Fiber": round(food["fiber_g_per_100g"] * factor, 2),
            "Sugar": round(food["sugar_g_per_100g"] * factor, 2),
            "Sodium": round(food["sodium_mg_per_100g"] * factor, 2),
        }

        return nutrients