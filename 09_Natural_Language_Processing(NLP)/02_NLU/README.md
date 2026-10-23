# Natural Language Understanding (NLU)

## What is NLU?

Natural Language Understanding (NLU) is the part of Natural Language
Processing (NLP) concerned with interpreting human language. It helps a
computer identify what text says and what it may mean, including its words,
structure, entities, and intent.

For example, an NLU system might analyze “Book a table for two tonight” to
identify the user's intent (make a reservation), the party size (two), and
the requested time (tonight). Real systems use context and task-specific
models; the techniques in this folder introduce several foundational text
analysis steps.

## What this folder covers

The notebook and examples introduce:

- **Tokenization:** Splitting text into sentences or word-like tokens so it
  can be processed. Different tokenizers may handle punctuation and
  contractions differently.
- **N-grams:** Grouping consecutive tokens to preserve some local word order.
  A bigram has two tokens, a trigram has three, and an *n*-gram has *n*
  tokens.
- **Stemming:** Applying a stemming algorithm to reduce related word forms
  to a stem. A stem may not be a valid dictionary word; Porter, Lancaster,
  and Snowball stemmers are demonstrated.
- **Lemmatization:** Using linguistic information and lexical resources to
  map a word to its dictionary form, or lemma. Results can depend on the
  word's part of speech and the available language data.
- **Stop words:** Examining common words that are sometimes excluded in
  particular text-analysis tasks. They should not be removed automatically:
  words such as “not” can be essential to meaning.
- **Part-of-speech tagging:** Assigning grammatical labels, such as noun or
  verb, to tokens in context.
- **Named Entity Recognition (NER):** Finding and categorizing names in text,
  such as people, organizations, and locations.

These are useful building blocks, not a complete understanding of language
on their own. The right combination depends on the application, and
preprocessing choices can change or remove meaning.

## Contents

- `NLP.ipynb` — NLTK practice with tokenizers, n-grams, stemming,
  lemmatization, stop words, part-of-speech tagging, and NER. It also contains
  a word-cloud demonstration near the end.
- `01_TOKENIZATION` — focused Python examples and visual notes on tokenizing
  text.
- `02_STEMMING` — focused Python examples and visual notes on stemming.
- `03_LEMMATIZATION` — focused Python examples on lemmatization.

## Suggested study order

1. Learn the concepts in `NLP.ipynb`, starting with tokenization and n-grams.
2. Compare stemming and lemmatization using their dedicated folders.
3. Return to the notebook for stop words, part-of-speech tagging, and NER.
4. Consider how each step affects meaning before using it in a real task.

## Running the examples

The Python examples use **NLTK (Natural Language Toolkit)**. Install NLTK in
your Python environment and download the data resources required by the
specific tokenizer, corpus, tagger, or lemmatizer being used. The notebook's
word-cloud section also uses `wordcloud` and `matplotlib`. Open the notebook
in Jupyter Notebook, JupyterLab, or VS Code and run cells in order.
