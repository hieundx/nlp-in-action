from nltk.tokenize import word_tokenize
from nltk.util import ngrams
# import nltk
# nltk.download('punkt')

sent = "Thomas Jefferson began building Monticello at the age of 26."

tokens = word_tokenize(sent)
bigrams = ngrams(tokens, 2)

print(list(bigrams))