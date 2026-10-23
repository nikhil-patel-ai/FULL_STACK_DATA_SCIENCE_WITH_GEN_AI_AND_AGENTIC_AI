# Introduction to Natural Language Processing

## What is NLP?

Natural Language Processing (NLP) is a field of artificial intelligence that
enables computers to work with human language. NLP methods can analyze,
understand, and generate text or speech so that software can perform useful
language-related tasks.

Human language is challenging for computers because the same word or sentence
can mean different things depending on context, word order, tone, spelling,
and the speaker's intent. NLP combines techniques from computer science,
linguistics, and machine learning to address these challenges.

## Main components

- **Natural Language Understanding (NLU):** Analyzes input language to identify
  its structure, meaning, intent, or important information. Examples include
  sentiment analysis, information extraction, and named entity recognition.
- **Natural Language Generation (NLG):** Produces natural-language output,
  such as a chatbot reply, a summary, or generated text.

Many language applications use both components: an assistant interprets a
user's request with NLU and formulates its response with NLG.

## Common applications

NLP is used in:

- Spell checking and grammar assistance
- Search engines and keyword search
- Information extraction, such as finding people, organizations, dates, and
  locations in text
- Sentiment analysis of reviews and social media
- Chatbots and virtual assistants
- Speech recognition and voice interfaces
- Machine translation
- Advertisement matching and social media monitoring
- Text summarization and response generation

## A basic text-processing workflow

An NLP workflow depends on the task, but a common starting point is:

1. **Collect text** from a document, message, review, or other source.
2. **Prepare the text** by applying task-appropriate cleanup and normalization.
3. **Tokenize** the text into sentences, words, or other units called tokens.
4. **Represent and analyze** the tokens using linguistic rules, statistical
   methods, or machine-learning models.
5. **Produce or evaluate an output**, such as a label, extracted information,
   translation, or generated response.

Preprocessing is not one-size-fits-all: removing punctuation, stop words, or
other text can discard information that a particular task needs.

## Concepts introduced in these notes

### Tokenization

Tokenization splits text into manageable units. For example, a sentence can
be divided into words; a tokenizer can also split a passage into sentences.
The resulting tokens are the input to many later NLP steps.

### N-grams

An *n*-gram is a sequence of *n* consecutive tokens. A **bigram** contains two
tokens, a **trigram** contains three, and the general term **n-gram** covers
sequences of other lengths. N-grams preserve some local word order and can be
used as text features.

### Stemming and lemmatization

Both methods reduce related word forms, but they do so differently:

- **Stemming** applies a rule-based reduction to produce a stem, which may not
  be a valid dictionary word.
- **Lemmatization** uses linguistic information to map a word to its
  dictionary form, called a lemma. For example, *going* and *went* can map to
  *go* when the correct context and resources are available.

### Named Entity Recognition

Named Entity Recognition (NER) identifies and classifies names in text, such
as people, organizations, and locations. For example, in “Google's CEO Sundar
Pichai introduced the new Pixel at Minnesota,” an NER system can identify
“Google” as an organization, “Sundar Pichai” as a person, and “Minnesota” as
a location.

## Python and NLTK

The course notes introduce **NLTK (Natural Language Toolkit)**, a Python
library for working with human-language data. NLTK provides tools and
language datasets used by examples such as tokenization, stemming, and
lemmatization. Install the package and download any data resources required by
the specific example before running it.

## Study the accompanying notes

This folder contains numbered image-based lesson notes. Review the images in
sequence; the visible notes include the definition and applications of NLP,
its NLU/NLG components, NLTK, tokenization, n-grams, stemming, lemmatization,
and NER. They are visual course notes rather than runnable code.

For hands-on language-understanding examples, continue to
[`02_NLU`](../02_NLU). For language generation, see
[`03_NLG`](../03_NLG).
