import urllib.request
import re
import random
import time
uapools=[
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    ]
def UA():
    opener=urllib.request.build_opener()
    thisua=random.choice(uapools)
    ua=("User-Agent",thisua)
    opener.addheaders=[ua]
    urllib.request.install_opener(opener)
    print("当前使用UA："+str(thisua))
for i in range(0,6):
    UA()
    thisurl="http://www.qiushibaike.com/8hr/page/"+str(i+1)+"/"
    try:
        data=urllib.request.urlopen(thisurl).read().decode("utf-8","ignore")
        pat = '<div class="recmd-tag">(.*?)</div>'
        rst=re.compile(pat,re.S).findall(data)
        for j in range(0,len(rst)):
            print(rst[j])
            print("-------")
    except Exception as err:
        pass