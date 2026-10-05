import mlflow.pyfunc

model = mlflow.pyfunc.load_model(
    "models:/HousePricePredictor/Production"
)

print(model)