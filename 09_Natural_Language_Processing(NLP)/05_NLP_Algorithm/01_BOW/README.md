# Bag of Words (BoW)

## 1. Overview

Bag of Words is a way to turn text into numeric features for machine-learning
algorithms. It represents a collection of documents using a vocabulary of
terms and records how often each vocabulary term occurs in each document.
“Bag” refers to the fact that the representation ignores the order of words:
documents with the same term counts have the same vector, even if their
sentences are arranged differently.

BoW is a useful baseline for tasks such as document classification, spam
detection, topic exploration, and search. It is simple and interpretable, but
does not understand meaning, grammar, or context.

## 2. Core concepts

- **Document:** One text item to represent. Depending on the task, it may be a
  sentence, review, email, article, or another text unit.
- **Corpus:** The collection of documents used to build and apply a text
  representation.
- **Token:** A unit extracted from text, usually a word.
- **Vocabulary:** The unique tokens selected from the corpus. Each vocabulary
  item is assigned a feature/column.
- **Document-term matrix (DTM):** A matrix with one row per document and one
  column per vocabulary item.

For a corpus with `D` documents and a vocabulary of `V` terms, the DTM has
shape `D × V`. Its entry `X[i, j]` is the value for term `j` in document `i`.
The feature names and their column positions must stay consistent when the
matrix is used by a model.

## 3. How it works

1. Choose the documents that make up the corpus.
2. Normalize and tokenize the text as appropriate for the task.
3. Build a vocabulary from the training documents.
4. Assign each vocabulary term a column.
5. For each document, fill the vector with term counts or binary presence
   values.
6. Use the resulting vectors as input features for a model.

### 3.1 Worked example

Consider these three short documents:

```text
Document 1: small dog
Document 2: cute cute cat
Document 3: cute dog
```

The sorted vocabulary is `cat`, `cute`, `dog`, `small`. The count-based
document-term matrix is:

| Document | cat | cute | dog | small |
| --- | ---: | ---: | ---: | ---: |
| Document 1 | 0 | 0 | 1 | 1 |
| Document 2 | 1 | 2 | 0 | 0 |
| Document 3 | 0 | 1 | 1 | 0 |

The value `2` for `cute` in Document 2 shows that counts preserve repeated
occurrences. A **binary BoW** representation changes every positive count to
`1`, so it records only whether a term appears, not how many times.

## 4. Count and binary representations

- **Count BoW:** Stores the number of times a term occurs. This is the default
  behavior of scikit-learn's `CountVectorizer`.
- **Binary BoW:** Stores `1` when a term occurs and `0` otherwise. This can be
  useful when presence matters more than repetition; in scikit-learn, use
  `CountVectorizer(binary=True)`.

Both variants preserve token identity but discard word order and semantic
relationships. The count vector for a repeated word may have a value greater
than one; the binary vector never does.

## 5. Text preparation

Preprocessing decisions affect the vocabulary and every feature vector. A
typical pipeline may include:

1. **Sentence segmentation:** Split a long text into sentence-level
   documents, when sentences are the desired unit.
2. **Normalization:** Lowercase text so `Word` and `word` are treated alike.
3. **Cleaning:** Remove or normalize punctuation, numbers, markup, or other
   content that is not useful for the task.
4. **Tokenization:** Split text into tokens.
5. **Stop-word filtering:** Optionally remove frequent function words such as
   “the” and “is.”
6. **Stemming or lemmatization:** Optionally map related forms to a common
   root or dictionary form.
7. **Vectorization:** Learn the vocabulary and create the document-term
   matrix.

These are choices, not universal requirements. For example, numbers, negation
words (“not”), punctuation, and word forms can carry important information in
some tasks. Choose preprocessing based on the language and problem, and fit
data-dependent steps only on the training split.

## 6. Scikit-learn example

`CountVectorizer` combines tokenization, vocabulary construction, and count
matrix creation:

```python
from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "small dog",
    "cute cute cat",
    "cute dog",
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)

print(vectorizer.get_feature_names_out())
print(X.toarray())
```

`fit_transform` learns the vocabulary from the supplied documents and returns
their feature matrix. For supervised learning, split the data first, fit only
on the training text, and use the learned vocabulary to transform the test
text:

```python
X_train = vectorizer.fit_transform(train_documents)
X_test = vectorizer.transform(test_documents)
```

