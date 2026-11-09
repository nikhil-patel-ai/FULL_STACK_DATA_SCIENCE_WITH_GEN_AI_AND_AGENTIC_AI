# 05 — Classification

Classification is a supervised machine-learning task used to predict discrete class labels.

## Learning path

1. **Fundamentals** — classification workflow and problem types.
2. **Algorithms** — Logistic Regression → KNN → Decision Trees → Naive Bayes → SVM.
3. **Model evaluation** — confusion matrix, accuracy, precision, recall, F1-score, and ROC-AUC.
4. **Datasets** — inspect labels, missing values, class balance, and feature types.
5. **Projects** — review future-prediction materials and document leakage risks.
6. **Reference materials** — supporting algorithm documents.

## Folder map

| Folder | Purpose |
|---|---|
| `01_classification_fundamentals/` | Introductory concepts and original starter files |
| `02_algorithms/01_logistic_regression/` | Logistic Regression |
| `02_algorithms/02_knn/` | KNN scripts, notes, and image references |
| `02_algorithms/03_decision_trees/` | Decision tree notes and practice |
| `02_algorithms/04_naive_bayes/` | Naive Bayes notes and practice |
| `02_algorithms/05_svm/` | SVM scripts, notes, and math-image references |
| `03_model_evaluation/` | Classification metrics and evaluation practice |
| `04_datasets/` | Shared and algorithm-specific datasets |
| `05_projects/` | Original prediction project materials |
| `99_reference_materials/` | Additional documents |

## Practice file convention

Each meaningful topic folder has a matching `*_practice.py` and `*_practice.ipynb`.
Original notebooks, scripts, PDFs, datasets, and images are retained. Starter examples use
scikit-learn datasets where possible, so the learning code does not depend on local CSV paths.

## Suggested packages

```bash
pip install numpy pandas scikit-learn jupyter
```
