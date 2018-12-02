from Trie import Trie
from StopWord import StopWord
from Scraping import Scraping
class Document():
    T = Trie()
    words = []
    doc = ""
    docData = {}
    @staticmethod
    def initializeData(TrieObject):
        T = TrieObject

        #Loading the data from local host and sending it to Scraping for extracting data
        #And then calling the initialize function
        Document.doc = "http://127.0.0.1//CS600/html_intro.html"
        Document.words = Scraping.getDataFromWebPage(Document.doc)
        Document.initialize()
        Document.docData[Document.doc] = Scraping.DocumentData()

        Document.doc = "http://127.0.0.1//CS600/html_editors.html"
        Document.words = Scraping.getDataFromWebPage(Document.doc)
        Document.initialize()
        Document.docData[Document.doc] = Scraping.DocumentData()

        Document.doc = "http://127.0.0.1//CS600/html_basic.html"
        Document.words = Scraping.getDataFromWebPage(Document.doc)
        Document.initialize()
        Document.docData[Document.doc] = Scraping.DocumentData()

        Document.doc = "http://127.0.0.1//CS600/html_elements.html"
        Document.words = Scraping.getDataFromWebPage(Document.doc)
        Document.initialize()
        Document.docData[Document.doc] = Scraping.DocumentData()

        Document.doc = "http://127.0.0.1//CS600/html_attributes.html"
        Document.words = Scraping.getDataFromWebPage(Document.doc)
        Document.initialize()
        Document.docData[Document.doc] = Scraping.DocumentData()

        Document.doc = "http://127.0.0.1//CS600/html_headings.html"
        Document.words = Scraping.getDataFromWebPage(Document.doc)
        Document.initialize()
        Document.docData[Document.doc] = Scraping.DocumentData()

        Document.doc = "http://127.0.0.1//CS600/html_paragraphs.html"
        Document.words = Scraping.getDataFromWebPage(Document.doc)
        Document.initialize()
        Document.docData[Document.doc] = Scraping.DocumentData()

        Document.doc = "http://127.0.0.1//CS600/html_styles.html"
        Document.words = Scraping.getDataFromWebPage(Document.doc)
        Document.initialize()
        Document.docData[Document.doc] = Scraping.DocumentData()

        Document.doc = "http://127.0.0.1//CS600/html_formatting.html"
        Document.words = Scraping.getDataFromWebPage(Document.doc)
        Document.initialize()
        Document.docData[Document.doc] = Scraping.DocumentData()

        Document.doc = "http://127.0.0.1//CS600/html_quotation_elements.html"
        Document.words = Scraping.getDataFromWebPage(Document.doc)
        Document.initialize()
        Document.docData[Document.doc] = Scraping.DocumentData()

        return Document.T
    
    #inserting all the scraped data to the Trie object and its method
    @staticmethod
    def initialize():
        for key in range(0,len(Document.words)): 
            k = StopWord.T.search(Document.words[key])[0]
            if not k:
                Document.T.insert(Document.words[key].lower(),Document.doc,key,False) 
                
        
    #returning the key of the word using trie.search
    @staticmethod
    def Search(key):
        return Document.T.search(key)[1]
        

