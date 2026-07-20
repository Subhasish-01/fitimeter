from PIL import Image

from src.components.prediction import Prediction


predictor = Prediction()

image = Image.open("datasets/food-101/images/pizza/1008104.jpg")

food, confidence = predictor.predict(image)

print(f"Prediction : {food}")
print(f"Confidence : {confidence}%")