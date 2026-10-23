# Stemming

Stemming is a text-normalization technique that reduces related word forms to
a common **stem**, usually by applying rules that remove or change word
endings. For example, forms such as *playing* and *played* may be reduced to a
shared stem. The resulting stem is not guaranteed to be a valid dictionary
word, and stemming does not generally understand a word's meaning or context.

## Stemmers in the examples

The scripts demonstrate NLTK's **Porter**, **Lancaster**, and **Snowball**
English stemmers. Different algorithms can produce different stems; choosing
one depends on the language and the needs of the application.

Stemming is often used to group related word forms for search or text
analysis. It can also over-reduce words, so inspect the results and avoid it
when preserving exact wording is important. The examples also remove English
stop words before stemming; stop-word removal is task-dependent and can remove
meaningful words, such as negations.

## Files

- `stem.py` — applies a Porter stemmer to tokenized sentences after filtering
  English stop words.
- `STEMMING.py` — demonstrates stemming on a sample passage and compares
  Porter, Lancaster, and Snowball stemmers.
- `1.PNG` and `2.PNG` — supporting visual course notes.

## Running the examples

The scripts use **NLTK (Natural Language Toolkit)**. Install NLTK and download
the `punkt` tokenizer data and English stop-word corpus required by your NLTK
version before running them.
