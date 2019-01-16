import urllib.request
import re
cid="6375489932584768380"
for i in range(0,100):
    print("第"+str(i+1)+"页的评论数据")
    url="https://video.coral.qq.com/varticle/2461939412/comment/v2?callback=_varticle2461939412commentv2&orinum=10&oriorder=o&pageflag=1&cursor="+str(cid)+"&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=9"
    data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
    pat1='"content":"(.*?)"'
    comment=re.compile(pat1,re.S).findall(data)
    for item in comment:
	    #强制转换成中文
        print(eval('u"'+str(item)+'"'))
        print("-------")
    pat2='"last":"(.*?)"'
    cid=re.compile(pat2,re.S).findall(data)[0]

