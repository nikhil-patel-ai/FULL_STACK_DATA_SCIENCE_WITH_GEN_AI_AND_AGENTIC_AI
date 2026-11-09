# Machine Learning — Learning Roadmap

This repository organizes the files from the original `08_machine_learning` folder into a beginner-friendly learning order. It keeps the original materials (code, notebooks, datasets, PDFs, images, and project assets) while grouping them by topic.

## Recommended learning order

1. [01 — ML Fundamentals](01_ml_fundamentals/README.md)
2. [02 — Data Preprocessing](02_data_preprocessing/README.md)
3. [03 — Feature Engineering](03_feature_engineering/README.md)
4. [04 — Regression](04_regression/README.md)
5. [05 — Classification](05_classification/README.md)
6. [06 — Clustering](06_clustering/README.md)
7. [07 — Dimensionality Reduction](07_dimensionality_reduction/README.md)
8. [08 — Ensemble Learning](08_ensemble_learning/README.md)
9. [09 — Model Evaluation](09_model_evaluation/README.md)
10. [10 — Hyperparameter Tuning](10_hyperparameter_tuning/README.md)
11. [11 — Specialized ML](11_specialized_ml/README.md)
12. [12 — ML Projects](12_ml_projects/README.md)
13. [99 — Reference Materials](99_reference_materials/README.md)

## Standard note-taking template

For each concept, use this order:

- **Definition:** Explain the concept in simple language.
- **Why it is needed:** Describe the problem it solves.
- **Core intuition:** Explain how it works.
- **Mathematics:** Add equations and a small worked example when useful.
- **Python:** Include a runnable example with comments.
- **Practice:** Add numerical and coding questions.
- **ML application:** Explain where it is used.
- **Interview questions:** Add short questions and answers.

## Repository inventory

- Original files included: **202**
- File types include Python scripts, Jupyter notebooks, datasets, PDFs, images, model files, spreadsheets, and project assets.
- `file_map.csv` maps every original file path to its new location.
- `99_reference_materials` contains broader learning PDFs (for example, Python, NumPy, pandas, NLP, and GenAI) that were stored inside the original ML folder but do not all belong to core ML.

## Important notes

- This is a **file organization**, not a claim that every notebook/script has been tested or every PDF rewritten.
- Existing model `.pkl` files are binary artifacts; load only trusted pickle files.
- Before publishing datasets or project assets publicly, check that they do not contain personal, confidential, or licensed data.
- Large files may be subject to GitHub repository limits. GitHub blocks individual files larger than 100 MB.


## Python practice files

Each folder now includes a matching `*_practice.py` script and `*_practice.ipynb` notebook.
The practice files provide a runnable starting point for the topic; original notebooks,
scripts, datasets, PDFs, and project assets are retained. Some data/resource folders use
a file-inventory exercise because they mainly contain images, datasets, or reference files.

**Suggested environment**
```bash
pip install numpy pandas scikit-learn
```
Some original projects may require additional packages listed in their own `requirements.txt`.
