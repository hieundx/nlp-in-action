from nltk.tokenize.casual import casual_tokenize

texts = [
    'OMG guys! 😱💖 Just had the BEST day ever at the beach! 🏖️☀️',
    'Caught some killer waves 🏄‍♀️🌊 and got my tan on 😎✨',
    'Feeling so blessed and grateful rn 🙏🥰',
    '#BeachVibes #SummerLovin #LivingMyBestLife'
]

for text in texts:
    tokens = casual_tokenize(text)
    print(text)
    print(tokens)
    print()