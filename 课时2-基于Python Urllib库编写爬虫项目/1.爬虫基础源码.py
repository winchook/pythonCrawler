#爬网页
import urllib.request
import re
import random
url="http://www.jd.com"
#爬到内存中
data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
pat="<title>(.*?)</title>"
rst=re.compile(pat,re.S).findall(data)
#print(rst)
#爬到硬盘的文件中
urllib.request.urlretrieve(url,filename="D:/我的教学/Python/阿里云 Python网络爬虫/test.html")

#浏览器伪装
#尝试
url="https://www.qiushibaike.com/"
#data=urllib.request.urlopen(url).read().decode("utf-8","ignore")

opener=urllib.request.build_opener()
UA=("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
opener.addheaders=[UA]
urllib.request.install_opener(opener)
data=urllib.request.urlopen(url).read().decode("utf-8","ignore")

#用户代理池
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
for i in range(0,10):
    UA()
    data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
#思考：如何实现每爬3次换一次UA
for i in range(0,10):
    if(i%3==0):
        UA()
    data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
    print(len(data))
