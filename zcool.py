import urllib.request 
import io
import os
import sys
import http.cookiejar
from bs4 import BeautifulSoup
import urllib.request as rq
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') 
cj = http.cookiejar.CookieJar()
pro = urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(pro)
headers = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'),
           ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
           ('Accept-Language','zh-CN,zh;q=0.8'),
           ('Host', 'www.zcool.com.cn')
           ]
opener.addheaders=headers
urllib.request.install_opener(opener)
for numa in range(1,5):
  f = opener.open('http://www.zcool.com.cn/works/0!0!null!0!0!200!1!%s!!!'%numa)
  content = f.read().decode('utf-8')
  g=open("zcooll.html","w",encoding='utf-8')
  g.write(content)
  g.close()
  soup=BeautifulSoup(content)
  aimgs=soup.find_all('a',class_="image-link")
  num=0
  for aimg in aimgs:
    if int(aimg.find('img').get('width'))>30:
      link=aimg.find('img').get('src')
      f=open(r"F:\py2\imgs3"+"\\"+"第"+str(numa)+"页"+"第"+str(num)+"张图"+os.path.splitext(link)[1],'wb')
      f.write(urllib.request.urlopen(link).read())
      f.close()
      num+=1