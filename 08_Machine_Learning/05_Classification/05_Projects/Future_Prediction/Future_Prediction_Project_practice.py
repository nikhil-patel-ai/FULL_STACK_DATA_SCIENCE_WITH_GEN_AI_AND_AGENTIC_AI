"""\nFuture Prediction Project\n\nLearning goal: Inspect the original future-prediction project files and verify the target, feature definitions, and data leakage risks.\nRun with: python "Future_Prediction_Project_practice.py"\n"""\n\nfrom pathlib import Path
for path in sorted(Path.cwd().iterdir()):
    print(("Folder " if path.is_dir() else "File   ") + path.name)
print("\nBefore using a prediction model, confirm its training features match inference features.")\n