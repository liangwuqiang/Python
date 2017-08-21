# -*- coding: utf-8 -*-
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MyscrapyPipeline(object):
    def process_item(self, item, spider):
        return item


class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item

"""
ImagePipeline

需要在自定义的ImagePipeline类中重载的方法：
get_media_requests(item, info)和item_completed(results, items, info)

正如工作流程所示，Pipeline将从item中获取图片的URLs并下载它们，
所以必须重载get_media_requests，并返回一个Request对象，
这些请求对象将被Pipeline处理，当完成下载后，结果将发送到item_completed方法，
这些结果为一个二元组的list，每个元祖的包含(success, image_info_or_failure)。 
* success: boolean值，true表示成功下载 * image_info_or_error：
如果success=true，image_info_or_error词典包含以下键值对。失败则包含一些出错信息。 
* url：原始URL * path：本地存储路径 * checksum：校验码
"""
