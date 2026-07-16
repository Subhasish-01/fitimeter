import os
import sys
import tensorflow as tf
from dataclasses import dataclass

from src.logger import logging
from src.exception import CustomException

from src.components.model_builder import ModelBuilder


@dataclass
class ModelTrainerConfig:

    epochs = 10

    model_path = os.path.join(
        "artifacts",
        "food_classifier.keras"
    )


class ModelTrainer:

    def __init__(self):

        self.config = ModelTrainerConfig()

        self.model = ModelBuilder().build_model()

    def initiate_model_trainer(
            self,
            train_ds,
            test_ds
    ):

        try:

            logging.info("Training Started")

            os.makedirs(
                os.path.dirname(self.config.model_path),
                exist_ok=True
            )

            checkpoint = tf.keras.callbacks.ModelCheckpoint(
                filepath=self.config.model_path,
                monitor="val_accuracy",
                save_best_only=True,
                verbose=1
            )

            early_stopping = tf.keras.callbacks.EarlyStopping(
                monitor="val_loss",
                patience=3,
                restore_best_weights=True,
                verbose=1
            )
            
            history = self.model.fit(
                train_ds,
                validation_data=test_ds,
                epochs=self.config.epochs,
                callbacks=[
                    checkpoint,
                    early_stopping
                ]
            )

            logging.info("Training Completed Successfully")

            return history
        except Exception as e:

            logging.error(e)

            raise CustomException(e, sys)