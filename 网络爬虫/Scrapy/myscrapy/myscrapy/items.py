# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class MyscrapyItem(Item):
    # define the fields for your item here like:
    title = Field()
    content = Field()
    image_urls = Field()


class ImageItem(Item):
    image_urls = Field()
    images = Field()
    image_paths = Field()


