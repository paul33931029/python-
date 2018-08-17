# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 13:20:22 2018

@author: Toby
"""

import re,requests
url='https://auth.cht.com.tw/ldaps/'
html=requests.get(url)
html.encoding="urf-8"
a=str(html.text)
pat=re.compile('[a-z]+@[a-z\.]+')
m=pat.findall(a)
for row in m:
    print(row)

