# Handling Numbers and Punctuation

## Should numbers and punctuation be removed?
Only if they are irrelevant to the task.

### Remove punctuation
```python
import string
text = "Wow! This costs $25.50."
table = str.maketrans("", "", string.punctuation)
print(text.translate(table))
```

### Replace numbers with a placeholder
```python
import re
text = "I bought 3 books for 120 rupees."
print(re.sub(r"\\d+(?:\\.\\d+)?", "<NUM>", text))
```

### Why numbers may matter
- Product reviews: star ratings and prices
- Medical text: measurements and dosages
- Dates and times: event extraction
- Financial documents: amounts and percentages

### Why punctuation may matter
Question marks can indicate questions; exclamation marks may carry emphasis; apostrophes can distinguish contractions and possessives.

### Practice
Design two different cleaning rules: one for product reviews and one for extracting prices. Explain the difference.
