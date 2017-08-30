# coding=utf-8

from scrapy import cmdline

name = 'stackoverflow'

cmd = 'scrapy crawl {0} -s LOG_FILE=stackoverflow.log -o temp1.csv'.format(name)

cmdline.execute(cmd.split())
