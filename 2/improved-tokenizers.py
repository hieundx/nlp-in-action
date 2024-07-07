from nltk.tokenize.casual import casual_tokenize

message = "RT @hieundx Python is amazing! #NLTK #NLP :P"

print(casual_tokenize(message))
print(casual_tokenize(message, strip_handles=True))
