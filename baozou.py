import urllib.request 
import io
import os
import sys
from bs4 import BeautifulSoup
import urllib.request as rq
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') 
proxy_handler = urllib.request.ProxyHandler({'http':account:password@proxy'})   
opener = urllib.request.build_opener(proxy_handler)
urllib.request.install_opener(opener)
for num in range(1,10):
    f = opener.open('http://baozoumanhua.com/?page=%s&sv=1475122801'%num)
    content = f.read().decode('utf-8')
#print(content)
    soup=BeautifulSoup(content)
    aimg=soup.find_all('img',class_="lazy")
#print(aimg)
    x=1
    for asrc in aimg:
        print(asrc.get('data-original-image-url'))
        f=open(r"F:\py\imgs2"+"\\"+"Page"+str(num)+"-"+str(x)+os.path.splitext(asrc.get('data-original-image-url'))[1],'wb')
        f.write(urllib.request.urlopen(asrc.get('data-original-image-url')).read())
        f.close()
        x+=1


