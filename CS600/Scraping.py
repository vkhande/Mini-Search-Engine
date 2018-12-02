from bs4 import BeautifulSoup
import requests

class Scraping():
    
    text2 = ""

    #getting data from local host
    @staticmethod
    def getDataFromWebPage(url):
        code = requests.get(url,stream = True)
        with open("temp.html","wb") as html: 
            html.write(code.content)
        
        data = open("temp.html",'r')
        soup = BeautifulSoup(data, 'html.parser')

        #removing all the scripts and styling from the file
        for script in soup(["script", "style"]):
            script.extract()    # rip it out

        # get text
        text = soup.get_text()

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)        
        
        #removing all the non-alphabatic and non-number charecters 
        ''.join(e for e in text if e.isalnum())
        
        #converting from UTF-8 to Ascii
        text1 = str(text.encode('Ascii',errors = 'ignore'))
        text2 = text1.replace('\\n',' ').replace('//',' ')
        
        #converting all the data to a list and returning
        Scraping.words = text2.split()
        
        return Scraping.words

    def DocumentData():

        #Returning total number of words in each doc after scraping
        return len(Scraping.words)