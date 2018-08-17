# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 15:12:35 2018

@author: Toby
"""
import os,ast
def enter_id_and_password():
    i=str(input("請輸入帳號(ENTER==>停止輸入):"))
    p=str(input("請輸入密碼:"))
    
    data1.setdefault(i,p)
    
def show():
    print("帳號","密碼",sep="   ")
    print("==============")
    listkey=list(data1.keys())
    for i in range(len(data1)):
        print("%-5s"%(listkey[i]),end="  ")
        print("%-5s"%(data1[listkey[i]]))
    print("按任意鍵返回主選單")
    enter()
    
    
def correct():
    i=str(input("請輸入要修改的帳號(Enter==>停止輸入):"))
    print("原來密碼為:"+data1[i],end="")
    f=str(input("請輸入新密碼:"))
    data1[i]=f
    print("密碼更改完畢,請按任意鍵返回主選單")
    enter()
 
def delete():
    i=str(input("請輸入要刪除的帳號(Enter==>停止輸入)"))
    boolean=str(input("確認要刪除%s的資料?:\n(Y/N)"%(i)))
    if(boolean=="Y"):
        del data1[i]
        print("已刪除完畢,請按任意鍵返回主選單")
        enter()
    elif(boolean=="N"):
        print("已取消您這次的刪除動作,請按任意鍵返回主選單")
        enter()



    
    


    
    
def enter():    
    while(input("")):
        break


cur_path=os.path.abspath("D:\pythonex\ch04\password")
os.system("cls")
choose=1
global data1
data1=dict()
while (choose!=0):
    print("1. 輸入號碼,密碼")
    print("2. 顯示帳號,密碼")
    print("3. 修 改 密 碼")
    print("4. 刪除帳號,密碼")
    print("0. 結 束 程 式")    
    print("-----------------------",end="")
    choose=int(input("請輸入您的選擇:"))
    if(choose==1):
        enter_id_and_password()
    if(choose==2):
        show()
    if(choose==3):
        correct()
    if(choose==4):
        delete()
    if(choose==8):
        f=open("D:\pythonex\ch04\password.txt",'w',encoding="UTF-8-sig")
        f.write(str(data1))    #write 只能寫str文字串進去
        f.close()
        with open('D:\pythonex\ch04\password.txt','r',encoding='UTF-8-sig') as f:
            filedata=f.read()   #read 只能read文字
            print(type(filedata))  
            data2=ast.literal_eval(filedata)   #把read到的文字分析然後轉換到list
            print(data2)    
            print(type(data2))
            break
        

            

        
    
    
    