# -*- coding: cp950 -*-
# Refers from : https://read01.com/2xOGP.html

import urllib2
from bs4 import BeautifulSoup
import pandas as pd

wiki = 'https://zh.wikipedia.org/wiki/%E6%B2%83%E5%BE%B7%C2%B7%E5%9D%8E%E5%AE%81%E5%AE%89'

page = urllib2.urlopen(wiki)

soup = BeautifulSoup(page,"lxml")

table = soup.find('table',class_='nowraplinks hlist collapsible autocollapse navbox-inner')

a=[] #領域
b=[] #概念
c=[] #導向
d=[] #模型
e=[] #軟體工程師
f=[] #相關領域


for row in table.findAll("tr"):
  cells = row.findAll('td')
  #states = row.findAll('th')
  #print len(cells)
  if len(cells) >= 1:
    #a.append(cells[0].find(text=True))
    #b.append(states[0].find(text=True))
    #c.append(cells[1].find(text=True))
    #d.append(cells[2].find(text=True))
    #e.append(cells[3].find(text=True))
    #f.append(cells[4].find(text=True))

#print a
