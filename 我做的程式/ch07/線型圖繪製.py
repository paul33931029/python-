# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 15:03:00 2018

@author: Toby
"""

import matplotlib.pyplot as plt
xlist=[1,5,7,9,13,16]
ylist=[15,50,80,40,70,50]
plt.plot(xlist,ylist,label="male")
xlist2=[2,6,8,11,14,16]
ylist2=[10,40,30,50,80,60]
plt.plot(xlist2,ylist2,color="red",lw=5.0,ls="--",label="female")

plt.ylim(0,100)
plt.title("Pocket Money")
plt.xlabel("Age")

plt.xticks(range(0,21,5))
plt.ylabel("Money")
plt.legend()
plt.show()