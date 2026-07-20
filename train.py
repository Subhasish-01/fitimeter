from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

from src.logger import logging
from src.exception import CustomException

import sys


def main():

    try:

        logging.info("=" * 50)
        logging.info("Training Pipeline Started")
        logging.info("=" * 50)

        ingestion = DataIngestion()

        train_data, test_data, metadata = ingestion.initiate_data_ingestion()

        logging.info("Data Ingestion Completed")

        transformation = DataTransformation()

        train_ds, test_ds = transformation.initiate_data_transformation(
            train_data,
            test_data,
           ingestion.ingestion_config.images_path
        )

        logging.info("Data Transformation Completed")

        trainer = ModelTrainer()

        history = trainer.initiate_model_trainer(
            train_ds,
            test_ds
        )

        logging.info("Model Training Completed")

        print("\nTraining Completed Successfully!")

    except Exception as e:

        raise CustomException(e, sys)


if __name__ == "__main__":

    main()