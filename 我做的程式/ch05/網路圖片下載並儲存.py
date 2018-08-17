# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 14:39:56 2018

@author: Toby
"""

def open_the_file(x):
    try:
        url=x
        f=open(r"C:\Users\Toby\Desktop\paul\我做的程式\ch05\image","w",encoding="utf-8")
        f.write(url)
        f.close()
    except:
        print("無法讀取")
import requests,os,re,ast
url="http://www.tooopen.com/img/87.aspx"
html=requests.get(url)
html.encoding="urf-8"
from bs4 import BeautifulSoup
sp=BeautifulSoup(html.text,"html.parser")
data1=sp.find("div",{"class":"c-fix wrap-list list-com"})
data2=data1.find("ul")    #找到ul
data3=data2.find_all("img")
for list1 in data3:
    find_picture=list1.get("src")
    print(find_picture)                       #找出顯現的圖片
data4=data1.find("div",{"style":"display:none"})
change=ast.literal_eval(data4.text)
print()
for dict1 in change:
    print(dict1["imgthumb"])
    open_the_file(dict1["imgthumb"])
data5=sp.find_all("img")
for op in data5:
    o=op.get("src")
    if(".png"in str(o) and "http://" in str(o)):
        print(o)
        open_the_file(o)
    
        

        
    
    

