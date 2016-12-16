# -*- coding: cp950 -*-
import urllib2
import cookielib
import urllib
from bs4 import BeautifulSoup
import json
#Create Cookies
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

#Set Agent
opener.addheaders = [('User-agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36')]

urllib2.install_opener(opener)

authentication_url = "http://web.ccgh/"
payload={'T1':'13432', 'T2':'123qweasd'}
data = urllib.urlencode(payload)

req = urllib2.Request(authentication_url,data)
resp = urllib2.urlopen(req)
contents = resp.read()

#Below B.Soup
soup = BeautifulSoup(contents,"lxml")
script=str(soup.script.contents)
MainPage = script.split('"')[1]

#req = urllib2.Request(MainPage)
#resp = urllib2.urlopen(req)
#contents = resp.read()

opener.addheaders = [('Referer', MainPage)]
response = opener.open("http://web3.ccgh/ccghiso/DocLookList.asp")
contents = response.read()
print MainPage
print contents
print cj







