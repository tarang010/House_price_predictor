from fastapi import FastAPI
from src.serving.predict import predict

app = FastAPI()

@app.post("/predict")
def prediction(payload: dict):

    result = predict(payload)

    return {
        "prediction": float(result)
    }