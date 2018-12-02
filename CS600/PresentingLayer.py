from Search import Search
import requests
from bs4 import BeautifulSoup
class PresentingLayer():
    
    #Final presentation layer where the data is arranged on the console based on the ranks
    def FinalPresentation(Query):
        
        D = Search.Search(Query)
        Sort_based_on_ranks = sorted(D, key=D.get, reverse=True)

        for key in Sort_based_on_ranks:
            url = key
            code = requests.get(url,stream = True)
            with open("temp.html","wb") as html: 
                html.write(code.content)
        
            data = open("temp.html",'r')
            soup = BeautifulSoup(data, 'html.parser')
            
            print(soup.h1.get_text()+"\n"+url+"\n\n\n")
           
        if(len(Sort_based_on_ranks)==0):
            print("I'm sorry! The webpages included in the project does not have any related information")
            
