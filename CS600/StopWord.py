from Trie import Trie
class StopWord():
    
    T = Trie()
    
    @staticmethod
    def initialize(Trieobject):
        T = Trieobject
        keys = ["a","about","above","after","again","against","all","am","an","and","any","are","as","at","be","because","been",
                "before","being","below","between","both","but","by","cannot","could","did","do","does","doing","down","during",
                "each","few","for","from","further","had","have","having","he","her","here","hers","herself","him",
                "himself","his","how","i","if","in","into","is","it","its","itself","me","more","most","my","myself",
                "no","nor","not","of","off","on","once","only","or","other","ought","our","ours","ourselves","out","over",
                "own","same","she","should","so","some","such","than","that","the","their","theirs","them","themselves","then","there",
                "these","they","this","those","through","to","too","under","until","up","very","was","we","were","what","when",
                "where","which","where","while","who","whom","why","with","would","you","your","yours","yourself","yourselves",] 
        #Inserting the Stopwords using function in trie.insert
        for key in range(0,len(keys)): 
            StopWord.T.insert(keys[key],"Stopword",key,True) 
        
        #Return the Trie object with stopwords 
        return T
    
    @staticmethod
    def Search(key):

        #Searching the stopwords and returning using Trie.search
        return StopWord.T.search(key)
    
  




