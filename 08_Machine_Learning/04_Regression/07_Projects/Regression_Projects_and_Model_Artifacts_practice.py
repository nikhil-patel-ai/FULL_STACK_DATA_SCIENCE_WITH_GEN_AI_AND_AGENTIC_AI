"""\nRegression Projects and Model Artifacts\n\nLearning goal: Review model artifacts and web-app files. Verify preprocessing and feature order before using saved models.\nRun with: python "Regression_Projects_and_Model_Artifacts_practice.py"\n"""\n\nfrom pathlib import Path

for path in sorted(Path.cwd().rglob("*")):
    if path.is_file():
        print(path.relative_to(Path.cwd()))
print("\nSecurity note: do not load pickle files from untrusted sources.")\n