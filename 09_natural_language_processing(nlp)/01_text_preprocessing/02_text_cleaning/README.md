# Text Cleaning

## What is text cleaning?
Text cleaning removes or transforms unwanted patterns while preserving useful information.

### Lowercasing
```python
text = "Natural LANGUAGE Processing"
print(text.lower())
# natural language processing
```

### Remove HTML tags and decode entities
```python
import re
from html import unescape

text = "<p>Tom &amp; Jerry</p>"
text = unescape(text)
text = re.sub(r"<[^>]+>", " ", text)
print(" ".join(text.split()))
# Tom & Jerry
```
For complex or malformed HTML, use a proper HTML parser rather than relying only on a regular expression.

### Remove URLs
```python
import re

text = "Read https://example.com for details"
text = re.sub(r"https?://\\S+|www\\.\\S+", "", text)
print(" ".join(text.split()))
```

### Remove repeated whitespace
```python
text = "NLP   is\\n\\t useful"
print(" ".join(text.split()))
# NLP is useful
```

### Remove punctuation (only if appropriate)
```python
import string
text = "Hello, NLP!"
table = str.maketrans("", "", string.punctuation)
print(text.translate(table))
# Hello NLP
```

### Common mistakes
- Removing all punctuation when punctuation carries meaning.
- Removing every number even when numbers are important.
- Applying a cleaning rule without checking sample outputs.
- Assuming one regex handles every possible URL or HTML document.

### Practice
Clean a sentence containing a URL, extra spaces, and HTML. Show the original and cleaned versions.
