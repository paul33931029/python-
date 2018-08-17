# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 16:39:02 2018

@author: Toby
"""
def show():
    cursor=conn.execute('select*from password')
    rows=cursor.fetchall()
    print("帳號    密碼\n-------------------")
    for r in rows:
        print("%-3s"%(r[0]),end='   ')
        print("%-6s"%(r[1]))     
    conn.commit()
    conn.close()
    
def ID_password(value):
    
    
    a=str(input("請輸入帳號(Enter==>停止輸入)"))
    
    b=str(input("請輸入密碼:"))
    print("%s已輸入完畢"%(a))
    conn.execute("insert into password values('{}','{}')".format(a,b))
    conn.commit()
    conn.close()

def press():
    while(input("")):
        break
    


def change():
    def search(value):
        cursor=conn.execute("select*from password where name='{}'".format(value))
        row=cursor.fetchone()
        print(row)
        print("原來密碼為:{}".format(row[1]))
        conn.commit()
    a=str(input("請輸入要修改的帳號(Enter==>停止輸入)"))
    search(a)
    b=str(input("請輸入新密碼:"))
    conn.execute("update password set pass='{}'where name='{}'".format(b,a))
    conn.commit()
    conn.close()
    print("密碼更改完畢,請按任意鍵返回主選單")
    press()


def delete():
    a=str(input("請輸入要刪除的帳號(Enter==>停止輸入)"))
    b=str(input("確定要刪除{}的帳號?".format(a)))
    if(b=='Y'):
        conn.execute("delete from password where name='{}'".format(a))
        conn.commit()
        conn.close()
        print("已刪除完畢,請按任意鍵返回主選單")
        press()
    
    
    
    
import sqlite3
enter=""
while(enter!=0):
    print("1. 輸入號碼,密碼")
    print("2. 顯示帳號,密碼")
    print("3. 修 改 密 碼")
    print("4. 刪除帳號,密碼")
    print("0. 結 束 程 式")    
    print("-----------------------",end="")
    enter=int(input("請輸入你的選擇:"))
    conn=sqlite3.connect("sqlite01.sqlite")
    if(enter==2):
        show()
    if(enter==1):
        ID_password()
    if(enter==3):
        change()
    if(enter==4):
        delete()
    if(enter==0):
        conn.close()
        print("程式已結束")
        break
    
