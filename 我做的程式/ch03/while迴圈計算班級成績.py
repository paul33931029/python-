# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 22:22:04 2018

@author: Toby
"""
number=score=sum=0
while(score!=-1):
    number+=1
    sum+=score
    score=int(input("請輸入第%d位學生的成績:"%(number)))
print("本班平均成績:%d分,平均成績:%5.2f分"%(sum,sum/(number-1)))
    