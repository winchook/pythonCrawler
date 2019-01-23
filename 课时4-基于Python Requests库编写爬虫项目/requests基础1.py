'''

【请求方式】
get,post,put,最常用的是get请求
【参数】
params:添加get方式请求的参数
headers:添加头信息
proxies:添加代理
cookies:添加cookie
data:post请求发过去的数据
【属性】
text:响应数据
content:响应数据(b二进制类型的流数据)
encoding:网页编码
cookies:取出cookies
url:取出当前网页的url
status_code:状态码

'''
import requests
import re
rst=requests.get("http://www.aliwx.com.cn")
title=re.compile("<title>(.*?)</title>",re.S).findall(rst.text)
print(title)
