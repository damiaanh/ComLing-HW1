from corpusreader import CorpusReader
from model import BigramModel
import sys
import os
import random
import operator

def generate(model, n):
    paragraphs = ""
    randomwords = list(model.bigrams.keys())
    
    for x in range(2):
        word = get_random_word(randomwords)
        capword = word.capitalize()
        needs_capital = False
        text = [capword]
        generated = 0
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
                    new = newword.capitalize()
                    text.append(" " + new)
                else:
                    text.append(" " + newword)
                needs_capital = False
                word = newword
            else:
                text.append(".")
                needs_capital = True
                word = get_random_word(randomwords)
                generated += 1
        paragraph = "".join(text)
        paragraphs += paragraph + "\n\n"
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
    n = 10
    text = generate(mymodel, n)
    print(text)
    # mymodel.perplexity()