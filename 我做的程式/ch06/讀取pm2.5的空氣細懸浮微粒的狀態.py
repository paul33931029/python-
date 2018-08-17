# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 21:11:52 2018

@author: Paul
"""

import hashlib,requests,os,ast,sqlite3
url="http://opendata2.epa.gov.tw/AQI.json"
html=requests.get(url).text.encode("utf-8-sig")      #byte形式
md5=hashlib.md5(html).hexdigest()                    #byte加密並轉成16進位形式 很短 所以很好比較
if os.path.exists("old_md5.text"):                    
    with open("old_md5.text","r",)as f:               #讀前幾天我儲存他的url到old_md5.text 的file    
        oldversion=f.read()                           
    with open("old_md5.text","w")as f:                 #把old_md5.text更新
        f.write(str(md5))
else:
    with open("old_md5.text","w")as f:                 #若沒有old_md5.text黨,做一個然後寫更新的code到裡面
        f.write(str(md5))
if(oldversion==md5):
    print("資料已更新")                                #若oldversion=新的code,可以顯示已更新
else:
    print("file資料還沒更新,我幫你更新新的版本到file") #若oldversion不等於,顯示沒有更新,然後再更新

from bs4 import BeautifulSoup
html1=requests.get(url)
sp=BeautifulSoup(html1.text,"html.parser")
change=ast.literal_eval(html1.text)
conn=sqlite3.connect("PM2.5.sqlite")
cursor=conn.cursor()
sqlstr='CREATE TABLE IF NOT EXISTS PM25 \
("站名" TEXT PRIMARY KEY NOT NULL,"PM2.5" TEXT)'
cursor.execute(sqlstr)
conn.commit()
for row in change:
    if(row["PM2.5"]!=""):
        cursor.execute ('insert or replace into PM25 values("{}","{}")'.format(row["SiteName"],row["PM2.5"]))
    else:
        cursor.execute('insert or replace into PM25 values("{}","{}")'.format(row["SiteName"],"ND"))
    conn.commit()
cursor1=conn.execute('select * from PM25')
rows=cursor1.fetchall()
for r in rows:
    print("站名:%s\tPM2.5:%s"%(r[0],r[1]))
conn.close()