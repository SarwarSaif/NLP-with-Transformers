![google-colab]
![python]
![huggingface]
![flair]

# Introduction
Sentiment analysis from text is an NLP task where we classify sentiments of sentences as Positives, Negatives or Neutral. The number of categories might differ. 
Example: 
1. Positive: "GBP rallies after stronger than ever economic performance."
2. Negative: "GBP slips on fear of a divided economy."
3. Neutral: "GBP is one of several European currencies."

### The typical flow of a **Sentiment classification model using Transformers** consists of four steps:
1. Raw text is Tokenized. A tokenizer usually converts words into a list of numerical ids. 
2. Token IDs fed into the Model. 
  With Transformer model, the first layer will be Embedding Layer and our token ids will be passed through this layer. And we will get a Set of Word Vectors from the output of Embedding layer. 
  - This is the very first layer of most Transformer Models.
3. The model typically outputs a set of Activations. So we need to feed these Output Activations in our Transformer Heads, and then our Transformer Heads will convert these activations into a Set of Probabilities. And Softmax is applied onto the activations after they are processed by the linear layers, the Sum of the Probabilities will be 1.
4. Argmax is applied at the end to get the Class with Highest Probability.

Note: It can be possible to change the Number of Output Classes to fit our number of desired classes in the head module. 


[google-colab]: https://img.shields.io/badge/notebook-colab%20notebook-orange 
[python]: https://img.shields.io/badge/python-3.7-blue
[huggingface]: https://img.shields.io/badge/Hugging%20Face-%20-red
[flair]: https://img.shields.io/badge/flair----yellow
