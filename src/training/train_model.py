import mlflow
import mlflow.sklearn
import pandas as pd
import joblib as jb

from src.training.model_factory import get_model
from src.training.evaluate_model import evaluate
from src.utils.helpers import load_yaml

config = load_yaml("src/config/config.yaml")
model_cfg = load_yaml("src/config/model_config.yaml")

mlflow.set_tracking_uri(
    config["mlflow"]["tracking_uri"]
)

mlflow.set_experiment(
    config["mlflow"]["experiment_name"]
)

X_train = pd.read_csv("data/processed/X_train.csv")
X_test = pd.read_csv("data/processed/X_test.csv")

y_train = pd.read_csv(
    "data/processed/y_train.csv"
).squeeze()

y_test = pd.read_csv(
    "data/processed/y_test.csv"
).squeeze()

best_r2 = -999
best_model = None
best_name = None

for name, info in model_cfg["models"].items():

    if not info["enabled/"]:
        continue

    model = get_model(
        name,
        info["params"]
    )

    with mlflow.start_run(run_name=name):

        model.fit(X_train, y_train)

        rmse, r2 = evaluate(
            model,
            X_test,
            y_test
        )

        mlflow.log_metric(
            "RMSE",
            rmse
        )

        mlflow.log_metric(
            "R2",
            r2
        )

        mlflow.sklearn.log_model(
            model,
            name
        )

        if r2 > best_r2:
            best_r2 = r2
            best_model = model
            best_name = name

jb.dump(
    best_model,
    "models/trained/best_model.pkl"
)

print(f"Best Model: {best_name}")