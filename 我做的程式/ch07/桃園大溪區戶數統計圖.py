# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 21:04:36 2018

@author: Toby
"""
import requests,re
from bs4 import BeautifulSoup
url="http://www.daxi-hro.tycg.gov.tw/home.jsp?id=25&parentpath=0,21,22"
html=requests.get(url)
sp=BeautifulSoup(html.text,"html.parser")
a=sp.find_all("td",{"valign":"middle","align":"center"})
listy=[]
listx=[]
n=1
pat=re.compile("[0-9]{5}")
pat2=re.compile("[0-9]+")
for b in a:
    print(b.text)
    
    m=pat.findall(b.text)
    for i in m:
        listy.append(int(i))        
   
    
while(n<=len(a)):
    
    if( a[n].text!="─"):
        m2=pat2.search(a[n-1].text)
        listx.append(int(m2.group()))
    n+=2  



from bokeh.plotting import figure,show,output_file
p=figure(width=800,height=400,title="桃園市大溪區歷年戶數")
p.line(listx,listy)

p.xaxis.axis_label="年度"
p.yaxis.axis_label="戶數"


output_file("Bokeh繪製大溪區歷年戶數統計圖.html")
show(p)
