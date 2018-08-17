# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 20:51:59 2018

@author: Paul
"""
dict1={"林小明":85,"黃明晶":71,"曾山水":93}
dict1.setdefault("陳莉莉",98)
dict1.setdefault("鄭美麗",67)
nameandscore=list(dict1.items())
for i in range(0,5):
    print("%s 的成績為:%d分"%(nameandscore[i][0],nameandscore[i][1]))
    i+=1
#林小明   黃明晶    曾山水    陳莉莉    鄭美麗
#85   71    93    98 67