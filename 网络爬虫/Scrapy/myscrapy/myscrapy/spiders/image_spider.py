# coding=utf-8

# from scrapy.spiders import BaseSpider
from scrapy.spiders import Spider
from scrapy.selector import HtmlXPathSelector

from myscrapy.items import ImageItem


# class MyImageSpider(BaseSpider):
class MyImageSpider(Spider):
    name = "image_spider"
    allowed_domains = ["http://topit.me/"]
    start_urls = [
        "http://topit.me/",
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        imgs = hxs.select('//img/@src').extract()
        item = ImageItem()
        item['image_urls'] = imgs
        return item
