# NLP Algorithms

This section demonstrates three common ways to represent text numerically for
machine-learning workflows: Bag of Words (BoW), TF-IDF, and Word2Vec. The
examples use a short, fixed paragraph and include diagrams and study notes.

## 1. Topics

| Folder | Subject | Main example |
| --- | --- | --- |
| [01_BOW](01_BOW/README.md) | Bag of Words and count-based document vectors | `BOW.py`, `BowCW.py` |
| [02_TFIDF](02_TFIDF/README.md) | Term Frequency–Inverse Document Frequency | `TFIDF.py` |
| [03_Word_2_Vec](03_Word_2_Vec/README.md) | Context-based word embeddings with Word2Vec | `WORD2VEC.py` |

## 2. How the approaches differ

- **BoW** records how often vocabulary terms occur in each document. It is
  straightforward, but does not preserve word order or meaning.
- **TF-IDF** weights terms by their frequency in a document and how uncommon
  they are across the document collection. Common terms receive less weight.
- **Word2Vec** learns a dense vector for each word from its surrounding
  context. It can represent relationships between words, but needs enough
  representative training text to learn useful vectors.

## 3. Running the examples

The scripts use text embedded in the source files; they do not read an external
dataset or write output files. Run a script from a Python environment with its
dependencies installed, for example:

```bash
python .\01_BOW\BOW.py
```

Install the libraries used by the examples as needed: `nltk`, `scikit-learn`,
and (for Word2Vec) `gensim`. The NLTK examples also require its sentence and
word tokenizers, English stop-word list, and WordNet data. If NLTK reports a
missing resource, download the named resource using NLTK's downloader.

These are instructional examples rather than production pipelines. Their
preprocessing, vectorizer settings, and training data are intentionally small
and should be reviewed before adapting them to a real corpus.

## 4. Compatibility note

`WORD2VEC.py` accesses `model.wv.vocab`, an interface removed in Gensim 4.
With Gensim 4, use `model.wv.key_to_index` to inspect the vocabulary. The
remaining code also trains on only a short paragraph, so its learned
similarities are illustrative rather than reliable.
