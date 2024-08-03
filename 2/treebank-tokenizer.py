from nltk.tokenize import TreebankWordTokenizer

text = 'If conscience and empathy were impediments to the advancement of self-interest, then we would have evovled to be amoral sociopaths.'

tokenizer = TreebankWordTokenizer()
tokens = tokenizer.tokenize(text)

print(tokens)