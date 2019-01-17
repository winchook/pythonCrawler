'''
请求方式:get、post、put…
参数：params、headers、proxies、cookies、data
text    响应数据
content  响应数据（b）
encoding  网页编码
cookies   响应cookie
url       当前请求的url
status_code   状态码
'''

import requests
import re
hd={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0",}
px={"http":"http://127.0.0.1:8888"}
rst=requests.get("http://www.aliwx.com.cn/",headers=hd)
title=re.compile("<title>(.*?)</title>",re.S).findall(rst.text)
pr={"wd":"阿里文学",}
rst=requests.get("http://www.baidu.com/s",params=pr)
postdata={"name":"测试账号",
      "pass":"测试密码",
      }
rst=requests.post("http://www.iqianyue.com/mypost/",data=postdata)
