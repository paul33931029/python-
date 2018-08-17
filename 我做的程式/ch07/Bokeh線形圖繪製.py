# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 13:43:45 2018

@author: Toby
"""
from bokeh.plotting import figure,show,output_file
xlist=[1,5,7,9,13,16]
ylist=[15,50,80,40,70,50]
xlist1=[2,6,8,11,14,16]
ylist1=[10,40,30,50,80,60]
p=figure(width=800,height=400,title="零用金統計")
p.line(xlist,ylist,line_color="red",line_alpha=0.3,line_dash=[12,3],legend="男性")
p.line(xlist1,ylist1,legend="女性")
p.xaxis.axis_label="年齡"
p.yaxis.axis_label="零用金"
output_file("零用金統計.html")
show(p)
