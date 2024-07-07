import nltk
nltk.download('stopwords')

stop_words = nltk.corpus.stopwords.words('english')
print(stop_words)