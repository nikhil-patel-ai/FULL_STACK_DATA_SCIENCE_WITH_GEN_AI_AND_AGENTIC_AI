"""\nModel Artifacts\n\nLearning goal: Inventory saved model artifacts and remember that pickle files should only be loaded from trusted sources.\nRun with: python "Model_Artifacts_practice.py"\n"""\n\nfrom pathlib import Path
for file in sorted(Path.cwd().glob("*.pkl")):
    print(f"{file.name}: {file.stat().st_size:,} bytes")
print("Only load model files from sources you trust.")\n