from bs4 import BeautifulSoup
import urllib
import urllib.request as rq
import sys
import io
import os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
for page in range(1,10):
	url='http://baozoumanhua.com/?page=%s&sv=1475070602'%page
	content=rq.urlopen(url).read().decode('utf-8')
	soup=BeautifulSoup(content)
	aimg=soup.find_all('img',class_="lazy")
	x=0
	for asrc in aimg:
		try:
			rq.urlopen(asrc.get('data-original-image-url')).read()
		except:
			continue
	print(asrc.get('data-original-image-url'))
	f=open(r"F:\py2\imgs2"+"\\"+str(x)+os.path.splitext(asrc.get('data-original-image-url'))[1],'wb')
	f.write(rq.urlopen(asrc.get('data-original-image-url')).read())
	f.close()
	x+=1
	


