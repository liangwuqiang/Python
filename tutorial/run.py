# coding=utf-8
from scrapy import cmdline

name = 'stackoverflow'

cmd = 'scrapy crawl {0} -s LOG_FILE=tutorial.log -o temp.csv'.format(name)

cmdline.execute(cmd.split())
