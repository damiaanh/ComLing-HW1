import string
import nltk
import re

class BigramModel:

    def __init__(self, tokens):
        self.tokens = tokens
        self.wordcount = {}
        self.tokenlist = self.clean_tokens(self.tokens)

        self.words = self.count_word_freqs(self.tokenlist)
        self.totalwords = self.count_total(self.words)

        self.bigrams = self.count_bigram_freqs(self.tokenlist)
        self.totalbigrams = self.count_total(self.bigrams)

    def clean_tokens(self, tokens):
        """
        Prepares the tokens generated by CorpusReader by removing punctuation,
        lower case all and add start and end markings.
        Returns a list of tokenized lists (sentences).
        """
        STARTMARK = "<s>"
        ENDMARK = "</s>"
        cleanlist = []
        for sentence in tokens:
            cleansent = []
            cleansent.append(STARTMARK)
            for token in sentence:
                token.strip(string.punctuation)
                token.lower()
                if token != "":     # Only continue for tokens that are not empty (due to removing punctuation)
                    cleansent.append(token)
            cleansent.append(ENDMARK)
            cleanlist.append(cleansent)
        return cleanlist


    def count_word_freqs(self, sentences):
        """
        Calculates frequencies for all words in all sentences.
        Returns a dictionary with all (unique) words and their frequency.
        """
        wordcount = {}
        for sentence in sentences:
            for word in sentence:
                if word in wordcount:
                    wordcount[word] += 1
                else:
                    wordcount[word] = 1
        return wordcount


    def count_total(self, freqdict):
        """
        Counts the total amount of items in a dataset by adding all frequencies.
        Returns the total as integer.
        """
        total = 0
        for item in freqdict:
            total += freqdict[item]
        return total

    
    def count_bigram_freqs(self, sentences):
        """
        Calculates frequencies for all bigrams in all sentences.
        Returns a dictionary with all (unique) bigrams and their frequency.
        """
        bigramcount = {}
        for sentence in sentences:
            for word in range(len(sentence[:-1])): # Not looping over the last word ("</s>") since there is no second word
                bigram = f"{sentence[word]} {sentence[word+1]}"
                if bigram in bigramcount:
                    bigramcount[bigram] += 1
                else:
                    bigramcount[bigram] = 1
        return bigramcount


    def p_raw(self, w, w_n):
        """
        Takes a word and a successor word and looks if this specific bigram exists.
        If so, it returns the probability for this bigram. Otherwise it returns 0. 
        """
        bigram = f"{w} {w_n}"
        if bigram in self.bigrams:
            p = self.bigrams[bigram] / self.totalbigrams
        else:
            p = 0
        return p
    
    def p_smooth(self,w, w_n):

        bigram = f"{w} {w_n}"
        p_raw = self.p_raw(w, w_n)
        aantalw_en_w_n = x[[w, w_n]] + 1
        aantalw = BigramModel.wordsintext(w) + 1            
        #elke count 1 bij optellen, ook wanneer iets meerdere keren voorkomt
        chance_of_w_n = (aantalw_en_w_n / aantalw) * 100
        return chance_of_w_n

    def successors(self, w):
        wi_ci_list = []
        for successor in self.words:
            p = self.p_raw(w, successor)
            if p != 0:
                wi_ci_list.append([successor, p])
        return wi_ci_list
            
#Return a list of pairs (w_i, c_i) , where w_i is a token that
#might follow w , and c_i is its raw (unsmoothed) bigram
#probability, P_r(w_i | w) . Tokens with zero probability need
#not be included in the result.
        
    
    def perplexity(self, sent):
        #er moet van sent nog tokens gemaakt worden en vervolgens van de tokens
        #sentences zoals in clean_tokens:
        cleansent = self.clean_tokens(sent)
        calc = 0
        for x in cleansent:
            calc *= 1/(self.p_smooth(cleansent[x], cleansent[x + 1]))
        perplexity = pow(calc, (1/self.count_bigrams(sent_sentences)))
        return perplexity
            
        #sent is een voorbeeld bigram
