# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 12:30:26 2018

@author: Toby
"""
score=number=sum=0
list1=[]
while(score!=-1):
    number+=1
    score=int(input("請輸入第%d位學生的成績:"%(number)))
    list1.append(score)
    sum+=list1[number-1]
print("共有%d位學生\n本班總成績:%d分,平均成績:%5.2f分"%(number-1,sum+1,((sum+1)/(number-1))))
