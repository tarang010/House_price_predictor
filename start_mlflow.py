import os

port = 5000

os.system(
    f"mlflow ui --host 0.0.0.0 --port {port}"
)