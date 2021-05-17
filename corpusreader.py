import os

class CorpusReader:
    """Read the contents of a directory of files, and return the results as
    either a list of lines or a list of words.

    The pathname of the directory to read should be passed when
    creating the class:

    >>> reader = CorpusReader(r"path/to/dir")
    """

    def __init__(self, directory):
        """
        Initialize a CorpusReader object. This function stores the path to 
        the corpus directory.
        """
        self.directory = directory
        if not os.path.isdir(self.directory):
            raise ValueError(f"{self.directory} does not exist or is not a directory.")

    
    def sents(self):
        """return the text of the corpus as a list of tokenized sentences, 
            i.e., the corpus becomes a list of lists of tokens."""
        pass

    

    