from corpusreader import CorpusReader
from model import BigramModel
import sys

def generate(model, n):
    pass

path = sys.argv[1]

if __name__ == '__main__':
    corpus = CorpusReader(path)
    sentences = reader.sents()
    mymodel = BigramModel(sentences)
    generate(mymodel, n)
    mymodel.perplexity()