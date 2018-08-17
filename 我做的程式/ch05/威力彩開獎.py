# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 22:57:41 2018

@author: Toby
"""



def findball():
    a=sp.find_all("div",{"class":"ball_tx ball green"})
    for ball in a:
        print(a[ball])
        
        
import requests,re
from bs4 import BeautifulSoup   
url='http://www.taiwanlottery.com.tw'
html=requests.get(url)                               #取得原始碼
sp=BeautifulSoup(html.text,'html.parser')
data=sp.select("#rightdown")                         #找到id rightdown的超連結內容
data2=data[0].find("div",{"class":"contents_box02"})  #data[0]不是普通string,是經過sp過的string
data3=data2.find("div",{"class":"contents_mine_tx04"})#從contents_box02找到contents_mine_tx04
pat=re.compile("[\u4e00-\u9fa5]+")
m=pat.findall(str(data3))
print("%s:"%m[0],end=" ")                              #開出順序:
find_ball=data2.find_all("div",{"class":"ball_tx ball_green"})
for first_row_ball in range(6):
    print(find_ball[first_row_ball].text,end="   ")    #第一排綠球
print("\n%s:"%m[1],end=" ")                            #大小順序
for second_row_ball in range(6,12):
    print(find_ball[second_row_ball].text,end="   ")   #第二排綠球
print("\n%s:"%m[2],end=' ')
print(data2.find("div",{"class":"ball_red"}).text)    
 
    