# -*- coding: utf-8 -*-
import scrapy
from my17k.items import My17KItem
from scrapy.http import Request

class Mys1Spider(scrapy.Spider):
    name = 'mys1'
    allowed_domains = ['17k.com']
    start_urls = ['http://www.17k.com/book/1.html']

    def parse(self, response):
        item=My17KItem()
        item["name"]=response.xpath('//div[@class="infoPath"]/div/a[@class="red"]/text()').extract()
        print("------------:"+str(item["name"]))
        yield item
        for i in range(2,5739387):
            thisurl="http://www.17k.com/book/"+str(i)+".html"
            yield Request(thisurl,callback=self.parse)