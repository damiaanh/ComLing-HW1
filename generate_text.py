from corpusreader import CorpusReader
from model import BigramModel
import sys
import os

def generate(model, n):
    pass
    
if len sys.argv > 0:
    path = sys.argv[1]
else:
    path = os.path.join(os.getcwd(), "train") # Define standard path if no path is given.

if __name__ == '__main__':
    corpus = CorpusReader(path)
    sentences = reader.sents()
    mymodel = BigramModel(sentences)
    generate(mymodel, n)
    mymodel.perplexity()