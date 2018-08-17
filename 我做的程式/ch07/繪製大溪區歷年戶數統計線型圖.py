# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 12:49:01 2018

@author: Toby
"""

import requests,re
pat=re.compile('[0-9]+')
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
url="http://www.daxi-hro.tycg.gov.tw/home.jsp?id=25&parentpath=0,21,22"
html=requests.get(url)
sp=BeautifulSoup(html.text,"html.parser")
listyear=[]
listpeople=[]
allyear=sp.find_all("td",{"valign":"middle"})
for people in allyear:
    if(allyear.index(people)%2==0):
        m=pat.match(people.text).group()
        listyear.append(int(m))
    else:
        if(people.text=="─"):
            listyear.pop(0)
        if(people.text!="─"):
            listpeople.append(int(people.text))
plt.plot(listyear,listpeople)

plt.xlabel("年度")
plt.ylabel("戶籍")
plt.legend()
plt.title("桃園市大溪區歷年戶數")
plt.yticks(range(18000,34001,2000))