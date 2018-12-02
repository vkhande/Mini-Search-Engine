from InitializeEngine import InitializeEngine
from PresentingLayer import PresentingLayer

def main():
    #Initialising the data base with all the stopwords and loading all the documents in Trie
    T = InitializeEngine.Initialize()
    k = True
    while k:
        print("Type exit to exit\n")
        query = input("Enter text to search?     ")
        if(query.lower() == "exit"):
            k = False
        else:
            PresentingLayer.FinalPresentation(query.lower())
    
    
if __name__ == '__main__':
    main()