from mlflow.tracking import MlflowClient

client = MlflowClient()

client.transition_model_version_stage(
    name="HousePricePredictor",
    version=1,
    stage="Production"
)

print("Moved to Production")