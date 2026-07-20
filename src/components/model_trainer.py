import os
import sys
import tensorflow as tf
from dataclasses import dataclass

from src.logger import logging
from src.exception import CustomException
from src.components.model_builder import ModelBuilder


@dataclass
class ModelTrainerConfig:

    epochs = 30

    model_path = os.path.join(
        "artifacts",
        "food_classifier.keras"
    )

    log_dir = "logs"


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
                save_weights_only=False,
                verbose=1
            )

            early_stopping = tf.keras.callbacks.EarlyStopping(
                monitor="val_loss",
                patience=5,
                restore_best_weights=True,
                verbose=1
            )

            reduce_lr = tf.keras.callbacks.ReduceLROnPlateau(
                monitor="val_loss",
                factor=0.2,
                patience=2,
                min_lr=1e-7,
                verbose=1
            )

            tensorboard = tf.keras.callbacks.TensorBoard(
                log_dir=self.config.log_dir,
                histogram_freq=1
            )

            history = self.model.fit(
                train_ds,
                validation_data=test_ds,
                epochs=self.config.epochs,
                callbacks=[
                    checkpoint,
                    early_stopping,
                    reduce_lr,
                    tensorboard
                ],
                shuffle=True,
                verbose=1
            )

            logging.info("Training Completed Successfully")

            return history

        except Exception as e:

            logging.error(e)

            raise CustomException(e, sys)