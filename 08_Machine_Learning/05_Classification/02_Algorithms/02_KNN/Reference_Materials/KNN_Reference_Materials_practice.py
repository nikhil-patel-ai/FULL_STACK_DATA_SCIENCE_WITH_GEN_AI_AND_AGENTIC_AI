"""\nKNN Reference Materials\n\nLearning goal: Use the original KNN PDF and explanatory documents to support the practical notebook.\nRun with: python "KNN_Reference_Materials_practice.py"\n"""\n\nfrom pathlib import Path
for path in sorted(Path.cwd().iterdir()):
    print(path.name)\n