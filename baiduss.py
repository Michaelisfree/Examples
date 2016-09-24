## -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup
import urllib.request as re
import urllib
import sys
import io
from collections import deque
queue=deque()
visited=set()
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
for num in range(10,100,10):
	url1='http://www.baidu.com/s?'
	value={ "wd":"python3",
	         "pn":num,
             "oq":"python3",
             "ie":"utf-8&usm=1",
             "rsv_pq":"d3951ef50000b429",
             "rsv_t":"1440J2Mi7DlGFGtvsExFqwKMOcHFN1zNx5wT0Kqm%2FBY8HlOxPw8w1AkGsHk"
           }
	url=url1+urllib.parse.urlencode(value)
	with re.urlopen(url) as f:
		data=f.read().decode('utf-8')
		soup1=BeautifulSoup(data).prettify()
		g=open("python%s.html"%num,"w",encoding='utf-8')
		g.write(soup1)
		g.close()
	
'''

for num in range(10,100,10):
	soup=BeautifulSoup(open('python%s.html'%num,'r',encoding="utf-8"))
	for link in soup.find_all('a'):
		if "http" in str(link.get('href')) or "https" in str(link.get('href')) and type(link.get('href'))!=None and str(link.get('href'))!="javascript:;"and str(link.get('href'))!="/"and str(link.get('href'))!="None":
			h=open("2-%s.txt"%num,"a",encoding='utf-8')
			h.write(str(link.get('href'))+'\n')
			h.close()
			





	for a in soup.select('a'):
		h=open("1-%s.txt"%num,"a",encoding='utf-8')
		h.write(a.get_text().strip()+'\n')
		h.close()

	
#ls=soup.select('a')
    
'''
    

