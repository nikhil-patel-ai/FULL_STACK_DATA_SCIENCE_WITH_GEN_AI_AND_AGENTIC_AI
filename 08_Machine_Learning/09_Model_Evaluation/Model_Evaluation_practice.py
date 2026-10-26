"""
Model Evaluation

Goal: Calculate and interpret common regression metrics.

Run from this folder with:
    python "Model_Evaluation_practice.py"

This is a learning example. Review the code and dependencies before using it in production.
"""

import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

actual = np.array([3.0, 5.0, 2.5, 7.0, 4.0])
predicted = np.array([2.8, 5.2, 2.0, 6.5, 4.5])

mae = mean_absolute_error(actual, predicted)
mse = mean_squared_error(actual, predicted)
rmse = np.sqrt(mse)
r2 = r2_score(actual, predicted)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R²:", r2)
print("Reminder: compare models on data not used for training.")
