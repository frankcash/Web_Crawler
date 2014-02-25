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
    for link in soup.find_all('a'):
        print(link.get('href'))
runSoup(urlInput)
