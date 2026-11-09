# Stopword Removal

## What are stopwords?
Stopwords are frequent words such as “the”, “is”, and “and” that may contribute little to some tasks. Whether to remove them depends on the goal.

### Example with a custom list
```python
text = "this is a useful NLP lesson"
stopwords = {"is", "a"}
tokens = text.split()
filtered = [word for word in tokens if word not in stopwords]
print(filtered)
# ['this', 'useful', 'NLP', 'lesson']
```

### NLTK English stopwords
```python
import nltk
# nltk.download("stopwords")
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))
tokens = ["this", "is", "not", "useful"]
print([w for w in tokens if w not in stop_words])
```

### Preserve negation
In sentiment tasks, words such as `not`, `no`, and `never` can be essential. Review the stopword list before filtering it.

### When removal may be unhelpful
- Sentiment analysis
- Question answering
- Machine translation
- Modern transformer models, which generally expect their own tokenizer input
- Any task where grammar or function words carry useful signals

### Practice
Create a custom stopword set. Compare output before and after filtering, and explain whether the meaning changed.
