# -*- coding: utf-8 -*-
import scrapy
from myscrapy.items import MyscrapyItem

html_template = """\
<!DOCTYPE html><html>
<head><meta charset="UTF-8"></head>
<body>
{content}
</body></html>
"""


class OneSpider(scrapy.Spider):
    name = 'one'
    allowed_domains = ['www.cnblogs.com']
    start_urls = [
        # 'http://www.cnblogs.com/wuxl360/p/5567631.html'
        'file:///home/lwq/Desktop/myscrapy/html/test.html'
        ]

    def parse(self, response):
        item = MyscrapyItem()

        item['title'] = response.xpath('.//div[@class="post"]/h2/a/text()').extract_first()
        item['content'] = response.xpath('.//div[@id="cnblogs_post_body"]').extract_first()
        image_urls = response.xpath('.//img[@src]/@src').extract()[0]
        # for each in image_urls:
        #     item['image_urls'].append('file:///home/lwq/Desktop/myscrapy/html/' + each)
        item['image_urls'] = 'file:///home/lwq/Desktop/myscrapy/html/' + image_urls

        title = '<center><h1>' + item['title'] + '</h1></center>'
        content = title + '\n' + item['content']
        html = html_template.format(content=content)

        # with open('output/temp.html', 'w') as f:
        #     f.write(html)

        images = item['image_urls']
        print(type(images))
        print(images)
        # with open('output/lwq.jpg', 'wb') as f:
        #     f.write(imgaes)

        return item


