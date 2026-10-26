# Regular Expressions for Text Processing

## What is a regular expression?
A regular expression (regex) describes a pattern used to find, match, or replace text.

### Useful patterns
```python
import re

text = "Contact me at learner@example.com or visit https://example.com"
print(re.findall(r"[\\w.+-]+@[\\w.-]+\\.[A-Za-z]{2,}", text))
print(re.findall(r"https?://\\S+", text))
```

### Remove digits
```python
text = "NLP 101 is useful"
print(re.sub(r"\\d+", "", text))
```

### Keep letters and spaces (English-oriented example)
```python
text = "Hello, NLP! Version 2."
cleaned = re.sub(r"[^A-Za-z\\s]", "", text)
print(" ".join(cleaned.split()))
```
This example removes accented letters and many non-English characters, so it is not suitable for all languages.

### Common regex symbols
- `\\d`: digit
- `\\w`: word character (Unicode behavior depends on the pattern and flags)
- `\\s`: whitespace
- `+`: one or more
- `*`: zero or more
- `^`: start of string or negation inside a character class
- `$`: end of string
- `[]`: character class

### Practice
Write patterns to find numbers, remove repeated spaces, and identify email-like strings. Explain why regex email validation is only approximate.
