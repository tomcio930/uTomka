'''
Created on 06-03-2013

@author: Tomasz Gorny
'''
from BeautifulSoup import BeautifulSoup as BS
from uuid import uuid4
import urllib2
import re

class WebSite():
    def __init__(self, adress):
        self.adress = adress
        
    def __getDataFromPage(self, page):    
        print "Reading images from website: "+self.adress+str(page)
        return urllib2.urlopen(self.adress+str(page))
        
    def __downloadImageFromTag(self, imageTag, page):
        src = imageTag["src"]
        ext = src.split(".")[-1][0:3]
        if(not str(src).__contains__("http")):
            src = self.adress+str(page)+src
        f = open("images/"+str(uuid4()).replace('-','')+"."+ext,"wb")
        f.write(urllib2.urlopen(src).read())
        f.close()
        print "  Image: "+src+" is downloaded."
        
    def downloadImages(self, imageSourceRegExp, count=-1):
        """Saves 'count' images with src matching 'imageSourceRegExp' from website."""
        downloadedImages = 0
        condition = True
        page = 1
        while(condition):
            data = self.__getDataFromPage(page)
            if(data.getcode() != 200):
                print "Done. No more pages."
                break
            page += 1
            doc = BS(data)
            images = doc.findAll("img", {"src": imageSourceRegExp})
            if(images.__len__() == 0):
                print "Done. No more images."
                break
            for image in images:
                self.__downloadImageFromTag(image, page)
                downloadedImages+=1
                if(count != -1):
                    condition = downloadedImages < count
                    if(not condition):
                        print "Done. Downloaded: "+str(downloadedImages)+" images."
                        break
                

        
if __name__ == '__main__':
    jzd = WebSite("http://jebzdzidy.pl/strona/")
    jzd.downloadImages(re.compile("img.myepicwall.com"), 10)
    wikary = WebSite("http://wikary.pl/?page=")
    wikary.downloadImages(re.compile("media"), 10)
    
    
    