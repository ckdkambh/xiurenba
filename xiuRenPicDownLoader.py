#coding-utf-8
import requests,re,json,html2text,sys,time,urllib.parse
from bs4 import BeautifulSoup
from array import array
import time 
from urllib.request import urlretrieve
import os

url="http://www.xiuren8.com/wp-content/plugins/dopwgg/uploads/Ah1ank42an4xWNB254Br59dnNDstcDGk6aWgOnSyzrzcyOjE47ZBntcOGnw8ndqym.jpg"
path = 'D:\\4444\\'

class PicDownLoader(object):
    def __init__(self, link="", name=1, fpath=path):
        self.link = link
        self.name = name
        self.fpath = fpath
        
    def setLink(self,link):
        self.link = link
        return self
    
    def getLink(self):
        return self.link
        
    def setName(self,name):
        self.name = name
        return self
    
    def getName(self):
        return self.name

    def setPath(self,fpath):
        self.fpath = fpath
        return self
    
    def getPath(fpath):
        return self.fpath
        
    def downPic(self):
        if not os.path.isdir(self.fpath):
            os.mkdir(self.fpath)
        #保存文件时候注意类型要匹配，如要保存的图片为jpg，则打开的文件的名称必须是jpg格式，否则会产生无效图片  
        print('Pic start download %s'%(self.link))
        conn = urllib.request.urlopen(self.link)
        print('Pic download done,start saving...')
        totalSize = 0
        with open(self.fpath+str(self.name)+".jpg",'wb') as f:
            while True:
                a1 = conn.read(100)
                if a1:
                    totalSize = totalSize+len(a1)
                    print("save %d bit"%(totalSize))
                    f.write(a1)
                else:
                    break
             
        print('Pic Saved!')   

if __name__=="__main__":
    a = PicDownLoader(url, 1)
    a.downPic()