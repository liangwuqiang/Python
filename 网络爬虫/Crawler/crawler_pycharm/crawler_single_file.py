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


def single_url_to_html(url, tag_title, tag_body):
    """ 通过url获得文本内容,并存入文件中 """
    try:
        # response = requests.get(url)
        # soup = BeautifulSoup(response.content, "html.parser")
        with open("test.html") as f:
            soup = BeautifulSoup(f.read(), "html.parser")

        # 标题
        title = soup.find(class_=tag_title).get_text()
        # 正文内容
        body = soup.find_all(class_=tag_body)[0]

        # 标题加入到正文的最前面，居中显示
        center_tag = soup.new_tag("center")
        title_tag = soup.new_tag('h1')
        title_tag.string = title
        center_tag.insert(1, title_tag)
        body.insert(0, center_tag)
        html = str(body).replace('>', '>\n')

        pattern = "(<img .*?src=\")(.*?)(\")"

        # def func(m):
        #     rtn = m.group(1) + "https://www.liaoxuefeng.com" + m.group(2) + m.group(3)
            # rtn = m.group(1) + m.group(2) + m.group(3)
            # return rtn

        # html = re.compile(pattern).sub(func, html)

        html = html_template.format(content=html)

        filename = "output/" + str(title).replace('/', '_') + ".html"
        with open(filename, 'w') as f:
            f.write(html)

        time.sleep(1)

    except Exception as e:
        print(e)


def main():
    url = "https://www.baidu.com/home/news/data/newspage?nid=3124091726505125447&n_type=0&p_from=1&dtype=-1"
    tag_title = "article-title"
    tag_body = "article-content"

    single_url_to_html(url, tag_title, tag_body)
        
if __name__ == '__main__':
    main()
