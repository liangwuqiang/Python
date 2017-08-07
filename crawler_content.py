# coding=utf-8

import re
import requests
from bs4 import BeautifulSoup
import time

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


def parse_url_to_html(url, index):
    """ 通过url获得文本内容,并存入文件中 """
    try:
        print(url)
        print(index)
        # url = "https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432339247097eea476bf61f8496092cc1b663eae1848000"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        # 本地测试
        # with open("test.html") as f:  # 本地测试
        #     soup = BeautifulSoup(f.read(), "html.parser")  # 本地测试

        # 正文内容
        body = soup.find_all(class_="x-wiki-content")[0]
        # 标题
        title = soup.find('h4').get_text()

        # 标题加入到正文的最前面，居中显示
        center_tag = soup.new_tag("center")
        title_tag = soup.new_tag('h1')
        title_tag.string = title
        center_tag.insert(1, title_tag)
        body.insert(0, center_tag)
        html = str(body)

        # body中的img标签的src相对路径的改成绝对路径,图片处理
        pattern = "(<img .*?src=\")(.*?)(\")"
        # pattern = "(<img .*?src=\")test_files(.*?)\.png(\")"  # 本地测试

        def func(m):
            rtn = m.group(1) + "https://www.liaoxuefeng.com" + m.group(2) + m.group(3)
            # rtn = m.group(1) + \
            #       "https://www.liaoxuefeng.com/files/attachments/00138676512923004999ceca5614eb2afc5c0efdd2e4640000"\
            #       + m.group(2) + m.group(3)  # 本地测试
            return rtn

        html = re.compile(pattern).sub(func, html)  # 处理图片中的链接
        html = html_template.format(content=html)  # 处理后的内容套入模板中,形成完整的html文件

        filename = "output/" + str(index) + "." + title + ".html"
        with open(filename, 'w') as f:
            f.write(html)

        time.sleep(5)

    except Exception as e:
        print(e)


def main():
    # 网络单网页测试
    # url = "https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/" \
    #       "0014323396477522f8ff26917934f53b49559ab4dc5eab2000"
    # file_index = 0
    with open("list.txt") as f:
        # for url in f.readlines():
            # parse_url_to_html(url, file_index)
            # print(url)
            # print(file_index)
            # file_index += 1
            # time.sleep(2)
        htmls = [parse_url_to_html(url, index) for index, url in enumerate(f.readlines())]
        return htmls

if __name__ == '__main__':
    main()
