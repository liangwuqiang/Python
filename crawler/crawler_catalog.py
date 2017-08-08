# coding=utf-8

import requests
from bs4 import BeautifulSoup

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
{content}
</body>
</html>

"""

def get_url_catalog(url):
    """从给定的主页中抓取所需的链接列表"""

    # response = requests.get(url)
    # soup = BeautifulSoup(response.content, "html.parser")
    # 以下两句是本地测试用
    with open("test.html") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    menu_tag = soup.find_all(class_="uk-nav uk-nav-side")[1]
    catalog = []
    for line in menu_tag.find_all("a"):
        # url = "https://www.liaoxuefeng.com" + li.a.get('href')
        # url = li.get_text()  # 该行对应本地测试
        print(line)
        catalog.append(line)
    return catalog


def main():
    url = "https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000"
    catalog = get_url_catalog(url)
    l =[]
    for item in catalog:
        l.append("<p>" + str(item) + "</p>\n")

    html = html_template.format(content=''.join(l))

    with open("output/catalog.html", "w") as f:
        f.write(html)  # 清空文件内容


if __name__ == '__main__':
    main()
