# Text Preprocessing Interview Questions

## Fundamentals
1. What is text preprocessing in NLP?
2. Why is preprocessing task-dependent?
3. What is tokenization? Name common types.
4. What are stopwords?
5. What is the difference between stemming and lemmatization?

## Practical questions
6. How would you remove URLs from text with Python?
7. How would you normalize repeated whitespace?
8. Why can removing punctuation be harmful?
9. How should emojis be handled in sentiment analysis?
10. What is the role of regular expressions in text cleaning?

## Pipeline and modeling
11. What is the difference between preprocessing and feature extraction?
12. Are POS tagging and NER text-cleaning techniques?
13. Why should the same preprocessing rules be used consistently at training and inference time?
14. What is data leakage in an NLP workflow?
15. How would you test a preprocessing function?

## Revision points
- Stemming is heuristic; lemmatization aims for a dictionary lemma.
- Tokenization breaks text into units.
- Stopword removal is optional and task-specific.
- POS tagging and NER are linguistic annotation tasks.
- Keep useful signals such as negation, numbers, punctuation, and emojis when the task needs them.
