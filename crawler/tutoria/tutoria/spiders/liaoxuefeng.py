# -*- coding: utf-8 -*-
import scrapy
import sys
from tutoria.tutoria.items import TutoriaItem


class LiaoxuefengSpider(scrapy.Spider):
    name = "liaoxuefeng"
    allowed_domains = ["www.liaoxuefeng.com"]
    start_urls = [
        "https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000"
    ]

    @staticmethod
    def parse(self, response):
        sel = scrapy.selector.Selector(response)
        sites = sel.xpath('//div[@class="x-sidebar-left-content"]/ul[2]/li')

        items = []
        for site in sites:
            item = TutoriaItem()
            item['title'] = site.xpath('a/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            items.append(item)
        return items

