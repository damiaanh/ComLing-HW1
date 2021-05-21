from corpusreader import CorpusReader
from model import BigramModel
import sys
import os
import random
import operator

def generate(model, n):
    generated = 0
    randomwords = list(model.bigrams.keys())
    word = get_random_word(randomwords)
    word.capitalize()
    needs_capital = False
    text = [word]
    while generated < n:
        successors = model.successors(word)
        newwords = sorted(successors, key=lambda successor : successor[1], reverse=True)
        if not newwords:
            word = get_random_word(randomwords)
        else:
            choice = []
            for word in newwords[:3]:
                choice.append(word[0])
            newword = get_random_word(choice)
        if newword != "</s>":
            if needs_capital == True:
                newword.capitalize()
            text.append(" " + newword)
            needs_capital = False
            word = newword
        else:
            text.append(".")
            needs_capital = True
            word = get_random_word(randomwords)
            generated += 1
    paragraphs = "".join(text)
    return paragraphs

def get_random_word(words):
    word = random.choice(words)
    if " " in word:
        word = word.split()[0]
    return word
    
if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = os.path.join(os.getcwd(), "train") # Define standard path if no path is given.

if __name__ == '__main__':
    corpus = CorpusReader(path)
    sents = corpus.sents()
    mymodel = BigramModel(corpus.sents())
    n = 50
    text = generate(mymodel, n)
    input("newtext is ")
    print(text)
    # mymodel.perplexity()