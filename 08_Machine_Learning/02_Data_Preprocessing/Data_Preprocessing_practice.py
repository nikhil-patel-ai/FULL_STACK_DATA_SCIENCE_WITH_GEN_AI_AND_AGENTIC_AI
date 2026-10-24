"""
Data Preprocessing

Goal: Load a dataset, inspect missing values, and prepare numeric and categorical columns.

Run from this folder with:
    python "Data_Preprocessing_practice.py"

This is a learning example. Review the code and dependencies before using it in production.
"""

import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Small example dataset so the notebook runs without external files.
df = pd.DataFrame({
    "age": [21, None, 25, 30],
    "city": ["Satna", "Maihar", None, "Satna"],
    "score": [70, 85, None, 90]
})
print("Original data:")
print(df)
print("\nMissing values:")
print(df.isna().sum())

numeric = df[["age", "score"]]
imputer = SimpleImputer(strategy="median")
numeric_filled = pd.DataFrame(imputer.fit_transform(numeric), columns=numeric.columns)
print("\nNumeric columns after median imputation:")
print(numeric_filled)

city_filled = df[["city"]].fillna("Unknown")
encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
print("\nEncoded city values:")
print(encoder.fit_transform(city_filled))
