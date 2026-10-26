# Introduction to Text Preprocessing

## What is text preprocessing?
Text preprocessing is the process of inspecting and transforming raw text into a form suitable for a specific NLP task.

### Why is it useful?
Raw text may contain inconsistent capitalization, HTML tags, repeated spaces, URLs, spelling variations, punctuation, and other noise. Preprocessing can improve consistency and make downstream analysis easier.

### Example
```python
text = "  NLP IS FUN!!!   "
clean_text = " ".join(text.lower().split())
print(clean_text)
# nlp is fun!!!
```

### Typical workflow
1. Inspect examples and understand the task.
2. Clean known noise.
3. Normalize text where appropriate.
4. Tokenize text.
5. Optionally remove stopwords or apply stemming/lemmatization.
6. Validate that meaning has not been unintentionally changed.

### Important
There is no universal preprocessing pipeline. A sentiment classifier may need punctuation, emojis, and negation. A search engine may normalize words differently from a language model.

### Practice
1. Explain text preprocessing in your own words.
2. List three types of noise in raw text.
3. Why should preprocessing be chosen according to the task?
