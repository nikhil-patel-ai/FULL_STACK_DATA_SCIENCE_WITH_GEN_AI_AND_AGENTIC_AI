# Tokenization

Tokenization is the process of splitting text into smaller units called
**tokens**. Depending on the task, tokens may be sentences, words, punctuation
marks, or other text pieces. It is usually an early step in NLP because later
operations need a structured representation of the text.

## Why tokenization matters

Consider the sentence “NLP helps computers process language.” A word tokenizer
might produce separate tokens for each word and the final punctuation. A
sentence tokenizer can instead identify sentence boundaries in a longer
passage. The exact output depends on the tokenizer: punctuation, abbreviations,
contractions, and language can make boundaries ambiguous.

Tokens can also be grouped into **n-grams** for analysis: a unigram is one
token, a bigram is a pair of consecutive tokens, and a trigram is a sequence
of three. The NLU notebook demonstrates n-grams after tokenization.

## Files

- `Token.py` — tokenizes a sample paragraph into sentences and words with
  NLTK.
- `5.TOKENIZATION.py` — demonstrates sentence and word tokenization on a
  longer sample passage.
- `1.jpg` through `4.jpg` — supporting visual course notes.

## Running the examples

The Python examples use **NLTK (Natural Language Toolkit)**. Install NLTK in
your Python environment and download the tokenizer data resources required by
your NLTK version. Run either script with Python to see its sentence and word
tokens.
