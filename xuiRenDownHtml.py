#coding-utf-8
import requests,re,json,html2text,sys,time,urllib.parse
from bs4 import BeautifulSoup
from array import array
import time 
from urllib.request import urlretrieve
import os
from xiuRenPicDownLoader import PicDownLoader

sys.setrecursionlimit(1000000) #例如这里设置为一百万
url="http://www.t66y.com/htm_data/7/1610/2110560.html"
path = 'D:\\3333\\'
  

    
class ContextDownLoader(object):

    def __init__(self, link, path='D:\\3333\\'):
        self.link = link
        self.path = path
    
    def setLink(self,link):
        self.link = page
        return self
    
    def getLink(self):
        return self.link

    def setPath(self,path):
        self.path = path
        return self
    
    def getPath(self):
        return self.path
    
    def downHtmlCont(self):
        while True:
            try:
                get_url = requests.get(self.link)
                break
            except requests.exceptions.ContentDecodingError as e:
                print('网页读取错误正在重试...')
                time.sleep(1)
                continue
            except requests.exceptions.ProxyError as e:    
                print('网络连接错误正在重试...')
                time.sleep(1)
                continue
            except requests.exceptions.ConnectionError as e:    
                print('网络连接错误正在重试...')
                time.sleep(1)
                continue
        print("get html source code done.start analysis...")        
        codingTypr = get_url.encoding
        soup = BeautifulSoup(get_url.text,"html5lib")
        print("analysis done")
        titleList = soup.find_all("title")
        try:
            title = titleList[0].string.encode(codingTypr, errors='ignore').decode('utf-8', errors='ignore').split('|')[0]
        except IndexError as e:
            return
        title = title.replace(" ","")
        print('down loading:%s'%(title))
        fpath = self.path+title+'.html'
        try:
            with open(fpath, 'w') as f:
                f.write('')
            with open(fpath, 'a') as f:
                f.write('<title>%s</title>\n'%(title))
            with open(fpath, 'a') as f:
                f.write('<link href=\"%s\" />\n'%(self.link))
        except OSError as e:
            return
        imgList = soup.find_all("img", class_="Image")
        for i in imgList:
            try:
                with open(fpath, 'a') as f:
                    f.write('%s\n'%(i))
            except OSError as e:
                return

        
        
        
        
if __name__=="__main__":
    print('runing..............')
    a = ContextDownLoader(url)
    a.downHtmlCont()
    print('done')        
        
        
        
        
        
        
        
        
        