# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem

class StackoverflowSpider(scrapy.Spider):
    name = 'stackoverflow'
    allowed_domains = ['stackoverflow.com']
    start_urls = [
        # 'http://stackoverflow.com/'
        # 'file:///home/lwq/Desktop/Python/tutorial/html/Highest Voted Questions - Stack Overflow.html'
        # "http://www.runoob.com/mongodb/mongodb-tutorial.html"
        'file:///home/lwq/Desktop/Python/tutorial/html/Books.html',
        'file:///home/lwq/Desktop/Python/tutorial/html/Resources.html'
    ]

    def parse(self, response):
        # filename = response.url.split('/')[-1]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        lis = response.xpath(".//*[@id='bd-cross']/fieldset[3]/ul/li")
        for li in lis:
            item = TutorialItem()
            item['title'] = li.xpath('a/text()').extract()[0]
            item['link'] = li.xpath('a/@href').extract()[0]
            item['desc'] = ''.join(li.xpath('text()').extract()).strip()
            # item['desc'] = li.xpath('text()')
            yield item
