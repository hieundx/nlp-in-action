import numpy as np

def build_vocabulary(token_sequence):
    vocab = sorted(set(token_sequence))
    return vocab

def create_onehot_vectors(token_sequence, vocab):
    num_tokens = len(token_sequence)
    vocab_size = len(vocab)

    onehot_vectors = np.zeros((num_tokens, vocab_size), int)

    for i, word in enumerate(token_sequence):
        onehot_vectors[i, vocab.index(word)] = 1

    return onehot_vectors

# Example usage
sentence = "26. Jefferson Monticello Thomas age at began building of the"
token_sequence = sentence.split()
vocab = build_vocabulary(token_sequence)
print(", ".join(vocab))

num_tokens = len(token_sequence)
vocab_size = len(vocab)

onehot_vectors = create_onehot_vectors(token_sequence, vocab)
print(onehot_vectors)