# Reusable Text Preprocessing Pipeline

## Why create a pipeline?
A reusable pipeline keeps preprocessing consistent across training and evaluation data. Every step should be selected for the task.

### A conservative baseline pipeline
```python
import re
import html

def clean_text(text: str) -> str:
    text = html.unescape(text)
    text = re.sub(r"<[^>]+>", " ", text)          # simple HTML-like tags
    text = re.sub(r"https?://\\S+|www\\.\\S+", " ", text)
    text = text.casefold()
    text = re.sub(r"\\s+", " ", text).strip()
    return text

sample = "<p>NLP is GREAT!</p> Visit https://example.com"
print(clean_text(sample))
```

### Pipeline design checklist
1. Define the task and target language.
2. Inspect representative examples.
3. Write small, testable functions.
4. Preserve negation and task-relevant symbols.
5. Test edge cases and empty strings.
6. Apply the same transformation consistently.
7. Avoid data leakage: learn any data-dependent transformations using training data only.

### Example tests
```python
assert clean_text("  HELLO   ") == "hello"
assert clean_text("") == ""
```

### Practice
Extend the function with a configurable option to preserve or remove punctuation. Add tests for URLs, empty strings, and repeated spaces.
