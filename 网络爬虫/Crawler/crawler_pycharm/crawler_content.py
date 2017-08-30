# coding=utf-8

import re
from urllib import request
# import requests
from bs4 import BeautifulSoup
import time
import hashlib

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
        req = request.Request(url)
        response = request.urlopen(req)
        soup = BeautifulSoup(response.read().decode('utf-8'), 'html.parser')
        # response = requests.get(url)
        # soup = BeautifulSoup(response.content, "html.parser")
        # with open("test.html") as f:  # 本地测试
        #     soup = BeautifulSoup(f.read(), "html.parser")  # 本地测试

        # 截取内容
        title = soup.find(class_="link_title").get_text().strip()
        body = soup.find_all(class_="article_content tracking-ad")[0]

        # 重新对内容布局
        center_tag = soup.new_tag("center")
        title_tag = soup.new_tag('h3')
        title_tag.string = title
        center_tag.insert(1, title_tag)
        body.insert(0, center_tag)
        html = str(body)

        # 处理图片的超链接
        pattern = "(<img .*?src=\")(.*?)(\")"
        # pattern = "(<img .*?src=\")test_files(.*?)\.png(\")"  # 本地测试

        def func(m):
            # rtn = m.group(1) + "//http://blog.csdn.net" + m.group(2) + m.group(3)
            rtn = m.group(1) + m.group(2) + m.group(3)
            # rtn = m.group(1) + \
            #       "https://www.liaoxuefeng.com/files/attachments/00138676512923004999ceca5614eb2afc5c0efdd2e4640000" \
            #       + m.group(2) + m.group(3)  # 本地测试
            return rtn

        html = re.compile(pattern).sub(func, html)  # 链接改用绝对地址
        md5 = hashlib.md5()
        pattern = "<img .*?src=\"(.*?)\""
        for url in re.compile(pattern).findall(html):
            md5.update(url.encode('utf-8'))
            filename = "images/" + md5.hexdigest() + ".jpg"
            html = html.replace(url, filename)
            request.urlretrieve(url, 'output/' + filename)

        html = html_template.format(content=html)  # 形成完整的html文件

        # 文件输出
        filename = "output/" + str(index) + "." + str(title).replace('/', '_') + ".html"
        with open(filename, 'w') as f:
            f.write(html)

        print("完成计数:" + str(index))

        time.sleep(1)

    except Exception as e:
        print(e)


def main():
    # 从list.txt文件中导入url
    with open("list.txt") as f:
        htmls = [parse_url_to_html(url.strip(), index) for index, url in enumerate(f.readlines())]
        return htmls

if __name__ == '__main__':
    main()
