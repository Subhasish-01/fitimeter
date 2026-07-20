import numpy as np
import tensorflow as tf
import json
from tensorflow.keras.models import load_model

from src.utils import read_yaml


config = read_yaml("config/config.yaml")


class FoodPredictor:

    def __init__(self):
        self.model = load_model(config["model_path"])
        with open("artifacts/class_mapping.json", "r") as f:
            self.class_to_index = json.load(f)

        self.index_to_class = {
            value: key
            for key, value in self.class_to_index.items()
        }

    def preprocess_image(self, image):

        # Resize
        image = image.resize((224, 224))

        # Convert to numpy
        image = np.array(image)

        # Convert to float32
        image = image.astype(np.float32)

        # Same preprocessing as training
        image = tf.keras.applications.efficientnet.preprocess_input(image)

        # Add batch dimension
        image = np.expand_dims(image, axis=0)

        return image

    def predict(self, image):

        image = self.preprocess_image(image)

        prediction = self.model.predict(image,verbose=0)

        class_index = np.argmax(prediction)

        confidence = round(float(np.max(prediction))*100,2)
        food_name  = self.index_to_class[class_index]
        return food_name, confidence