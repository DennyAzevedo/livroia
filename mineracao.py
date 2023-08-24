import nltk
from base import base
#nltk.download('popular')

stopwords = nltk.corpus.stopwords.words('portuguese')

def removeStopwords(texto):
    frases = []
    for (palavras, emocao) in texto:
        removesw = [p for p in palavras.split() if p not in stopwords]
        frases.append((removesw, emocao))
    return frases


