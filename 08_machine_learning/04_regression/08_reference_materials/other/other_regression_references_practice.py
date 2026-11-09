"""\nOther Regression References\n\nLearning goal: Review any additional source materials retained from the original folder.\nRun with: python "Other_Regression_References_practice.py"\n"""\n\nfrom pathlib import Path
for path in sorted(Path.cwd().rglob("*")):
    if path.is_file():
        print(path.relative_to(Path.cwd()))\n