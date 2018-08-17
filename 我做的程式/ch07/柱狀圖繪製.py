# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 17:02:37 2018

@author: Toby
"""


import matplotlib.pyplot as plt
xlist=[1,5,7,9,13,16]
ylist=[15,50,80,40,70,50]
plt.bar(xlist,ylist,label="男性")
xlist1=[2,6,8,11,14,16]
ylist1=[10,40,30,50,80,60]
plt.bar(xlist1,ylist1,label="女性")
plt.title("零用金統計")
plt.xlabel("年齡")
plt.ylabel("零用金數目")
plt.ylim(0,100)
plt.xticks(range(0,21,5))
plt.legend()
plt.show()
