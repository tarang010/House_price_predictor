import mlflow.pyfunc
import pandas as pd

model = mlflow.pyfunc.load_model(
    "models:/HousePricePredictor/Production"
)

def predict(data):

    df = pd.DataFrame([data])

    return model.predict(df)[0]