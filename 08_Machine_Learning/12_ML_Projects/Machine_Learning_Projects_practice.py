"""
Machine Learning Projects

Goal: Follow a reusable checklist for an end-to-end ML project.

Run from this folder with:
    python "Machine_Learning_Projects_practice.py"

This is a learning example. Review the code and dependencies before using it in production.
"""

from pathlib import Path

# Reusable project checklist; run this from the project folder.
checklist = [
    "Define the problem and success metric",
    "Inspect and understand the dataset",
    "Split data before fitting preprocessing steps",
    "Build a baseline model",
    "Evaluate on held-out data",
    "Check errors, bias, leakage, and limitations",
    "Save the model and document how to reproduce it",
]
for index, task in enumerate(checklist, start=1):
    print(f"{index}. {task}")

print("\nCurrent working directory:", Path.cwd())
print("Keep private credentials and large generated artifacts out of public repositories.")
