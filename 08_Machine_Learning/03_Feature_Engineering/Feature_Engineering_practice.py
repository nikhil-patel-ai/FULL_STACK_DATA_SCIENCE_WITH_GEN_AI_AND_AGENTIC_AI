"""
Feature Engineering

Goal: Create useful features and apply common transformations.

Run from this folder with:
    python "Feature_Engineering_practice.py"

This is a learning example. Review the code and dependencies before using it in production.
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

df = pd.DataFrame({
    "height_cm": [150, 165, 180, 172],
    "weight_kg": [45, 60, 82, 68]
})
df["bmi"] = df["weight_kg"] / (df["height_cm"] / 100) ** 2
print("Engineered feature (BMI):")
print(df)

features = df[["height_cm", "weight_kg", "bmi"]]
print("\nStandardized features:")
print(StandardScaler().fit_transform(features))
print("\nMin-max scaled features:")
print(MinMaxScaler().fit_transform(features))
