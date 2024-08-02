import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
texts = [
    "The old oak tree stood tall, its branches reaching toward the sky.",
    "She fumbled with her keys, trying to unlock the door in the dark.",
    "The aroma of freshly baked bread filled the kitchen.",
    "Children's laughter echoed across the playground on a sunny afternoon.",
    "The scientist carefully examined the data, searching for patterns."
]

if __name__ == '__main__':
    vectorizer = CountVectorizer(ngram_range=(1, 2), analyzer='char')
    vectorizer.fit(texts)

    print(list(vectorizer.vocabulary_.items())[:5])

    vectors = vectorizer.transform(texts)
    df = pd.DataFrame(vectors.todense(), columns=vectorizer.vocabulary_)

    df.index = [t[:8] + '...' for t in texts]
    df = df.T
    df['total'] = df.T.sum()

    print(df.sort_values('total').tail())