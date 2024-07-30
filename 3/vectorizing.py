kite_text = """
A kite is traditionally a tethered heavier-than-air craft with wing surfaces that react against the air to create lift and drag. A kite consists of wings, tethers, and anchors. Kites often have a bridle to guide the face of the kite at the correct angle so the wind can lift it. A kite’s wing also may be so designed so a bridle is not needed; when kiting a sailplane for launch, the tether meets the wing at a single point. A kite may have fixed or moving anchors. Untraditionally in technical kiting, a kite consists of tether-set-coupled wing sets; even in technical kiting, though, a wing in the system is still often called the kite. The lift that sustains the kite in flight is generated when air flows around the kite’s surface, producing low pressure above and high pressure below the wings. The interaction with the wind also generates horizontal drag along the direction of the wind. The resultant force vector from the lift and drag force components is opposed by the tension of one or more of the lines or tethers to which the kite is attached. The anchor point of the kite line may be static or moving (such as the towing of a kite by a running person, boat, free-falling anchors as in paragliders and fugitive parakites or vehicle). The same principles of fluid flow apply in liquids and kites are also used under water. A hybrid tethered craft comprising both a lighter-than-air balloon as well as a kite lifting surface is called a kytoon.
Kites have a long and varied history and many different types are flown individually and at festivals worldwide. Kites may be flown for recreation, art or other practical uses. Sport kites can be flown in aerial ballet, sometimes as part of a competition. Power kites are multi-line steerable kites designed to generate large forces which can be used to power activities such as kite surfing, kite landboarding, kite fishing, kite buggying and a new trend snow kiting. Even Man-lifting kites have been made.
"""
from collections import Counter
from nltk.tokenize import TreebankWordTokenizer
from pprint import pprint

tokenizer = TreebankWordTokenizer()
tokens = tokenizer.tokenize(kite_text.lower())

document_vector = []
doc_length = len(tokens)

kite_counts = Counter(tokens)

for key, value in kite_counts.most_common():
    document_vector.append(value / doc_length)
    
print('Document vector by most common words:')
pprint(document_vector[:5])

# Building Lexicon
docs = ["The faster Harry got to the store, the faster and faster Harry ➥ would get home."]
docs.append("Harry is hairy and faster than Jill.")
docs.append("Jill is not as hairy as Harry.")

doc_tokens = []
for doc in docs:
    doc_tokens += [sorted(tokenizer.tokenize(doc.lower()))]
    
all_doc_tokens = sum(doc_tokens, [])
lexicon = sorted(set(all_doc_tokens))
print('Lexicon:')
pprint(lexicon)

# Building the Document-Term Matrix
from collections import OrderedDict
zero_vector = OrderedDict((token, 0) for token in lexicon)

import copy
doc_term_matrix = []
for doc in docs:
    vec = copy.copy(zero_vector)
    tokens = tokenizer.tokenize(doc.lower())
    token_counts = Counter(tokens)
    for key, value in token_counts.items():
        vec[key] = value / len(lexicon)
    doc_term_matrix.append(vec)
    
print('Document-Term Matrix:')
pprint(doc_term_matrix)