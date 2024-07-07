# This script demonstrates where BOW approach fails
# BOW fails when the word orders are different.

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Define the sentences
sentence1 = "The sun rises in the east and sets in the west."
sentence2 = "The west is where the sun sets, and the east is where it rises."

# Convert the sentences to TF-IDF vectors
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([sentence1, sentence2])

vec1 = vectors[0].toarray()
vec2 = vectors[1].toarray()

# Calculate the cosine similarity between the two vectors
[[cosine_similarity]] = np.dot(vec1, vec2.T) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

print('sentence1:', sentence1)
print('sentence2:', sentence2)

if cosine_similarity > 0.7:
    print("The sentences are similar.")
else:
    print("The sentences are not similar.")

print('Expected: similar.')