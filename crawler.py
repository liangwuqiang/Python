# coding=utf-8
import os
import re
import time

# import pdfkit
import requests
from bs4 import BeautifulSoup










def save_pdf(htmls, file_name):
    """
    把所有html文件保存到pdf文件
    :param htmls:  html文件列表
    :param file_name: pdf文件名
    :return:
    """
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
        'cookie': [
            ('cookie-name1', 'cookie-value1'),
            ('cookie-name2', 'cookie-value2'),
        ],
        'outline-depth': 10,
    }
    # pdfkit.from_file(htmls, file_name, options=options)


def main():
    start = time.time()
    urls = get_url_list()
    # file_name = u"liaoxuefeng_Python3_tutorial.pdf"

    # url = "https://www.liaoxuefeng.com/wiki/0014323396477522f8ff26917934f53b49559ab4dc5eab2000"
    url = 1
    # name = parse_url_to_html(url, "new.html")
    # save_pdf(htmls, file_name)
    #
    # for html in htmls:
    #     os.remove(html)
    #
    total_time = time.time() - start
    print(u"总共耗时：%f 秒" % total_time)
    # -----------------------------------


    # print(name)

if __name__ == '__main__':
    main()

