#http://tieba.baidu.com/p/2772122563
#page 2 URL add ?pn=2
#EVA volume_13
#version alpha 1.0

import urllib
import re

def openUrl(url):
	html=urllib.urlopen(url).read()
	return html

def downloadImg(html,i):
	pat=r'class="BDE_Image" src="(.*?\.jpg)"'
	imgPat=re.compile(pat)
	imgUrl=re.findall(imgPat,html)
	num=0
	for url in imgUrl:
		urllib.urlretrieve(url,'%s_%s.jpg' % (i,num))
		num+=1

urll=raw_input("Input Url to Download Comics:")
n=int(raw_input("Input Page Number:"))
for i in range(0,n):
	addr='%s?pn=%s' % (urll,i)
	page=openUrl(addr)
	downloadImg(page,i)
print "Comics Downloaded"

