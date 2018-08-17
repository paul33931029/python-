# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 11:24:13 2018

@author: Toby
"""

x=int(input("請輸入國文成績:"))
y=int(input("請輸入數學成績:"))
z=int(input("請輸入英文成績:"))
a=x+y+z
print("成績總分="+str(a)+",平均成績=%5.2f"%(a/3))