# Mini Project: Review Text Cleaning

## Project goal
Build a small preprocessing workflow for a collection of product or movie reviews.

### Sample data
```python
reviews = [
    "I LOVE this product!!! 😊",
    "Not good... broke after 2 days.",
    "Fast delivery & great quality: 5/5",
    "Visit https://example.com for support"
]
```

### Tasks
1. Inspect raw reviews.
2. Decide which information to preserve (negation, emoji, rating, numbers, punctuation).
3. Create a cleaning function.
4. Tokenize the reviews.
5. Compare outputs from at least two preprocessing choices.
6. Write a short note describing trade-offs.

### Suggested output table
| Original text | Processed text | Reason |
|---|---|---|
| Keep the original review | Your transformation | Why the rule helps |

### Evaluation checklist
- No accidental deletion of `not` or `never`.
- Empty or whitespace-only strings are handled.
- URLs and HTML are handled according to the project requirements.
- Rules are applied consistently.
- Output has been manually inspected.

### Extension
Compare a simple keyword-based baseline with a scikit-learn text classifier in a later text-representation module. Do not evaluate on the same data used for training.
