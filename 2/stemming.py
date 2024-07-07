from nltk.stem.porter import PorterStemmer

stemmmer = PorterStemmer()

words = ["table", "probably", "wolves", "playing", "is", "dog", "the", "beaches", "grounded", "dreamt", "envision"]

for word in words:
    print("{:<10} : {}".format(word, stemmmer.stem(word)))
