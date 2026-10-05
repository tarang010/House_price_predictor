import os
import sys

os.system(
    f'"{sys.executable}" -m mlflow ui --host 0.0.0.0 --port 5000'
)