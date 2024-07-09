from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sa = SentimentIntensityAnalyzer()

# Generate a corpus of sentences with a wide range of sentiments
corpus = [
    "I am extremely happy about this amazing product!",
    "This product is terrible and I hate it.",
    "The service was terrible and I am very disappointed.",
    "I am delighted with this product.",
    "I am thoroughly dissatisfied with this product.",
]

for sent in corpus:
    scores = sa.polarity_scores(sent)
    print('{:+}: {}'.format(scores['compound'], sent))

print(sa.lexicon)