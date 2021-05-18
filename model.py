import string

class BigramModel:

    def __init__(self, tokens):
        self.tokens = tokens
        self.freqtable = {}
        self.cleanlist = self.clean_tokens()

    def clean_tokens(self):
        startmark = "<s>"
        endmark = "</s>"
        cleanlist = []
        for sentence in tokens:
            cleanlist.append(startmark)
            for token in sentence:
                token.strip(string.punctuation)
                token.lower()
                if token is not "":     # Only continue for tokens that are not empty (due to remove of punctuation)
                    if token in self.freqtable:  # Count frequencies while looping over the text
                        self.freqtable[token] += 1
                    else:
                        self.freqtable[token] = 1
                    cleanlist.append(token)
            cleanlist.append(endmark)
        return cleanlist

    def p_raw(self, w, w_n):
        pass

    def p_smooth(self,w, w_n):
        pass

    def successors(self, w):
        pass
    
    def perplexity(self, sent):
        pass


