# Text Normalization

## What is text normalization?
Normalization makes text more consistent. Choose transformations that suit the language and task.

### Whitespace and case
```python
text = "  HELLO   World  "
normalized = " ".join(text.casefold().split())
print(normalized)
# hello world
```
`casefold()` is a stronger Unicode-aware case normalization than `lower()` for some languages.

### Unicode normalization
```python
import unicodedata

text = "café"
normalized = unicodedata.normalize("NFC", text)
print(normalized)
```

### Contractions
Contractions such as “don't” may be expanded to “do not” when useful, but use a language-aware library or a carefully maintained mapping. Avoid unsafe global replacements.

### Spelling correction
Spelling correction can alter names, slang, dialect, and technical terms. Apply it only when justified and evaluate its effect.

### Practice
Normalize mixed-case text with extra spaces. Research one Unicode example and explain why visually similar text may have different underlying representations.
