# coding=utf-8

import scrapy


class LiaoxuefengSpider(scrapy.spiders.Spider):
    name = "liaoxuefeng"
    allowed_domains = ["www.liaoxuefeng.com"]
    start_urls = [
        "http://"
    ]

    def parser(self, response):
        current_url = response.url
        body = response.body
        unicode_body = response.body_as_unicode()
