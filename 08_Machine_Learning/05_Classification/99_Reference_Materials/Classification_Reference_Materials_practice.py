"""\nClassification Reference Materials\n\nLearning goal: Use this folder for additional documents that do not belong to one specific algorithm.\nRun with: python "Classification_Reference_Materials_practice.py"\n"""\n\nfrom pathlib import Path
for path in sorted(Path.cwd().rglob("*")):
    if path.is_file():
        print(path.relative_to(Path.cwd()))\n