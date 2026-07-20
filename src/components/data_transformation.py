import sys
import tensorflow as tf
import os
from dataclasses import dataclass

from src.logger import logging
from src.exception import CustomException


@dataclass
class DataTransformationConfig:
    image_size = (224, 224)
    batch_size = 32
    validation_split = 0.2
    seed = 42


class DataTransformation:

    def __init__(self):
        self.config = DataTransformationConfig()
        self.data_augmentation = tf.keras.Sequential([
            tf.keras.layers.RandomFlip("horizontal"),
            tf.keras.layers.RandomRotation(0.1),
            tf.keras.layers.RandomZoom(0.2),
            tf.keras.layers.RandomContrast(0.1),
        ])
    def create_labels(self, file_list):
        """
        Extract class names from train.txt/test.txt
        Example:
        apple_pie/1005649 -> apple_pie
        """

        labels = []

        for file in file_list:
            label = file.split("/")[0]
            labels.append(label)

        return labels
    
    def create_class_mapping(self, train_labels):
        """
        Create mapping:
        apple_pie -> 0
        pizza -> 75
        waffles -> 100
        """

        class_names = sorted(set(train_labels))

        class_to_index = {
            class_name: index
            for index, class_name in enumerate(class_names)
        }

        return class_to_index

    
    def encode_labels(self, labels, class_to_index):
        """
        Convert class names to integer labels.
        """

        encoded_labels = []

        for label in labels:
            encoded_labels.append(class_to_index[label])

        return encoded_labels
    
    def load_image(self, image_path, label):
        """
        Reads an image from disk and preprocesses it.
        """

        image = tf.io.read_file(image_path)

        image = tf.image.decode_jpeg(image, channels=3)

        image = tf.image.resize(
            image,
            self.config.image_size
        )

        image = tf.cast(image, tf.float32)

        image = tf.keras.applications.efficientnet.preprocess_input(image)

        return image, label

    def create_image_paths(self, file_list, images_path):

        image_paths = []

        for file in file_list:
            image_path = os.path.join(images_path, file + ".jpg")
            image_paths.append(image_path)

        return image_paths

    def initiate_data_transformation(self, train_data, test_data, images_path):

        try:

            logging.info("Entered Data Transformation Component")
            train_image_paths = self.create_image_paths(train_data, images_path)
            test_image_paths = self.create_image_paths(test_data, images_path)

            logging.info("Image paths created successfully.")
            train_labels = self.create_labels(train_data)
            test_labels = self.create_labels(test_data)

            logging.info("Labels created successfully.")
            class_to_index = self.create_class_mapping(train_labels)
            
            train_labels = self.encode_labels(
                train_labels,
                class_to_index
            )

            test_labels = self.encode_labels(
                test_labels,
                class_to_index
            )

            logging.info("Labels encoded successfully.")
            train_ds = tf.data.Dataset.from_tensor_slices(
                (train_image_paths, train_labels)
            )

            test_ds = tf.data.Dataset.from_tensor_slices(
                (test_image_paths, test_labels)
            )

            logging.info("TensorFlow datasets created.")
            train_ds = train_ds.map(
                self.load_image,
                num_parallel_calls=tf.data.AUTOTUNE
            )

            train_ds = train_ds.map(
                lambda x, y: (
                    self.data_augmentation(x, training=True),
                    y
                ),
                num_parallel_calls=tf.data.AUTOTUNE
            )
            train_ds = train_ds.shuffle(
                buffer_size=10000,
                seed=self.config.seed,
                reshuffle_each_iteration=True
            )
            test_ds = test_ds.map(
                self.load_image,
                num_parallel_calls=tf.data.AUTOTUNE
            )

            logging.info("Images loaded successfully.")
            train_ds = train_ds.batch(self.config.batch_size)

            test_ds = test_ds.batch(self.config.batch_size)

            logging.info("Batching completed.")

            train_ds = train_ds.prefetch(
                tf.data.AUTOTUNE
            )

            test_ds = test_ds.prefetch(
                tf.data.AUTOTUNE
            )

            logging.info("Prefetch enabled.")

            logging.info("Training Dataset Created Successfully")
            logging.info("Validation Dataset Created Successfully")

            return train_ds, test_ds

        except Exception as e:

            logging.error(e)

            raise CustomException(e, sys)