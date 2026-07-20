import sys
import tensorflow as tf
from dataclasses import dataclass

from src.logger import logging
from src.exception import CustomException


@dataclass
class ModelBuilderConfig:
    input_shape = (224, 224, 3)
    num_classes = 101
    learning_rate = 1e-5


class ModelBuilder:

    def __init__(self):
        self.config = ModelBuilderConfig()

    def build_model(self):

        try:

            logging.info("Building EfficientNetB0 Model")

            base_model = tf.keras.applications.EfficientNetB0(
                weights="imagenet",
                include_top=False,
                input_shape=self.config.input_shape
            )

            # Fine-tuning
            base_model.trainable = True

            # Freeze all except last 20 layers
            for layer in base_model.layers[:-20]:
                layer.trainable = False

            # Freeze BatchNorm layers
            for layer in base_model.layers:
                if isinstance(layer, tf.keras.layers.BatchNormalization):
                    layer.trainable = False

            inputs = tf.keras.Input(shape=self.config.input_shape)

            # Images are already augmented and preprocessed
            # in data_transformation.py
            x = inputs

            x = base_model(x, training=False)

            x = tf.keras.layers.GlobalAveragePooling2D()(x)

            x = tf.keras.layers.Dense(
                512,
                activation="relu",
                kernel_regularizer=tf.keras.regularizers.l2(1e-4)
            )(x)

            x = tf.keras.layers.BatchNormalization()(x)

            x = tf.keras.layers.Dropout(0.5)(x)

            outputs = tf.keras.layers.Dense(
                self.config.num_classes,
                activation="softmax",
                dtype=tf.float32
            )(x)

            model = tf.keras.Model(inputs, outputs)

            model.compile(
                optimizer=tf.keras.optimizers.AdamW(
                    learning_rate=self.config.learning_rate,
                    weight_decay=1e-5
                ),
                loss=tf.keras.losses.SparseCategoricalCrossentropy(),
                metrics=["accuracy"]
            )

            logging.info("EfficientNetB0 Model compiled successfully.")

            return model

        except Exception as e:

            logging.error(e)

            raise CustomException(e, sys)