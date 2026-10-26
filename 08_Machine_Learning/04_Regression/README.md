# 04 — Regression

Regression is a supervised machine-learning task used to predict a numeric target.

## Learning path

1. **Regression fundamentals** — understand features, targets, fitting, and prediction.
2. **Regression algorithms** — linear and polynomial regression.
3. **Regularization** — Ridge and Lasso; understand the bias/variance trade-off.
4. **Datasets** — inspect and prepare tabular data.
5. **Projects and model artifacts** — review existing web apps and saved models carefully.
6. **Reference materials** — trainer PDFs and statistics resources.

## Folder map

| Folder | Purpose |
|---|---|
| `01_Regression_Fundamentals/` | Concepts and original starter notebooks |
| `02_Regression_Algorithms/` | Algorithm scripts and practical examples |
| `03_Regularization/` | Ridge, Lasso, and original regularization files |
| `05_Datasets/` | CSV datasets used by regression lessons |
| `07_Projects/` | Existing web-app files and saved model artifacts |
| `08_Reference_Materials/` | PDFs, archived resources, and statistics references |

## Practice file convention

Meaningful topic folders contain a matching `*_practice.py` and `*_practice.ipynb`.
The original trainer files are retained in topic-appropriate locations. Practice examples are
learning starters; they are not a claim that every original application has been tested.

## Suggested packages

```bash
pip install numpy pandas scikit-learn jupyter
```

Some original web apps may need additional dependencies listed in their own `requirements.txt`.
Never load pickle files from an untrusted source.
