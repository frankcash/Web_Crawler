# Goes to a web site, grabs all the links.  Loops them into a hashmap while printing them individually.

from bs4 import BeautifulSoup
import urllib
import urllib2
import re
import requests

urlInput=raw_input("enter the page\n")

def runSoup(urlInput):
    url="http://www."+ urlInput
    content=urllib2.urlopen(url).read()
    soup=BeautifulSoup(content)
    print ("The title of this page is " + soup.title.string+"\n")
    links={}
    i=0
    for link in soup.find_all('a'):
        links[i]=link.get('href')
        i+=1
    return links
links = runSoup(urlInput)
print links
