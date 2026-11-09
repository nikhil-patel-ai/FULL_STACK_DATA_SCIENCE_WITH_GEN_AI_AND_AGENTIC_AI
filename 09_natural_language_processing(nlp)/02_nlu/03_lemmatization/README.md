# Lemmatization

Lemmatization reduces an inflected word to its dictionary form, called a
**lemma**. Unlike a simple stemmer, a lemmatizer uses linguistic information
and lexical resources to produce a meaningful base form. For example, the
verb forms *goes*, *going*, and *went* can map to *go* when the word is
correctly identified as a verb.

## Lemmatization and context

A word's part of speech matters. NLTK's `WordNetLemmatizer` uses noun as its
default part of speech, so a verb such as *running* may not become *run*
unless it is supplied with the appropriate part-of-speech information.
Lemmatization can also depend on the available WordNet data.

The scripts tokenize sample passages into sentences and words, remove English
stop words, and lemmatize the remaining tokens. Stop-word removal is
task-dependent; a common word such as *not* can be important to a sentence's
meaning.

## Files

- `lemm.py` — lemmatizes a sample passage with NLTK's WordNet lemmatizer.
- `lemmatization.py` — demonstrates the same workflow on another sample
  passage.

## Running the examples

The scripts use **NLTK (Natural Language Toolkit)**. Install NLTK and download
the tokenizer data, English stop-word corpus, and WordNet resources required
by your NLTK version before running them.
