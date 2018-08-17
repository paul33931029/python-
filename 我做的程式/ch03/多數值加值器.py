# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 12:02:00 2018

@author: Toby
"""
howmany=int(input("你要幾個參數:"))



def    sum(*number): 
       
    list1=[]
    
    for a in range(howmany):
        b=int(input("第%d個參數:"%(a+1)))
        list1.append(b)     
    
        
    print(list1)
    print(list(enumerate(list1))) 
    x=0 
    i=0
    number=list(enumerate(list1))[0]
    print(number)
    
    while( number!=list(enumerate(list1))[howmany-1]):
        print("%d+"%(number[1]),end="")
        
        
        x+=number[1]    
        i+=1
        number=list(enumerate(list1))[i]
        
    print("%d="%(list1[howmany-1]),end="")
    return x+list1[howmany-1]         

print(sum())
