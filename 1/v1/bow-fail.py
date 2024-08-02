# This script demonstrates where BOW approach fails
# BOW fails when the word orders are different.

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Define the sentences
def calculate_similarity(sent1, sent2):
    # Convert the sentences to TF-IDF vectors
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([sent1, sent2])

    vec1 = vectors[0].toarray()
    vec2 = vectors[1].toarray()

    # Calculate the cosine similarity between the two vectors
    [[cosine_similarity]] = np.dot(vec1, vec2.T) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

    print('sentence1:', sent1)
    print('sentence2:', sent2)

    if cosine_similarity > 0.7:
        return "The sentences are similar."
    else:
        return "The sentences are not similar."

# Test the function
sentence1 = "The sun rises in the east and sets in the west."
sentence2 = "The west is where the sun sets, and the east is where it rises."
print(calculate_similarity(sentence1, sentence2))
print('Expected: similar.')

print()

sentence1 = "The new employee was very happy with his first day at the company."
sentence2 = "The new employee was very unhappy with his first day at the company."
print(calculate_similarity(sentence1, sentence2))
print('Expected: not similar.')