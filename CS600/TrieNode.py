class TrieNode: 
    # Trie node class 
    def __init__(self): 
        self.children = [None]*256
        self.isEndOfWord = False
        self.isStopWord = False
        #for inverted index of the documents
        self.link = {}


