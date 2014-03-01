from bs4 import BeautifulSoup
import urllib
import urllib2
import re
import requests

def countUsers():
    i=1
    foo=0
    while(i<2):
        urlOne="http://registration.coded.io/events/1/teams"
        urlGen="http://registration.coded.io"
        #url="http://registration.coded.io/events/1/teams/"+str(i)
        content=urllib2.urlopen(urlOne).read()
        soup=BeautifulSoup(content)
        #temp=soup.find_all('p')
        links={}
        for link in soup.find_all('a'): #grabs all the team ideas and stores in hash map
            links[foo]=link.get('href') #match the href with the actual text using magic
            #print links[foo]
            contentGen=urllib2.urlopen(urlGen+links[foo])
            soupGen=BeautifulSoup(contentGen)
            temp=soupGen.find_all('p')
            print temp
            print links[foo]
            print len(temp)
            foo+=1
        i+=1
        #print temp

countUsers()
