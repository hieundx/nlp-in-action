import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# Download necessary NLTK data
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # Default to noun

def lemmatize_with_pos(text):
    words_and_tags = nltk.pos_tag(nltk.word_tokenize(text))
    return [lemmatizer.lemmatize(word, get_wordnet_pos(tag)) for word, tag in words_and_tags]

def lemmatize_without_pos(text):
    return [lemmatizer.lemmatize(word) for word in nltk.word_tokenize(text)]

# Example sentences
sentences = [
    "The cats are running quickly",
    "He was running and jumping",
    "The leaves are falling from the trees",
    "I am happily singing in the rain"
]

print("Lemmatization comparison:")
print("--------------------------")

for sentence in sentences:
    print(f"\nOriginal: {sentence}")
    print(f"Without POS: {' '.join(lemmatize_without_pos(sentence))}")
    print(f"With POS:    {' '.join(lemmatize_with_pos(sentence))}")

# Example with ambiguous words
ambiguous_sentences = [
    "I can't bear to see the bear suffer",
    "The wind was too strong to wind the sail",
    "The dump was so full that it had to refuse more refuse",
    "We must polish the Polish furniture"
]

print("\n\nLemmatization of ambiguous words:")
print("-----------------------------------")

for sentence in ambiguous_sentences:
    print(f"\nOriginal: {sentence}")
    print(f"Without POS: {' '.join(lemmatize_without_pos(sentence))}")
    print(f"With POS:    {' '.join(lemmatize_with_pos(sentence))}")