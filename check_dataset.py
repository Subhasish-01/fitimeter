import tensorflow as tf

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation

ingestion = DataIngestion()

train_data, test_data, metadata = ingestion.initiate_data_ingestion()

dt = DataTransformation()

train_ds, test_ds = dt.initiate_data_transformation(
    train_data,
    test_data,
    ingestion.ingestion_config.images_path
)

print("Train batches:", tf.data.experimental.cardinality(train_ds).numpy())
print("Test batches:", tf.data.experimental.cardinality(test_ds).numpy())

images, labels = next(iter(train_ds))

print("Image Shape:", images.shape)
print("Label Shape:", labels.shape)

print("First 10 Labels:", labels.numpy()[:10])

print("Image Range:")
print("Min:", tf.reduce_min(images).numpy())
print("Max:", tf.reduce_max(images).numpy())