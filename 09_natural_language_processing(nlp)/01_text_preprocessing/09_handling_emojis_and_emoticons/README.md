# Handling Emojis and Emoticons

## Why do emojis matter?
Emojis and emoticons can communicate sentiment, tone, and intent. Do not automatically remove them.

### Preserve emojis
```python
text = "This course is great 😊"
print(text)
```

### Remove many emoji characters (approximate range-based example)
```python
import re

text = "Great work 😊🚀!"
emoji_pattern = re.compile(
    "["
    "\\U0001F300-\\U0001FAFF"
    "\\U00002700-\\U000027BF"
    "]+",
    flags=re.UNICODE
)
print(emoji_pattern.sub("", text).strip())
```
Unicode emoji coverage changes and some emoji sequences use joiners or variation selectors; this regex is an approximation, not a complete emoji parser.

### Convert emoji to text
For sentiment analysis, mapping emojis to descriptions can preserve information. Use a maintained emoji library when needed.

### Emoticons
Examples include `:)`, `:(`, and `;)`. Punctuation cleaning may destroy them, so handle them before generic punctuation removal if they matter.

### Practice
Compare a sentiment sentence before and after emoji removal. Explain which version carries more sentiment information.
