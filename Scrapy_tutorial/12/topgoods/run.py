# coding=utf-8

from scrapy import cmdline

name = 'tm_goods'

cmd = 'scrapy crawl {0} -o output/results.csv'.format(name)

# print(cmd.split())
cmdline.execute(cmd.split())
