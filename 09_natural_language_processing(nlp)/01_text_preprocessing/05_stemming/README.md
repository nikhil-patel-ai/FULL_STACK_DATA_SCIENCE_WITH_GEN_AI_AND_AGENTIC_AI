# Stemming

## What is stemming?
Stemming applies heuristic rules to reduce related word forms to a stem. The output is not guaranteed to be a valid dictionary word.

### NLTK Porter Stemmer
```python
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
words = ["connect", "connected", "connecting", "connection"]
for word in words:
    print(word, "->", stemmer.stem(word))
```

### Snowball Stemmer
```python
from nltk.stem import SnowballStemmer

stemmer = SnowballStemmer("english")
print(stemmer.stem("studies"))
```

### Stemming vs. lemmatization
- Stemming: rule-based trimming; can produce non-words.
- Lemmatization: uses vocabulary and linguistic information to produce a lemma.

### Limitations
Stemming can over-stem or under-stem words and does not understand sentence context.

### Practice
Stem `playing`, `played`, `plays`, `studies`, and `studying`. Record whether each output is a dictionary word.
