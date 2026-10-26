# Lemmatization

## What is lemmatization?
Lemmatization maps a word to its lemma, a dictionary base form. Results can depend on part of speech and the language model or lexical resource.

### WordNet lemmatizer (NLTK)
```python
import nltk
# nltk.download("wordnet")
# nltk.download("omw-1.4")
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("cars"))       # car
print(lemmatizer.lemmatize("running"))    # often running with default noun POS
print(lemmatizer.lemmatize("running", pos="v"))  # run
print(lemmatizer.lemmatize("better", pos="a"))   # good
```

### spaCy lemmatization
```python
import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("The children were running and ate apples.")
print([(token.text, token.lemma_) for token in doc])
```

### Key difference
Lemmatization is usually more linguistically informed than stemming, but it may need POS tagging and can be slower.

### Practice
Compare stemming and lemmatization on the same list of words. Explain why POS information can change a lemma.
