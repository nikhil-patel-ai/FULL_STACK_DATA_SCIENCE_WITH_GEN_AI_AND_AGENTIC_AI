# POS Tagging and Named Entity Recognition

## How are POS tagging and NER related to preprocessing?
They are linguistic analysis tasks often used in an NLP pipeline. They are not simply text-cleaning operations.

### Part-of-speech (POS) tagging
POS tagging labels words with grammatical categories such as noun, verb, adjective, and adverb.

```python
import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("Mira studies machine learning in Delhi.")
print([(token.text, token.pos_) for token in doc])
```

### Named Entity Recognition (NER)
NER detects entities such as people, organizations, locations, and dates.

```python
for ent in doc.ents:
    print(ent.text, ent.label_)
```

### Why they can help
- POS-aware lemmatization
- Extracting names, locations, dates, and organizations
- Information extraction and search

### Important distinction
Tokenization and normalization are common preprocessing steps. POS tagging and NER add linguistic annotations and are often downstream analysis steps.

### Setup
```bash
python -m pip install spacy
python -m spacy download en_core_web_sm
```

### Practice
Run POS tagging and NER on a sentence containing a person, organization, and location. Note any incorrect predictions.
