import os
import nltk

class CorpusReader:
    """
    Read the contents of a directory of files, and return the results as
    either a list of lines or a list of words. 
    Authors: Damiaan Houtschild
    """

    def __init__(self, directory):
        """ Initialize a CorpusReader object. This function stores the path to 
        the corpus directory. """
        if not os.path.isdir(directory):
            raise ValueError(f"{path} does not exist or is not a directory.")
        self.directory = directory
        
        
    def sents(self):
        """ Return the text of the corpus as a list of tokenized sentences, 
            i.e., the corpus becomes a list of lists of tokens."""
        sentlist = []
        tokenlist = []
        for file in os.listdir(self.directory):
            if not file.endswith(".txt"):   # Skip files that are not txt files
                continue
            with open(os.path.join(self.directory, file), "r") as f:
                raw_text = f.read()
                sentences = nltk.sent_tokenize(raw_text)
                cleansents =[s.replace("\n", " ") for s in sentences]
                sentlist.extend(cleansents)
        for sentence in sentlist:
            tokens = nltk.word_tokenize(sentence)
            tokenlist.append(tokens)
        print(tokenlist)

