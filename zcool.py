import urllib.request 
import io
import os
import sys
import http.cookiejar
from bs4 import BeautifulSoup
import urllib.request as rq
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') 
proxy_handler = urllib.request.ProxyHandler({'http':'sss:ssss@asasas'})
cj = http.cookiejar.CookieJar()
pro = urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(proxy_handler,pro)
headers = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'),
           ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
           ('Accept-Encoding','gzip, deflate, sdch'),
           ('Accept-Language','zh-CN,zh;q=0.8'),
           ('Host', 'www.zcool.com.cn')
           ]
opener.addheaders=headers
urllib.request.install_opener(opener)
#for num in range(1,5):
f = opener.open('http://www.zcool.com.cn/works/')
content = f.read().decode('utf-8')
g=open("zcooll.html","w",encoding='utf-8')
g.write(content)
g.close()

soup=BeautifulSoup(content)
aimgs=soup.find_all('ul',class_="layout camWholeBoxUl")
aimg=aimgs[0]
print(aimg)
'''
x=1
for asrc in aimg:
    print(asrc.get('src'))
    f=open(r"F:\py\imgs2"+"\\"+"Page"+str(num)+"-"+str(x)+os.path.splitext(asrc.get('data-original-image-url'))[1],'wb')
    f.write(urllib.request.urlopen(asrc.get('data-original-image-url')).read())
    f.close()
    x+=1
'''

