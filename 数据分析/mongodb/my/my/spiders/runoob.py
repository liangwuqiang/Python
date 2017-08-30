# coding=utf-8

from scrapy import Spider, selector
from my.items import MyItem
import urllib
import urllib2
from bs4 import BeautifulSoup
import hashlib
import os
import re


class Runoob(Spider):
    name = "runoob"
    allowed_domains = ["www.runoob.com"]
    start_urls = [
        # "http://www.runoob.com/mongodb/mongodb-tutorial.html"
        "file:///home/lwq/Desktop/lwq/my/html/homepage.html"
    ]

    def parse(self, response):
        sel = selector.Selector(response)
        item = MyItem()
        menu = sel.xpath('.//div[@id="leftcolumn"]/a')

        index = 0
        for line in menu:
            item['title'] = line.xpath('text()').extract_first().strip()
            item['link'] = line.xpath('@href').extract_first().strip()
            index += 1
            # self.get_web_page(index, item)
            self.get_page(index, item)
            # break

    def get_page(self, index, item):
        url = item['link'].encode('utf-8')
        file_name = 'output/' + str(index) + '.html'
        urllib.urlretrieve(url, file_name)



    @staticmethod
    def get_web_page(index, item):
        url = 'file:///home/lwq/Desktop/lwq/my/html/homepage.html'
        # url = item['link'].encode('utf-8')
        print(url)

        response = urllib2.urlopen(url)
        html = response.read()
        # print(html)
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup)
        content = soup.find(class_="article-body")
        print(content)
        html = str(content)

        md5 = hashlib.md5()
        pattern = '<img .*?src=\"(.*?)\"'
        if not os.path.exists("output/images"):
            os.mkdir("output/images")

        for url in re.compile(pattern).findall(html):
            md5.update(url)
            ext = os.path.splitext(url)[1]
            image_name = "output/images/" + md5.hexdigest() + ext
            print(image_name)
            try:
                urllib.urlretrieve(url, image_name)
            except Exception as e:
                print("error", e)
            else:
                print(url)
                html = html.replace(url, image_name)

        html_template = """
            <!DOCTYPE html><html>
            <head><meta charset="UTF-8"></head>
            <body>
            {content}
            </body></html>        
            """
        html = html_template.format(content=html)

        filename = 'output/' + str(index) + '.' + item['title'].encode('utf-8') + '.html'
        with open(filename, 'w') as f:
            f.write(html)
        print('ok: ', index)
