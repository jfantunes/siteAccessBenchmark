import os
import validators

class urlReader():
    def __init__(self,fileLocation):
        self.file=fileLocation
        self.urls=[]
    
    def readFile(self):
        list_urls=[]
        try:
            with open(self.file) as f:
                lines= [line.rstrip() for line in f]
                for line in lines:
                    urls=line.split(';')
                    list_urls+=urls
            self.urls=self.url_validation(list_urls)
            return self.urls
        except:
            raise Exception("Error parsing url list")
    
    def url_validation(self,urlist):
        valid_list=[]
        for url in urlist:
            if validators.url(url):
                valid_list.append(url)
        return valid_list
        
        
def get_urls(filename):
    reader=urlReader(filename)
    return reader.readFile()

            
        