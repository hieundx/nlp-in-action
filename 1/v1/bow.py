import numpy as np
A = np.array([2, 1, 0, 1, 0])
B = np.array([1, 2, 0, 0, 1])
cosine_similarity = np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B))
print(cosine_similarity)
0.6666666666666667