from mlflow.tracking import MlflowClient

client = MlflowClient()

for model in client.search_registered_models():

    print(model.name)

    for version in model.latest_versions:

        print(
            version.version,
            version.current_stage
        )