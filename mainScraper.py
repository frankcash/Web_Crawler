from bs4 import BeautifulSoup
import urllib
import urllib2
import re
import requests

urlInput=raw_input("enter the page\n")

def runSoup(urlInput):
    url=urlInput
    content=urllib2.urlopen(url).read()
    soup=BeautifulSoup(content)
    print ("The title of this page is "+ soup.title.string+"\n")
    links=[ ]
    for link in soup.find_all('a'):
        print(link.get('href')) # prints all the links in a beautiful way
        links+=[link.get('href')] # adds all the links to an array
runSoup(urlInput)
