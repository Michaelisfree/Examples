import re
from collections import deque
import urllib
import urllib.request as rq
from bs4 import BeautifulSoup
queue=deque()
visited=set()
url="http://www.made-in-china.com"

queue.append(url)
cnt=0
while deque:
    url=queue.popleft()
    visited |={url}
    print("已经抓取",str(cnt),"条","正在抓取的链接为",url)
    cnt+=1
    urlop=rq.urlopen(url)
    if 'html' not in urlop.getheader('Content-Type'):
        continue

    try:
        data=urlop.read().decode('utf-8')
    except:
        continue
    '''
    linkrel=re.compile('href=\"(.*)\">')
    for x in linkrel.findall(data):
        if "http" in x or "https" in x and x not in visited:
            queue.append(x)
            print('加入队列---->',x)
    '''

    soup=BeautifulSoup(data)
    for x in soup.find_all('a'):
        if "http" in x.get('href') or "https" in x.get('href') and x.get('href') not in visited:
            queue.append(x.get('href'))
            h=open("lianje.txt","a",encoding='utf-8')
            h.write(x.get('href')+'\n')
            h.close()
            print('加入队列---->',x.get('href'))










