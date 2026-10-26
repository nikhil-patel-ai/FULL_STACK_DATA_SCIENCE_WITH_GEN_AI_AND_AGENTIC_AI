# Tokenization

## What is tokenization?
Tokenization splits text into units called tokens. Tokens may be words, sentences, subwords, or characters.

### Basic word splitting
```python
text = "NLP makes text useful."
print(text.split())
# ['NLP', 'makes', 'text', 'useful.']
```
`split()` is simple but does not handle punctuation as a linguistic tokenizer would.

### Sentence tokenization with NLTK
```python
import nltk
# Run once if required:
# nltk.download("punkt")
# Some NLTK versions may request punkt_tab as well.
from nltk.tokenize import sent_tokenize

text = "NLP is interesting. Tokenization is a first step."
print(sent_tokenize(text))
```

### Word tokenization with NLTK
```python
from nltk.tokenize import word_tokenize

text = "Don't remove meaning!"
print(word_tokenize(text))
```

### Tokenization with spaCy
```python
import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple hired Mira in London.")
print([token.text for token in doc])
```
Install the package and English model if needed:
```bash
python -m pip install spacy
python -m spacy download en_core_web_sm
```

### Types
- Sentence tokenization: document → sentences
- Word tokenization: sentence → word-like tokens
- Subword tokenization: words → model vocabulary units
- Character tokenization: text → characters

### Practice
Tokenize three sentences using `split()` and a library tokenizer. Compare punctuation handling.
