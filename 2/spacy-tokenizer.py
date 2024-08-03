from nlpia2.spacy_language_model import load
nlp = load('en_core_web_md')
doc = nlp('The old oak tree stood tall, its branches reaching toward the sky')

for token in doc:
    print(f'{token.text:>10s} {token.pos_:<8s} {token.dep_:<10s} {token.head.text:>10s}')
    
