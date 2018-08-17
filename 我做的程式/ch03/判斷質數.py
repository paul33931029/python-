# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 21:55:05 2018

@author: Toby
"""

number=int(input("請輸入大於一的整數:"))
for a in range(2,number):
    if (number%a==0):
        print("%d不是質數!"%(number))  
        break
else:
    print("%d是質數!"%(number))
  
    
        