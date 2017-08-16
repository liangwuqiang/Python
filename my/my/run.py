# coding=utf-8

from scrapy import cmdline

name = 'example'

cmd = 'scrapy crawl {0} -o items.json -t json'.format(name)

cmdline.execute(cmd.split())
