from StopWord import StopWord
from Document import Document
from Trie import Trie

class InitializeEngine():
    
    #load all the stopwords and document data to tries
    @staticmethod
    def Initialize():
        #Creating the trie object and passing to both the functions
        T = Trie()

        #Initialising the stopwords to trie
        T = StopWord.initialize(T)

        #Initialising the data by scraping and then loading it to trie data structure
        T= Document.initializeData(T)
        
        #Fully loaded Trie data structure is returned
        return T