Do not call `fit` or `fit_transform` independently on test data: that would
create a different feature space and expose information from the test set to
the preprocessing step.

### 6.1 Useful `CountVectorizer` options

| Option | Purpose |
| --- | --- |
| `lowercase=True` | Convert text to lowercase (the default). |
| `stop_words="english"` | Filter scikit-learn's built-in English stop-word list. Review whether this is appropriate for the task. |
| `binary=True` | Use presence/absence values instead of term counts. |
| `ngram_range=(1, 2)` | Include unigrams and bigrams, such as `machine` and `machine learning`. |
| `min_df=2` | Ignore terms appearing in fewer than two documents. |
| `max_df=0.9` | Ignore terms appearing in more than 90% of documents. |
| `max_features=5000` | Limit the vocabulary to the most frequent features. |

N-grams preserve limited local word order, but increase the number of
features. Vocabulary limits can reduce memory use and noise, but may remove
useful rare terms.

## 7. Sparse matrices and scale

Most documents contain only a small fraction of all vocabulary terms, so a
document-term matrix is usually sparse. `CountVectorizer.fit_transform`
returns a SciPy sparse matrix to avoid storing all the zeros. Keeping it
sparse is generally more memory-efficient. Calling `.toarray()` converts it
to a dense NumPy array and can consume substantial memory for large corpora.

## 8. Strengths and limitations

### 8.1 Strengths

- Simple to understand, implement, and explain.
- Produces explicit, interpretable word features.
- Works well as a baseline for many text-classification problems.
- Supports counts, binary features, and n-gram features.
- Efficient sparse storage is available for high-dimensional matrices.

### 8.2 Limitations

- Ignores word order and most syntax; “dog bites person” and “person bites
  dog” can have the same features.
- Does not represent meaning or similarity between different words such as
  “car” and “automobile.”
- Treats words as separate features, so related forms remain separate unless
  preprocessing or n-grams address them.
- Can create a very large, sparse vocabulary, especially with short or noisy
  text.
- Frequent terms can dominate raw counts; TF-IDF is an alternative weighting
  scheme when down-weighting corpus-wide common terms is useful.
- Rare or unseen words may not help the model, and words absent from the
  training vocabulary cannot create new features at inference time.

## 9. BoW compared with TF-IDF and Word2Vec

| Method | Feature values | Captures term frequency? | Captures semantic relationships? |
| --- | --- | --- | --- |
| Count BoW | Counts or binary presence | Yes | No |
| TF-IDF | Frequency adjusted by document rarity | Yes, with weighting | No |
| Word2Vec | Learned dense word vectors | Not as document term counts | Can capture contextual similarity |

The sibling [TF-IDF lesson](../02_TFIDF/README.md) covers TF-IDF in more detail;
[Word2Vec](../03_Word_2_Vec/README.md) covers dense context-based embeddings.

## 10. Examples in this folder

| File | Description |
| --- | --- |
| [BOW.py](BOW.py) | Uses a fixed paragraph, segments it into sentences, removes non-letter characters, lowercases, removes English stop words, and lemmatizes tokens. It creates a count matrix named `X_bow` and also a TF-IDF matrix named `X_tf`. |
| [BowCW.py](BowCW.py) | A second version of the same sentence-cleaning workflow. It creates a count matrix named `x_bow` and a TF-IDF matrix named `x_tf`. |

The scripts keep results in memory and do not print or save the matrices. They
require NLTK and scikit-learn. NLTK may need sentence-tokenizer, English
stop-word, and WordNet resources downloaded for the selected environment. The
scripts construct the stop-word set during each sentence's processing; for
larger corpora, prepare it once before the loop for better efficiency.

## 11. Diagrams and notes

| Image | What it illustrates |
| --- | --- |
| [1.PNG](1.PNG) | Handwritten example of removing stop words from sentences before forming a BoW representation. |
| [2.PNG](2.PNG) | Handwritten example showing a vocabulary, term frequencies, and a sentence-by-term binary BoW matrix. |
| [3.png](3.png) | Converts short text examples into a word-count matrix, including repeated words. |
| [4.png](4.png) | Example document-term table showing the count of each vocabulary word per sentence. |
| [5bow.png](5bow.png) | BoW example mapping four short sentences to a vocabulary and binary count vectors. |

These images are lesson references and are not loaded by the Python scripts.
