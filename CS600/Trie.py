from TrieNode import TrieNode
class Trie: 
      
    # Trie data structure
    def __init__(self): 
        self.root = self.getNode() 
  
    def getNode(self): 
        # Returns new trie node 
        return TrieNode() 
  
    #converts char to ascii value
    def _charToIndex(self,ch): 
        return ord(ch) 
    
    #inserting into string
    def insert(self,key,link,index1,stopword = False): 
        curr = self.root 
        for char in key: 
            index = self._charToIndex(char) 
            # if current character is not present 
            if not curr.children[index]: 
                curr.children[index] = self.getNode() 
            curr = curr.children[index] 
        curr.isEndOfWord = True
        curr.isStopWord = stopword
        if link not in curr.link:
            curr.link[link] = [index1]
        else:
            curr.link[link].append(index1)
           
    #Searching the key
    def search(self, key): 
        curr = self.root
        for char in key: 
            index = self._charToIndex(char) 
            if not curr.children[index]:
                return [False,{}]
            curr = curr.children[index] 
           
                
        return [curr.isStopWord,curr.link]


