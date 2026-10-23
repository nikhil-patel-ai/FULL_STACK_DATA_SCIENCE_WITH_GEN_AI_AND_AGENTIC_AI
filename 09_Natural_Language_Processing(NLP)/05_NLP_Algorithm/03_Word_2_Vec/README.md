# Word2Vec

## 1. Overview

Word2Vec is a family of shallow neural-network methods that learns a dense
vector for each word from its context in a text corpus. Words that occur in
similar contexts often receive vectors that are close in the learned vector
space.

Unlike BoW and TF-IDF, which produce explicit document-by-term features,
Word2Vec produces word embeddings. A separate aggregation step, such as
averaging word vectors, is needed when a single vector is required for an
entire sentence or document.

## 2. Important concepts

- **Token:** A word or other unit from the training text.
- **Context window:** Nearby tokens considered around a target word.
- **Embedding:** A learned, fixed-length numeric vector for a word.
- **Dimension:** The number of values in each embedding vector.
- **Vocabulary:** The words retained by the model after filtering.
- **Training corpus:** The text used to learn the word vectors.

For a vocabulary of `V` words and vector size `k`, the learned word-vector
table has approximately `V × k` values, in addition to training parameters.
Each word is represented by a vector of length `k`, rather than one scalar
count.

## 3. The two training approaches

Word2Vec is commonly trained using either of two objectives:

### 3.1 Continuous Bag of Words (CBOW)

CBOW predicts a target word from the words surrounding it. For example, the
context “the ___ barked” may be used to predict “dog.” CBOW is often efficient
for frequent words and larger datasets.

### 3.2 Skip-gram

Skip-gram uses a target word to predict nearby context words. Given “dog,” it
tries to predict surrounding words such as “the” or “barked.” It can be useful
for learning representations of less frequent words, though training may be
slower.

Gensim's `Word2Vec` supports both; its default `sg=0` selects CBOW, while
`sg=1` selects Skip-gram.

## 4. Training workflow

1. Collect a representative text corpus.
2. Normalize text and split it into sentences.
3. Tokenize each sentence into a list of tokens.
4. Optionally filter stop words and infrequent vocabulary items.
5. Train a CBOW or Skip-gram model using a chosen context window and vector
   size.
6. Inspect vectors and nearest-neighbor words.
7. Save and reuse the trained model when needed.

Word2Vec learns from local contexts, so sentence boundaries and tokenization
matter. It does not require a manually labeled dataset, but it does require
enough varied text for words to appear in meaningful contexts.

## 5. Using Gensim

```python
from gensim.models import Word2Vec

sentences = [
    ["the", "dog", "barked"],
    ["the", "cat", "slept"],
    ["a", "dog", "slept"],
]

model = Word2Vec(
    sentences,
    vector_size=50,
    window=3,
    min_count=1,
    workers=1,
    sg=1,
    seed=42,
)

dog_vector = model.wv["dog"]
neighbors = model.wv.most_similar("dog", topn=5)
```

Each sentence must be a sequence of tokens. Gensim 4 uses `vector_size` to
set embedding size; older releases used `size`. The example uses a tiny
corpus for API illustration only; meaningful embeddings generally require
much larger and more representative data.

### 5.1 Common training parameters

| Parameter | Meaning |
| --- | --- |
| `vector_size` | Number of dimensions in each learned word vector. |
| `window` | Maximum distance of context words from the target. |
| `min_count` | Ignore words with corpus frequency below this threshold. |
| `sg` | `0` for CBOW and `1` for Skip-gram. |
| `workers` | Number of worker threads used for training. |
| `epochs` | Number of training passes over the corpus. |
| `seed` | Random seed, useful for more repeatable experiments. |

Parameter choices depend on corpus size, language, and task. Increasing the
vector size or training time does not guarantee better results, particularly
when the corpus is small.

## 6. Working with learned vectors

