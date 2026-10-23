# Natural Language Processing (NLP)

Natural Language Processing is a branch of artificial intelligence that helps
computers work with human language. NLP systems can classify, search, extract
information from, summarize, translate, or generate text and speech.

This guide introduces the main ideas, explains common techniques with Python
examples, and points to the lessons in this folder. The code blocks are
teaching examples; the notebooks remain the source for the course exercises.

## Contents

- [NLP, NLU, and NLG](#nlp-nlu-and-nlg)
- [A typical NLP workflow](#a-typical-nlp-workflow)
- [Text preparation and tokenization](#text-preparation-and-tokenization)
- [Stemming, lemmatization, and stop words](#stemming-lemmatization-and-stop-words)
- [Linguistic analysis: POS and entities](#linguistic-analysis-pos-and-entities)
- [Representing text as numbers](#representing-text-as-numbers)
- [A simple text-classification example](#a-simple-text-classification-example)
- [Similarity, embeddings, and language models](#similarity-embeddings-and-language-models)
- [Natural Language Generation](#natural-language-generation)
- [Evaluation and responsible use](#evaluation-and-responsible-use)
- [Folder contents and study path](#folder-contents-and-study-path)
- [Python setup](#python-setup)

## NLP, NLU, and NLG

- **NLP** is the broad area of working with language using software.
- **Natural Language Understanding (NLU)** analyzes language to infer useful
  information: for example, intent, sentiment, entities, or a document topic.
- **Natural Language Generation (NLG)** creates language: for example, a
  chatbot response, a summary, or a report generated from structured data.

An assistant often uses both: NLU interprets “Will it rain in Delhi tomorrow?”
as a weather request with a location and date; NLG turns the forecast into a
helpful sentence.

Common applications include search, spam filtering, translation, speech
interfaces, question answering, sentiment analysis, document classification,
and information extraction.

## A typical NLP workflow

1. **Define the task.** Decide what the system should predict, extract, or
   generate, and how success will be measured.
2. **Collect and inspect data.** Check its source, language, quality, labels,
   and privacy constraints.
3. **Prepare text.** Apply only transformations that are useful for the task.
4. **Represent text.** Convert words or passages into features or vectors.
5. **Train or apply a method.** This might be a rule, a statistical model, or a
   pretrained language model.
6. **Evaluate and improve.** Test on data not used to train the model; inspect
   errors and monitor performance after deployment.

There is no universal preprocessing recipe. Lowercasing, removing punctuation,
or deleting common words can help one task and damage another. For example,
removing “not” can reverse sentiment: “not helpful” is not the same as
“helpful.”

## Text preparation and tokenization

**Normalization** makes selected text forms more consistent. Typical choices
include lowercasing, handling whitespace, and deciding how to treat URLs,
numbers, punctuation, emoji, and contractions. Keep the original text if later
steps may need it.

**Tokenization** splits text into units called tokens. Depending on the task,
tokens may be sentences, words, subwords, or characters. Tokenizers differ in
how they handle punctuation and contractions.

```python
import re

text = "NLP is useful! It helps computers process language."
tokens = re.findall(r"\b[\w']+\b|[^\w\s]", text.lower())

print(tokens)
# ['nlp', 'is', 'useful', '!', 'it', 'helps', 'computers',
#  'process', 'language', '.']
```

This regular-expression example is intentionally simple. It is useful for
learning, but it is not a complete language-aware tokenizer.

An **n-gram** is a sequence of `n` neighboring tokens. Unigrams contain one
token, bigrams two, and trigrams three. For “natural language processing,” the
bigrams are “natural language” and “language processing.” N-grams retain some
local word order and can be useful in search and classification.

## Stemming, lemmatization, and stop words

**Stemming** applies rules to shorten words to a stem. The result may not be a
valid word: a stemmer might reduce “studies” to “studi.” Stemming is often
fast, but can be linguistically rough.

**Lemmatization** uses vocabulary and grammatical information to find a
dictionary form, called a *lemma*. For example, “am,” “is,” and “are” can map
to “be.” The result can depend on context, part of speech, and language
resources.

NLTK example (requires the NLTK package and WordNet data):

```python
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download("wordnet")
nltk.download("omw-1.4")

words = ["studies", "playing", "better"]
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

for word in words:
    print(word, "-> stem:", stemmer.stem(word),
          "| noun lemma:", lemmatizer.lemmatize(word))

print(lemmatizer.lemmatize("running", pos="v"))  # run
```

The lemmatizer's default part of speech is noun, so giving it a verb label can
change the result.

**Stop words** are frequent words (such as “the” or “and”) that some workflows
exclude because they may add little signal. Whether to remove them is a
task-specific choice. Keep negations, modal verbs, and other meaningful words
when they matter to the task.

## Linguistic analysis: POS and entities

**Part-of-speech (POS) tagging** assigns grammatical categories—such as noun,
verb, adjective, or adverb—to tokens in context. It can support parsing,
lemmatization, and information extraction.

**Named Entity Recognition (NER)** locates and labels mentions of people,
organizations, places, dates, and other entity types. In “Maya works at Acme
in Paris,” an NER system might label “Maya” as a person, “Acme” as an
organization, and “Paris” as a location. Entity recognition is model- and
domain-dependent; the same name can refer to different things in different
contexts.

NLTK includes POS tagging and a basic named-entity chunker. Their required
language data packages depend on the NLTK version; download the resources
requested by the installed version if you run these examples:

```python
import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

sentence = "Maya works at Acme in Paris."
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)
entities = ne_chunk(tagged)

print(tagged)
print(entities)
```

## Representing text as numbers

Most machine-learning algorithms work with numbers, so text must be converted
to a numeric representation.

### Bag of Words

**Bag of Words (BoW)** records which vocabulary terms appear and how often,
without preserving their order. For example, “cats chase mice” and “mice chase
cats” have the same basic unigram counts. This makes BoW simple and useful for
baselines, but it loses word order and deeper meaning.

### TF-IDF

**Term Frequency–Inverse Document Frequency (TF-IDF)** gives a term a larger
weight when it is frequent in a document but less common across the collection.
It can reduce the influence of words that occur in nearly every document.

```python
from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "the team won the match",
    "the team trained for the match",
    "a new recipe uses fresh herbs",
]

vectorizer = TfidfVectorizer()
matrix = vectorizer.fit_transform(documents)

print(vectorizer.get_feature_names_out())
print(matrix.shape)  # (number of documents, number of vocabulary terms)
```

The output is a sparse matrix: most documents contain only a small fraction of
the full vocabulary.

### Word and sentence embeddings

An **embedding** is a dense numeric vector intended to capture useful
properties of a word, sentence, or document. Unlike basic BoW, embeddings can
represent relationships between terms. Contextual models can assign different
vectors to the same word depending on its surrounding text.

Embeddings are used for semantic search, clustering, recommendations, and
language-model applications. They require a suitable model, and similarity
between vectors should not be treated as proof that two statements mean
exactly the same thing.

## A simple text-classification example

Text classification assigns a label to a passage, such as *positive* or
*negative* sentiment, *spam* or *not spam*, or a document topic. This example
uses TF-IDF features and logistic regression from scikit-learn:

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

train_texts = [
    "The service was friendly and quick",
    "The meal was delicious",
    "The order arrived late",
    "The food was cold and disappointing",
]
train_labels = ["positive", "positive", "negative", "negative"]

model = make_pipeline(
    TfidfVectorizer(ngram_range=(1, 2)),
    LogisticRegression(),
)
model.fit(train_texts, train_labels)

print(model.predict(["friendly service and delicious food"]))
```

This tiny dataset demonstrates the API, not a production-quality sentiment
system. Real projects need representative labeled examples, a held-out
evaluation set, error analysis, and checks for class imbalance and data
leakage.

## Similarity, embeddings, and language models

**Cosine similarity** measures the angle between two non-zero vectors. It is
commonly used to compare text vectors; values closer to 1 indicate a smaller
angle, but the practical meaning depends on the representation and task.

**Large language models (LLMs)** are neural models trained on large collections
of text to predict or generate sequences. They can perform tasks such as
summarization, question answering, and drafting, often by following an
instruction. They may also produce incorrect or unsupported statements,
reflect biases in their data, or behave inconsistently. Verify important
outputs and protect private data when using external services.

**PCA (Principal Component Analysis)** is a dimensionality-reduction method
that projects numeric data onto directions capturing as much variance as
possible. It is not itself an NLP method, but it can be used to explore or
visualize numerical text features and embeddings. PCA plots are an
approximation: distances in a low-dimensional projection may not preserve all
relationships in the original space.

## Natural Language Generation

NLG produces text from data, instructions, or a model. It may be template-based,
rule-based, or model-based. A simple template makes the relationship between
structured data and generated text explicit:

```python
forecast = {"city": "Delhi", "temperature_c": 29, "condition": "cloudy"}
summary = (
    f"In {forecast['city']}, it is {forecast['condition']} "
    f"with a temperature of {forecast['temperature_c']}°C."
)
print(summary)
```

This is controlled template generation, not open-ended language generation.
Generated content should be checked for relevance, factual accuracy, tone, and
whether it includes information that was not present in the input.

The existing `03_NLG/NLG.ipynb` includes introductory exercises and a word
cloud. A word cloud visualizes word frequency; it does **not** generate new
sentences or summaries.

## Evaluation and responsible use

Choose metrics that match the task:

- **Classification:** accuracy, precision, recall, F1 score, and a confusion
  matrix. Accuracy alone can be misleading when classes are imbalanced.
- **Information extraction:** precision, recall, and F1 for entity or span
  predictions.
- **Text generation:** automatic overlap or similarity metrics can help
  compare outputs, but human review is often needed for factuality, relevance,
  readability, and safety.

Always test on data that was not used to fit the model. Look at individual
errors, consider whose language or dialect is represented in the data, and
avoid treating model scores as a substitute for judgment. Consider privacy,
consent, bias, and the consequences of incorrect predictions.

## Folder contents and study path

| Folder | What it contains |
| --- | --- |
| [`01_NLP_INTRO`](01_NLP_INTRO) | Numbered visual notes introducing NLP, its applications, NLU/NLG, and core concepts. |
| [`02_NLU`](02_NLU) | `NLP.ipynb` plus focused tokenization, stemming, and lemmatization materials; the notebook also introduces n-grams, stop words, POS tagging, NER, and a word cloud. |
| [`03_NLG`](03_NLG) | `NLG.ipynb`, introductory exercises, and a word-cloud demonstration. |
| [`04_PCA _MATH_TECHNIQUES`](04_PCA%20_MATH_TECHNIQUES) | Visual notes and materials about PCA and related mathematical techniques. |

Recommended order:

1. Read the numbered introduction notes in `01_NLP_INTRO`.
2. Work through `02_NLU/NLP.ipynb` for the processing concepts.
3. Compare the focused examples in `02_NLU/01_TOKENIZATION`,
   `02_NLU/02_STEMMING`, and `02_NLU/03_LEMMATIZATION`.
4. Study the NLG background and notebook in `03_NLG`.
5. Review the PCA notes after learning how text is represented numerically.

Open notebooks in Jupyter Notebook, JupyterLab, or VS Code and run cells in
order. Visual notes are images and are not executable code.

## Python setup

The course notebooks use NLTK; the word-cloud demonstrations use `wordcloud`
and `matplotlib`. The classification example uses scikit-learn. Install only
the packages needed for the examples you plan to run:

```bash
python -m pip install nltk scikit-learn wordcloud matplotlib
```

Some NLTK features also require separate language data, such as tokenizer,
WordNet, POS-tagger, or NER resources. If an NLTK example reports a missing
resource, follow the error message and download the resource for that
specific feature. Resource names can differ between NLTK versions.
