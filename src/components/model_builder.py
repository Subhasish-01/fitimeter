import sys
import tensorflow as tf
from dataclasses import dataclass

from src.logger import logging
from src.exception import CustomException


@dataclass
class ModelBuilderConfig:
    input_shape = (224, 224, 3)
    num_classes = 101
    learning_rate = 0.00001


class ModelBuilder:

    def __init__(self):
        self.config = ModelBuilderConfig()

    def build_model(self):

        try:

            logging.info("Building MobileNetV2 Model")
            data_augmentation = tf.keras.Sequential([
                tf.keras.layers.RandomFlip("horizontal"),
                tf.keras.layers.RandomRotation(0.2),
                tf.keras.layers.RandomZoom(0.2),
            ], name="data_augmentation")
            base_model = tf.keras.applications.MobileNetV2(
                weights="imagenet",
                include_top=False,
                input_shape=self.config.input_shape
            )
            base_model.trainable = False
            model = tf.keras.Sequential([
                tf.keras.layers.Input(shape=self.config.input_shape),

                data_augmentation,
                base_model,

                tf.keras.layers.GlobalAveragePooling2D(),

                tf.keras.layers.Dense(
                    256,
                    activation="relu"
                ),

                tf.keras.layers.Dropout(0.3),

                tf.keras.layers.Dense(
                    self.config.num_classes,
                    activation="softmax"
                )
            ])
            model.compile(
                optimizer=tf.keras.optimizers.Adam(
                    learning_rate=self.config.learning_rate
                ),
                loss=tf.keras.losses.SparseCategoricalCrossentropy(),
                metrics=["accuracy"]
            )

            logging.info("Model compiled successfully.")

            return model
        except Exception as e:

            logging.error(e)

            raise CustomException(e, sys)