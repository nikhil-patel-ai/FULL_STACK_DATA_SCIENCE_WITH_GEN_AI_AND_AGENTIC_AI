"""\nClassification Datasets\n\nLearning goal: Inspect CSV files before modeling and verify that the target label is not accidentally included as a feature.\nRun with: python "Classification_Datasets_practice.py"\n"""\n\nfrom pathlib import Path
import pandas as pd

for file in sorted(Path.cwd().rglob("*.csv")):
    try:
        df = pd.read_csv(file)
        print(f"\n{file.relative_to(Path.cwd())}: shape={df.shape}")
        print(df.head(3))
    except Exception as exc:
        print(file.name, "could not be read:", exc)\n