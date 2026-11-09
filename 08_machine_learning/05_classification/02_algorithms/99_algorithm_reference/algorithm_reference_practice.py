"""\nAlgorithm Reference\n\nLearning goal: Read reference PDFs for classification algorithms and map each document to its algorithm.\nRun with: python "Algorithm_Reference_practice.py"\n"""\n\nfrom pathlib import Path
for path in sorted(Path.cwd().iterdir()):
    print(path.name)\n