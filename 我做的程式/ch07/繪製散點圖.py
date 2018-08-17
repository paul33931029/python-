# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 20:48:43 2018

@author: Toby
"""
from bokeh.plotting import figure,show,output_file
p=figure(width=800,height=400,title="零用金統計")
listx=[1,5,7,9,13,16]
listy=[15,50,80,40,70,50]
size=[10,20,30,30,20,10]
color=["red","blue","green","pink","violet","grey"]
p.circle(listx,listy,size=size,color=color)
output_file("繪製散點圖.html")
p.xaxis.axis_label="x軸"
p.yaxis.axis_label="y軸"
show(p)