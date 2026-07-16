from src.components.model_builder import ModelBuilder

builder = ModelBuilder()

model = builder.build_model()

model.summary()