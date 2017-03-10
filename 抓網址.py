import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import os
#=================
#dest_dir=os.path.join(path,file_name)  
a=0
def download (x):
       global a
       filename = "logo"+str(a)+".jpg"
       path=r"F:\載圖\\"+data
       dest_dir=os.path.join(path,filename) 
       urlretrieve(x,dest_dir)
       a+=1
#=================
while(1):
       a=0
       data=input("請輸入圖片關鍵字:")
       f1 = open("抓取內容.txt", "w",encoding="utf-8")
       #============
       response = requests.get("https://www.google.com.tw/search?biw=1164&bih=593&site=webhp&tbm=isch&sa=100&q="+data)
       #response = requests.post("https://www.google.com.tw/search?biw=1164&bih=593&site=webhp&tbm=isch&sa=1&q="+data)
       soup = BeautifulSoup(response.text)
       print(response.text,file=f1)       
       if not os.path.exists(data):    #先確認資料夾是否存在
           os.makedirs(data)
       for d in soup.select('img'):     
              print(d)      
              download(d["src"])
       print("共",a,"張圖片")

f1.close()





