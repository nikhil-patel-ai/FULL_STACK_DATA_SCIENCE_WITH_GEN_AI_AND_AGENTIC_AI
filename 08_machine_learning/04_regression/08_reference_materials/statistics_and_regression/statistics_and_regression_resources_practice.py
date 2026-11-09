"""\nStatistics and Regression Resources\n\nLearning goal: Review supporting statistics resources before applying regression models.\nRun with: python "Statistics_and_Regression_Resources_practice.py"\n"""\n\nfrom pathlib import Path
for path in sorted(Path.cwd().iterdir()):
    print(("Folder: " if path.is_dir() else "File: ") + path.name)\n