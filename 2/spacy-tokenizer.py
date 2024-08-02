import spacy
from bpe import texts
from nlpia2.spacy_language_model import load
nlp = load('en_core_web_md')
doc = nlp(texts[0])
print(doc)

tokens = [token.text for token in doc]
print (tokens)