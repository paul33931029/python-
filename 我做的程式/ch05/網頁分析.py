# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 22:24:26 2018

@author: Toby
"""

import requests
from bs4 import BeautifulSoup
url='http://www.e-happy.com.tw/'
html=requests.get(url)
html.encoding="urf-8"
sp=BeautifulSoup(html.text,'html.parser')
a=sp.find_all("a")
for row in a:
    href=row.get("href")
    if("http://"in href):
        print(row.get("href"))

