# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 11:44:43 2018

@author: Toby
"""

def ctof(c):
    f=c*9/5+32
    return f
temp=ctof(float(input("請輸入攝氏溫度:")))
print("華氏溫度為:%.1f度"%(temp))