import time
from selenium import webdriver
browser = webdriver.PhantomJS()
browser.get("http://www.baidu.com")
a=browser.get_screenshot_as_file("D:/Python35/test.jpg")
#在网页上右键审查元素，复制Xpath即可得到
#清空内容
browser.find_element_by_xpath('//*[@id="kw"]').clear()
#输入内容
browser.find_element_by_xpath('//*[@id="kw"]').send_keys("爬虫")
#搜索内容
browser.find_element_by_xpath('//*[@id="su"]').click()
time.sleep(5)
a=browser.get_screenshot_as_file("D:/Python35/test.jpg")
data=browser.page_source
browser.quit()
print(len(data))
import re
title=re.compile("<title>(.*?)</title>").findall(data)
print(title)
