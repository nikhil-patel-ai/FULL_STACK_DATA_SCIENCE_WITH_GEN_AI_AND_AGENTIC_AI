"""\nClassification Projects\n\nLearning goal: Use the project checklist to define the label, split data correctly, select metrics, and document limitations.\nRun with: python "Classification_Projects_practice.py"\n"""\n\ntasks = [
    "Define the prediction target and business question",
    "Check class balance and missing values",
    "Split training and test data before fitting preprocessing",
    "Train a baseline model",
    "Evaluate precision, recall, F1-score, and confusion matrix",
    "Inspect false positives and false negatives",
    "Document limitations and reproducibility steps",
]
for i, task in enumerate(tasks, 1):
    print(f"{i}. {task}")\n