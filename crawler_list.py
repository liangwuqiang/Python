# coding=utf-8

import requests
from bs4 import BeautifulSoup


def get_url_list(url):
    """从给定的主页中抓取所需的链接列表"""

    # response = requests.get(url)
    # soup = BeautifulSoup(response.content, "html.parser")
    # 以下两句是本地测试用
    with open("test.html") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    menu_tag = soup.find_all(class_="uk-nav uk-nav-side")[1]
    urls = []
    for li in menu_tag.find_all("li"):
        # url = "https://www.liaoxuefeng.com" + li.a.get('href')
        url = li.a.get('href')  # 该行对应本地测试
        urls.append(url)
    return urls


def main():
    url = "https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000"
    urls = get_url_list(url)

    with open("list.txt", "w") as f:
        f.write("")  # 清空文件内容
    with open("list.txt", "a") as f:
        for item in urls:
            f.write(str(item) + "\n")

if __name__ == '__main__':
    main()
