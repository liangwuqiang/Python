# coding=utf-8

from scrapy import cmdline

name = "runoob"

cmd = 'scrapy crawl {0} -s LOG_FILE=my.log'.format(name)

cmdline.execute(cmd.split())

