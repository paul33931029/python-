# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 12:05:19 2018

@author: Toby
"""

import matplotlib.pyplot as plt
size=[10,20,40,30]
explode=[0,0,0.05,0]
labels=["東部","南部","北部","西部"]
plt.pie(size,explode=explode,labels=labels,autopct="%2d%%",shadow=True,startangle=90)
plt.legend()
plt.axis("equal")