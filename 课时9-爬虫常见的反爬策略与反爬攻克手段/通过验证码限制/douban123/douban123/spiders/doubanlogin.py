# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,FormRequest
import urllib.request
import os
class DoubanloginSpider(scrapy.Spider):
    name = 'doubanlogin'
    allowed_domains = ['douban.com']
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/57.0"}
    #start_urls = ['https://www.douban.com/']
    def start_requests(self):
        # 首先爬一次登录页，然后进入回调函数parse()
        return [Request("https://accounts.douban.com/login", meta={"cookiejar": 1}, callback=self.parse)]
    def parse(self, response):
        #判断是否有验证码
        ischapter=response.xpath("//img[@id='captcha_image']/@src").extract()
        if(len(ischapter)>0):
            #有验证码
            print("有验证码…")
            chapter=ischapter[0]
            localpath = "D:/我的教学/Python/天善智能-爬虫/12/douban123/yanzhengma/captcha.png"
            urllib.request.urlretrieve(chapter, filename=localpath)
            #thiscaptcha=input("请输入验证码：")
            cmd = "D:/Python27/python.exe D:/Python27/yzm/YDMPythonDemo.py"
            r = os.popen(cmd)
            thiscaptcha = r.read()
            print("验证码自动识别成功，识别结果为："+str(thiscaptcha))
            thiscaptchaid=chapter.replace("https://www.douban.com/misc/captcha?id=","").replace("&amp;size=s","").replace("&size=s","")
            data = {
                "source": "index_nav",
                "redir": "https://www.douban.com/note/667786391/",
                "form_email": "weisuen007@aliyun.com",
                "form_password": "weijc7789",
                "captcha-solution":thiscaptcha,
                "captcha-id":thiscaptchaid,
                "login":"登录",
            }
            #print(data)
        else:
            #没有验证码
            data = {
                "source":"index_nav",
                "redir": "https://www.douban.com/note/667786391/",
                "form_email": "weisuen007@aliyun.com",
                "form_password": "weijc7789",
            }
        print("登录中……")
        return [FormRequest.from_response(response,
                                          # 设置cookie信息
                                          meta={"cookiejar": response.meta["cookiejar"]},
                                          # 设置headers信息模拟成浏览器
                                          headers=self.header,
                                          # 设置post表单中的数据
                                          formdata=data,
                                          # 设置回调函数，此时回调函数为next()
                                          callback=self.next,
                                          )]
    def next(self,response):
        #能够登录
        #title=response.xpath("/html/head/title/text()").extract()
        #print("----------"+str(title))
        return [Request("https://www.douban.com/people/178079565/", meta={"cookiejar": response.meta["cookiejar"]},callback=self.userindex)]
    def userindex(self,response):
        title=response.xpath("//div[@class='note-header pl2']/a/@title").extract()
        content=response.xpath("//div[@class='note']/text()").extract()
        print("个人中心页的所有日记标题与内容是：")
        for i in range(0,len(title)):
            print(title[i])
            print(content[i])
            print("-----------")

