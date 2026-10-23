# Natural Language Generation (NLG)

## What is NLG?

Natural Language Generation (NLG) is the process of producing human-readable
language from data, instructions, or a model's internal representation. It is
often paired with Natural Language Understanding (NLU): NLU interprets an
input, while NLG creates an appropriate response.

Examples of NLG include:

- Generating a chatbot or virtual-assistant response
- Summarizing a long document
- Turning structured data into a written report
- Producing captions, explanations, or translated text

High-quality generated text should be relevant to its input, coherent, and
appropriate for its intended audience. In practical systems, generation may
be guided by templates, rules, statistical methods, or language models.

## Notebook contents

This folder contains `NLG.ipynb`. The notebook currently includes introductory
NLU exercises as well as a **word-cloud visualization** using `WordCloud` and
`matplotlib`. A word cloud displays words from a supplied text, often with
more frequent words shown more prominently. It is a visualization, not by
itself an example of generating new natural-language sentences.

The notebook does not currently contain a complete text-generation exercise.
The NLG explanation above provides background for the topic; the hands-on
notebook content is what is present in the file.

## Running the notebook

Open `NLG.ipynb` in Jupyter Notebook, JupyterLab, or VS Code and run cells in
order. The word-cloud section requires `wordcloud` and `matplotlib`. Other
notebook cells use NLTK and may need the corresponding NLTK data resources.
