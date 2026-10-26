# 01 — Text Preprocessing

A structured, beginner-friendly module for learning text preprocessing in Natural Language Processing (NLP).

## Learning objectives
- Understand why raw text needs preprocessing.
- Clean and normalize text without losing task-relevant meaning.
- Apply tokenization, stopword removal, stemming, and lemmatization.
- Use regular expressions for common cleaning tasks.
- Understand when to preserve punctuation, numbers, emojis, and negation.
- Build and evaluate a reusable preprocessing pipeline.

## Learning path
1. [Introduction to Text Preprocessing](01_Introduction_to_Text_Preprocessing/README.md)
2. [Text Cleaning](02_Text_Cleaning/README.md)
3. [Tokenization](03_Tokenization/README.md)
4. [Stopword Removal](04_Stopword_Removal/README.md)
5. [Stemming](05_Stemming/README.md)
6. [Lemmatization](06_Lemmatization/README.md)
7. [Normalization](07_Normalization/README.md)
8. [Regular Expressions](08_Regular_Expressions/README.md)
9. [Handling Emojis and Emoticons](09_Handling_Emojis_and_Emoticons/README.md)
10. [Handling Numbers and Punctuation](10_Handling_Numbers_and_Punctuation/README.md)
11. [POS Tagging and Named Entity Recognition](11_POS_Tagging_and_NER/README.md)
12. [Text Preprocessing Pipeline](12_Text_Preprocessing_Pipeline/README.md)
13. [Real-World Mini Project](13_Real_World_Project/README.md)
14. [Practice Exercises](14_Practice_Exercises/README.md)
15. [Interview Questions](15_Interview_Questions/README.md)

## Setup
Create and activate a virtual environment if desired, then install dependencies:

```bash
python -m pip install -r requirements.txt
```

Some examples use only Python's standard library. NLTK and spaCy examples may require model or corpus downloads, which are documented in the relevant topic README.

## Important principle
Preprocessing is task-dependent. Do not automatically remove stopwords, punctuation, numbers, or emojis from every dataset. For example, removing **not** can reverse sentiment, and punctuation may matter for question detection or language modeling.

## Suggested workflow
Raw text → inspect data → clean only necessary noise → normalize → tokenize → optional linguistic processing → validate output → model-specific representation.

## Folder convention
Each topic folder contains one `README.md` with concepts, examples, common mistakes, and practice tasks. Keep notebooks or scripts alongside the README only when you add them later.

## Core libraries
- Python standard library (`re`, `html`, `unicodedata`, `string`)
- NLTK
- spaCy
- scikit-learn (for later text representation tasks)

## References
- [NLTK documentation](https://www.nltk.org/)
- [spaCy documentation](https://spacy.io/usage)
- [scikit-learn text feature extraction](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction)
