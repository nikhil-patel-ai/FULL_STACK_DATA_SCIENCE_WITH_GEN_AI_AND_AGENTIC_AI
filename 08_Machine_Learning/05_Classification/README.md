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
| `01_Classification_Fundamentals/` | Introductory concepts and original starter files |
| `02_Algorithms/01_Logistic_Regression/` | Logistic Regression |
| `02_Algorithms/02_KNN/` | KNN scripts, notes, and image references |
| `02_Algorithms/03_Decision_Trees/` | Decision tree notes and practice |
| `02_Algorithms/04_Naive_Bayes/` | Naive Bayes notes and practice |
| `02_Algorithms/05_SVM/` | SVM scripts, notes, and math-image references |
| `03_Model_Evaluation/` | Classification metrics and evaluation practice |
| `04_Datasets/` | Shared and algorithm-specific datasets |
| `05_Projects/` | Original prediction project materials |
| `99_Reference_Materials/` | Additional documents |

## Practice file convention

Each meaningful topic folder has a matching `*_practice.py` and `*_practice.ipynb`.
Original notebooks, scripts, PDFs, datasets, and images are retained. Starter examples use
scikit-learn datasets where possible, so the learning code does not depend on local CSV paths.

## Suggested packages

```bash
pip install numpy pandas scikit-learn jupyter
```
