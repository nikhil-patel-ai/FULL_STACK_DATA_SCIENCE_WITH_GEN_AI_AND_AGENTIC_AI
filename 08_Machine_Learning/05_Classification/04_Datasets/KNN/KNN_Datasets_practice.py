"""\nKNN Datasets\n\nLearning goal: Inspect the datasets used in the KNN exercises.\nRun with: python "KNN_Datasets_practice.py"\n"""\n\nfrom pathlib import Path
import pandas as pd
for file in sorted(Path.cwd().glob("*.csv")):
    df = pd.read_csv(file, nrows=5)
    print(f"\n{file.name}: sample shape={df.shape}")
    print(df.head(2))\n