
import os
import re
import time

# import pdfkit
import requests
from bs4 import BeautifulSoup













def main():
    start = time.time()
    # urls = get_url_list()
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

