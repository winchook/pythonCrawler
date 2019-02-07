import urllib.request
import re
url="https://n.yam.com/Article/20180724529828"
data2=urllib.request.urlopen(url,timeout=1200).read().decode("utf-8","ignore")
pat='<h2 class="newsTitle ">(.*?)</h2>'
title=re.compile(pat,re.S).findall(data2)
print("標題是:"+title[0])
