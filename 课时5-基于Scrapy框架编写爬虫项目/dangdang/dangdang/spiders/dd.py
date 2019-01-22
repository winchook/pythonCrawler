# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangItem
from scrapy.http import Request
class DdSpider(scrapy.Spider):
    name = "dd"
    allowed_domains = ["dangdang.com"]
    start_urls = (
        'http://category.dangdang.com/pg1-cp01.54.06.00.00.00.html',
    )

    def parse(self, response):
        item=DangdangItem()
        item["title"]=response.xpath("//a[@name='itemlist-title']/@title").extract()
        item["link"] = response.xpath("//a[@name='itemlist-title']/@href").extract()
        item["comment"] = response.xpath("//a[@name='itemlist-review']/text()").extract()
        yield item
        print(item["title"])
        print(item["link"])
        print(item["comment"])
        for i in range(2,3):
            url="http://category.dangdang.com/pg"+str(i)+"-cp01.54.06.00.00.00.html"
            yield Request(url,callback=self.parse)

