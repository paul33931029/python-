# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 12:53:18 2018

@author: Toby
"""

x=int(input("請輸入購物金額:"))
if(x>=100000):
    x*=.8
    print(str(x)+"元")
elif(x>=50000):
    x*=.85
    print(str(x)+"元")
elif(x>=30000):
    x*=.9
    print(str(x)+"元")
elif(x>=10000):
    x*.95
    print(str(x)+"元")
else:
    print(str(x)+"元")
    

