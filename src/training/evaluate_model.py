from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import numpy as np

def evaluate(model, X_test, y_test):

    preds = model.predict(X_test)

    rmse = np.sqrt(
        mean_squared_error(y_test, preds)
    )

    r2 = r2_score(y_test, preds)

    return rmse, r2