# Term Frequency–Inverse Document Frequency (TF-IDF)

## 1. Overview

TF-IDF is a numeric text representation that weights a term according to how
important it is to a document relative to a collection of documents. A term
receives a higher weight when it appears often in one document but occurs in
relatively few documents in the corpus.

TF-IDF is commonly used for document search, information retrieval, text
classification, and as a weighted alternative to raw Bag of Words (BoW)
counts. It is a weighting scheme rather than a semantic embedding: it does
not understand word meaning or word order.

## 2. Key terms

- **Term:** A token or feature, usually a word or n-gram.
- **Document:** One text unit being represented, such as a sentence or
  article.
- **Corpus:** The collection of documents used to calculate document
  frequencies and fit the vectorizer.
- **Term frequency (TF):** How much a term contributes within a document.
- **Document frequency (DF):** The number of documents that contain a term.
- **Inverse document frequency (IDF):** A weight that decreases as a term
  occurs in more documents.
- **TF-IDF weight:** The term-frequency value adjusted by its IDF.

## 3. How TF-IDF works

### 3.1 Term frequency

A simple term frequency is the raw count:

```text
TF(t, d) = count of term t in document d
```

Other conventions normalize counts by document length or use logarithmic
scaling. Normalization helps avoid letting longer documents dominate only
because they contain more tokens.

### 3.2 Inverse document frequency

A common unsmoothed definition is:

```text
IDF(t) = log(N / DF(t))
```

where `N` is the number of documents in the corpus and `DF(t)` is the number
of documents containing term `t`. Rare terms receive a larger IDF, while
terms found in every document receive a smaller weight.

Implementations often smooth the calculation to avoid division by zero and
to keep weights well-defined. Scikit-learn's `TfidfVectorizer` uses smoothed
IDF by default:

```text
IDF(t) = log((1 + N) / (1 + DF(t))) + 1
```

### 3.3 Combine and normalize

The unnormalized weight is:

```text
TF-IDF(t, d) = TF(t, d) × IDF(t)
```

Scikit-learn then applies L2 normalization to each document vector by default.
This scales each nonzero row to unit length, making its direction more
important than its absolute magnitude.

### 3.4 Small illustration

Suppose the corpus is:

```text
Document 1: cat sat mat
Document 2: cat ate fish
Document 3: fish swam
```

The term `cat` appears in two of the three documents, while `mat` appears in
only one. The IDF of `mat` is therefore larger than the IDF of `cat`. Within
Document 1, both terms occur once, but `mat` receives the larger TF-IDF
weight because it is more distinctive across the corpus. Exact values depend
on the chosen TF, IDF smoothing, and normalization conventions.

## 4. TF-IDF compared with count-based BoW

| Property | Count BoW | TF-IDF |
| --- | --- | --- |
| Feature space | Vocabulary terms | Vocabulary terms |
| Basic value | Count or binary presence | Term frequency weighted by inverse document frequency |
| Effect of common corpus terms | May give them large counts | Reduces their relative weight |
| Word order and meaning | Not represented | Not represented |

TF-IDF does not remove common terms by itself; it down-weights terms that
appear across many documents. Stop-word filtering is a separate, optional
preprocessing decision.

## 5. Scikit-learn usage

`TfidfVectorizer` learns a vocabulary and calculates the weighted feature
matrix in one step:

```python
from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "cat sat mat",
    "cat ate fish",
    "fish swam",
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

print(vectorizer.get_feature_names_out())
print(X.toarray())
```

The matrix is sparse by default. Avoid converting a large matrix to a dense
array with `.toarray()` unless its size is known to be manageable.

For a train/test workflow, fit the vectorizer using training text only, then
transform the test text with the same fitted vocabulary and IDF weights:

```python
X_train = vectorizer.fit_transform(train_documents)
X_test = vectorizer.transform(test_documents)
```

Fitting on all documents before splitting can leak information about the test
set's vocabulary and document frequencies.

### 5.1 Useful `TfidfVectorizer` options

| Option | Purpose |
| --- | --- |
| `lowercase=True` | Convert text to lowercase (default). |
| `stop_words="english"` | Remove scikit-learn's built-in English stop words; check suitability for the task. |
| `ngram_range=(1, 2)` | Include single words and adjacent two-word sequences. |
| `min_df=2` | Ignore terms appearing in fewer than two documents. |
| `max_df=0.9` | Ignore terms appearing in more than 90% of documents. |
| `max_features=5000` | Limit vocabulary size. |
| `sublinear_tf=True` | Apply logarithmic scaling to term frequency. |
| `norm="l2"` | Normalize each row using the L2 norm (default); use `None` to disable normalization. |
| `use_idf=True` | Apply inverse document frequency (default). |

Choose options based on the corpus and evaluation results. In particular,
negation terms and domain-specific common words can be important, so do not
remove stop words automatically without checking.

## 6. Strengths and limitations

### 6.1 Strengths

- Simple, efficient, and often a strong baseline for text classification and
  retrieval.
- More informative than raw counts when common corpus-wide terms should have
  less influence.
- Feature weights can be inspected to understand which terms characterize a
  document.
- Works naturally with sparse matrices and linear models.

### 6.2 Limitations

- Ignores word order, syntax, and meaning.
- Different words with similar meanings remain unrelated features.
- Weights depend on the corpus: adding or removing documents can change IDF.
- A rare term is not necessarily useful; typos and noise may receive high
  weights if they occur in only a few documents.
- Unseen terms at inference time have no learned feature column.
- The representation can be large and sparse for a broad vocabulary.

## 7. Example in this folder

| File | Description |
| --- | --- |
| [TFIDF.py](TFIDF.py) | Uses a fixed paragraph, segments it into sentences, removes non-letter characters, lowercases, removes English stop words, and lemmatizes each token. It creates a count matrix (`X1`) and a TF-IDF matrix (`X`). |

The script keeps both matrices in memory and does not print or save them. It
uses NLTK for sentence tokenization, stop words, and WordNet lemmatization,
and scikit-learn for count and TF-IDF vectorization. NLTK may require the
corresponding tokenizer, stop-word, and WordNet resources to be available.
Because the script vectorizes sentences from a single paragraph, its weights
illustrate the calculation rather than provide a useful general-purpose model.

## 8. Diagram and notes

| Image | What it illustrates |
| --- | --- |
| [1.PNG](1.PNG) | Handwritten TF-IDF notes showing term-frequency values, inverse-document-frequency weights, and combining them to weight terms. |

The image is a study reference and is not read by the Python script.
