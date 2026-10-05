import mlflow
model_uri = ("runs:/RUN_ID/RandomForest")

mlflow.register_model(
    model_uri,
    "HousePricePredictor"
)