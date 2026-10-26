"""\nRegression Datasets\n\nLearning goal: Inspect tabular datasets and identify target columns before modeling.\nRun with: python "Regression_Datasets_practice.py"\n"""\n\nfrom pathlib import Path
import pandas as pd

folder = Path.cwd()
for file in sorted(folder.glob("*.csv")):
    try:
        df = pd.read_csv(file)
        print(f"\n{file.name}: {df.shape}")
        print(df.head(3))
    except Exception as exc:
        print(f"Could not read {file.name}: {exc}")\n