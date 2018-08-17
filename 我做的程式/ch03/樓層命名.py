# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 20:08:49 2018

@author: Paul
"""
floor=int(input("請輸入大樓的樓層數:"))
print("本大樓具有的樓層為:")
if(floor>3):
    for f in range(1,floor+2):
        if(f==4):
            continue
        print(f,end=" ")
else:
    for a in range(1,floor+1):
        print(a,end=" ")