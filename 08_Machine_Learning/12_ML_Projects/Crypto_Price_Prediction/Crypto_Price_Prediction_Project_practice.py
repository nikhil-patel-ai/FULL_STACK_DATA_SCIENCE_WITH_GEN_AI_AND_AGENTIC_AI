"""
Crypto Price Prediction Project

Goal: Inspect project files and outline safe reproducibility checks before running a prediction app.

Run from this folder with:
    python "Crypto_Price_Prediction_Project_practice.py"

This is a learning example. Review the code and dependencies before using it in production.
"""

from pathlib import Path

project_dir = Path.cwd()
print("Project folder:", project_dir)
for path in sorted(project_dir.iterdir()):
    print(("DIR " if path.is_dir() else "FILE"), path.name)

print("\nBefore running the app:")
print("1. Read the source code and requirements.")
print("2. Check how the training data is split and whether future information leaks into features.")
print("3. Confirm model/scaler files match the feature order used by the app.")
print("4. Do not treat crypto price predictions as guaranteed financial advice.")
