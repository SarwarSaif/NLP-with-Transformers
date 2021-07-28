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

### Long Text Classification 
"Texts which have a length more than the model token size."
Most of the cases sentences are much longer than 512 tokens and the actual sentiment from the sentence may not be clear from the first 512 tokens. So we really want to consider the full sentence.

We can basically take two approaches to overcome this problem:

1. By summarizing the whole sentence into 512 tokens and then using sentiment classification.
2. Or by using a window and then calculating the sentiment for each window in a sentence.

[google-colab]: https://img.shields.io/badge/notebook-colab%20notebook-orange 
[python]: https://img.shields.io/badge/python-3.7-blue
[huggingface]: https://img.shields.io/badge/Hugging%20Face-%20-red
[flair]: https://img.shields.io/badge/flair----yellow
