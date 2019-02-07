def getCartoon(page):
    from selenium import webdriver
    import time
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    import re
    import urllib.request
    dcap = dict(DesiredCapabilities.PHANTOMJS)  
    dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/4.0 (compatible; MSIE 5.5; windows NT)"  )  
    browser = webdriver.PhantomJS(desired_capabilities=dcap)
    #打开动漫的一页
    browser.get("http://ac.qq.com/ComicView/index/id/539443/cid/"+str(page))
    for i in range(20):
        js='window.scrollTo('+str(1280)+','+str((i+1)*720)+')'
        browser.execute_script(js)
        time.sleep(1)
    #将打开的界面截图保存，方便观察
    a=browser.get_screenshot_as_file("D:/我的教学/Python/test1.jpg")
    #获取当前页面所有源码（此时包含触发出来的异步加载的资源）
    data=browser.page_source
    #将相关网页源码写入本地文件中，方便分析
    fh=open("D:/我的教学/Python/dongman.html","w",encoding="utf-8")
    fh.write(data)
    fh.close()
    browser.quit()
    #构造正则表达式提取动漫图片资源网址
    pat='<img src="(https:\/\/manhua.qpic.cn\/manhua_detail.*?.jpg\/0)"'
    #获取所有动漫图片资源网址
    allid=re.compile(pat,re.S).findall(data)
    print(allid)
    for i in range(0,len(allid)):
        #得到当前网址
        thisurl=allid[i]
        #输出当前爬取的网址
        print(thisurl)
        #设置将动漫存储到本地的本地目录
        localpath="D:/我的教学/Python/dongman/"+str(page)+"__"+str(i)+".jpg"
        #通过urllib对动漫图片资源进行爬取
        urllib.request.urlretrieve(thisurl,filename=localpath)
for page in range(1,10):
    print("正在爬取第"+str(page)+"页")
    getCartoon(page)
print("全部爬完")
