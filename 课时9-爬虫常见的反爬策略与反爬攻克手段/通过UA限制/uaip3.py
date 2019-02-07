import time
#如何同时使用用户代理池和IP代理池
def ua_ip(ippools,myurl,thisapi):
    import random
    uapools=[
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
        ]
    import urllib.request
    def api(thisapi):
        print("这一次调用了接口")
        import urllib.request
        urllib.request.urlcleanup()
        thisall=urllib.request.urlopen(thisapi).read().decode("utf-8","ignore")
        print("接口调用完成")
        return thisall
    def ip(ippools,uapools):
        thisua=random.choice(uapools)
        print(thisua)
        headers=("User-Agent",thisua)
        thisip=ippools
        #thisip="127.0.0.1:8888"
        print("当前用的IP是："+thisip)
        proxy=urllib.request.ProxyHandler({"http":thisip})
        opener=urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
        opener.addheaders=[headers]
        urllib.request.install_opener(opener)
    if(ippools==0):
        while True:
            ippools=api(thisapi)
            print("提取IP完成")
            ip(ippools,uapools)
            print("正在验证IP有效性")
            data1=urllib.request.urlopen("http://www.baidu.com").read().decode("utf-8","ignore")
            if(len(data1)>5000):
                print("-----当前IP有效-----")
                break
            else:
                print("-----当前IP无效，正在延时60秒重新切换-----")
                time.sleep(60)
    url=myurl
    data1=urllib.request.urlopen(url).read()
    data=data1.decode("utf-8","ignore")
    return ippools,data
#data=ua_ip(0,"http://www.baidu.com")








    
