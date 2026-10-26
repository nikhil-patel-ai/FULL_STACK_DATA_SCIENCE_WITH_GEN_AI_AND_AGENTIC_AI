"""\nRegression Reference Materials\n\nLearning goal: Use the trainer PDFs and archived statistics resources as reference material alongside the practice notebooks.\nRun with: python "Regression_Reference_Materials_practice.py"\n"""\n\nfrom pathlib import Path
for path in sorted(Path.cwd().rglob("*")):
    if path.is_file():
        print(path.relative_to(Path.cwd()))\n