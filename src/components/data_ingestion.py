import os
import sys
from dataclasses import dataclass

from src.logger import logging
from src.exception import CustomException


@dataclass
class DataIngestionConfig:
    dataset_path: str = os.path.join("datasets", "food-101")
    images_path: str = os.path.join("datasets", "food-101", "images")
    meta_path: str = os.path.join("datasets", "food-101", "meta")

    train_file: str = os.path.join("datasets", "food-101", "meta", "train.txt")
    test_file: str = os.path.join("datasets", "food-101", "meta", "test.txt")


class DataIngestion:

    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def verify_dataset(self):

        try:

            logging.info("Dataset verification started.")

            if not os.path.exists(self.ingestion_config.dataset_path):
                raise FileNotFoundError(
                    f"{self.ingestion_config.dataset_path} not found."
                )

            if not os.path.exists(self.ingestion_config.images_path):
                raise FileNotFoundError(
                    f"{self.ingestion_config.images_path} not found."
                )

            if not os.path.exists(self.ingestion_config.meta_path):
                raise FileNotFoundError(
                    f"{self.ingestion_config.meta_path} not found."
                )

            logging.info("Dataset verified successfully.")

            return True

        except Exception as e:
            logging.error(e)
            raise CustomException(e, sys)

    def load_metadata(self):

        try:

            logging.info("Loading dataset metadata...")

            with open(self.ingestion_config.train_file, "r") as f:
                train_data = f.read().splitlines()

            with open(self.ingestion_config.test_file, "r") as f:
                test_data = f.read().splitlines()

            classes = sorted(os.listdir(self.ingestion_config.images_path))

            metadata = {
                "num_classes": len(classes),
                "train_images": len(train_data),
                "test_images": len(test_data),
                "classes": classes,
            }

            logging.info(f"Number of Classes : {metadata['num_classes']}")
            logging.info(f"Training Images   : {metadata['train_images']}")
            logging.info(f"Testing Images    : {metadata['test_images']}")

            return train_data,test_data,metadata

        except Exception as e:
            logging.error(e)
            raise CustomException(e, sys)

    def initiate_data_ingestion(self):

        try:

            logging.info("Entered Data Ingestion Component")

            self.verify_dataset()

            train_data, test_data, metadata = self.load_metadata()


            logging.info("Data Ingestion Completed Successfully")

            return (train_data,
                     test_data,
                     metadata
                     )

        except Exception as e:
            logging.error(e)
            raise CustomException(e, sys)


if __name__ == "__main__":

    obj = DataIngestion()

    train_data,test_data,metadata = obj.initiate_data_ingestion()

    print("=" * 60)
    print("Food-101 Dataset Information")
    print("=" * 60)

    print(f"Number of Classes : {metadata['num_classes']}")
    print(f"Training Images   : {metadata['train_images']}")
    print(f"Testing Images    : {metadata['test_images']}")

    print("\nFirst 10 Classes:")
    for cls in metadata["classes"][:10]:
        print(cls)