- `model.wv["word"]` retrieves the learned vector for a vocabulary word.
- `model.wv.most_similar("word")` returns words with high cosine similarity
  to that word.
- `model.wv.similarity("word1", "word2")` compares two in-vocabulary words.
- In Gensim 4, `model.wv.key_to_index` maps vocabulary words to their indices.
- A sentence vector can be formed by aggregating its word vectors, for
  example by averaging; this simple approach ignores word order and needs
  handling for out-of-vocabulary words.

Similarity indicates proximity in the learned space, not identity, causation,
or a guaranteed human judgment of relatedness. Nearest neighbors can reflect
topic, usage, or biases present in the training corpus.

## 7. Strengths and limitations

### 7.1 Strengths

- Learns dense representations from unlabeled text.
- Can place words used in similar contexts near one another.
- Requires fewer dimensions than a one-column-per-vocabulary BoW matrix.
- Provides word vectors that can be reused in downstream NLP tasks.

### 7.2 Limitations

- A standard Word2Vec model assigns one vector per word and does not
  distinguish senses by context; “bank” has the same vector in every
  sentence.
- Word order is not represented directly in an individual word vector.
- Words absent from the training vocabulary have no learned vector.
- Quality depends on corpus size, domain, preprocessing, and training
  settings.
- Corpus biases and stereotypes can be reflected in vector relationships.
- Similarity scores are not guaranteed to match human interpretation.
- The model must be trained or loaded; it does not produce useful embeddings
  from a handful of unrelated examples.

## 8. Comparison with BoW and TF-IDF

| Method | What it represents | Context or semantic similarity | Typical output |
| --- | --- | --- | --- |
| BoW | Document term counts or presence | No | Sparse document-term matrix |
| TF-IDF | Corpus-adjusted document term weights | No | Sparse weighted document-term matrix |
| Word2Vec | Words learned from neighboring contexts | Often captures contextual similarity | Dense word vectors |

See the sibling [BoW guide](../01_BOW/README.md) and
[TF-IDF guide](../02_TFIDF/README.md) for the other text representations.

## 9. Example in this folder

| File | Description |
| --- | --- |
| [WORD2VEC.py](WORD2VEC.py) | Normalizes a fixed sample paragraph, segments it into sentences, tokenizes each sentence, removes English stop words, trains Gensim Word2Vec with `min_count=1`, retrieves the vector for `war`, and queries similar words for several terms. |

The variables `model`, `vector`, and `similar` remain in memory; the script
does not print or save the results. The training corpus is only one short
paragraph, so the learned vectors and similarity rankings are not reliable
language representations.

### 9.1 Gensim version compatibility

The script reads `model.wv.vocab`, which was removed in Gensim 4. In Gensim
4, use `model.wv.key_to_index` to inspect the vocabulary. The script also
needs NLTK sentence and word tokenizers and English stop-word data.

## 10. Diagrams and notes

| Image | What it illustrates |
| --- | --- |
| [1.PNG](1.PNG) | Word2Vec concept diagram showing word groups and relationships such as gender, family, number, and geography. |
| [2.PNG](2.PNG) | Limitations of BoW and TF-IDF: they do not retain semantic information, TF-IDF emphasizes uncommon words, and high-dimensional representations can contribute to overfitting. |
| [3.PNG](3.PNG) | Vocabulary/matrix illustration introducing how word co-occurrence information can be organized. |
| [4.PNG](4.PNG) | Summary of Word2Vec: words are represented by multi-dimensional vectors that can preserve semantic relationships. |
| [5.PNG](5.PNG) | Two-dimensional sketch of word vectors, with example coordinates for words such as “man,” “women,” and “play.” |
| [6.PNG](6.PNG) | Vector-arithmetic illustration of the familiar “king − man + woman ≈ queen” analogy. |
| [7.PNG](7.PNG) | Outline of a Word2Vec workflow: tokenize, gather frequency/context information, select frequent words, and create word representations. |

These images are study notes and are not loaded by the Python script.
