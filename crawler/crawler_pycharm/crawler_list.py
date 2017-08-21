# coding=utf-8

import requests
from bs4 import BeautifulSoup


def get_url_list(url):
    """从给定的主页中抓取所需的链接列表"""

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    # 以下两句是本地测试用
    # with open("test.html") as f:
    #     soup = BeautifulSoup(f.read(), "html.parser")

    menu_tag = soup.find_all(class_="link_title")
    urls = []
    for item in menu_tag:
        url = "https://www.liaoxuefeng.com" + li.a.get('href')
        # url = item.a.get('href')  # 该行对应本地测试
        urls.append(url)
    return urls


def main():
    url = "http://blog.csdn.net/chenggong2dm/article/category/6137682"
    urls = get_url_list(url)

    with open("list.txt", "w") as f:
        f.write("")  # 清空文件内容
    with open("list.txt", "a") as f:
        for item in urls:
            f.write(str(item) + "\n")

if __name__ == '__main__':
    main()
