# coding=utf-8
from urllib import request
# import requests
from bs4 import BeautifulSoup
import hashlib
import re
import os

"""--------------------IBM--------------------"""
URL = r"https://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/"
TAG_TITLE = 'ibm-h1'
TAG_CONTENT = "ibm-columns dw-article-topbar"
"""----------------------------------------"""
html_template = """
<!DOCTYPE html>
<html lang="en"><head>
    <meta charset="UTF-8">
</head><body>

    {content}

</body></html>
"""
req = request.Request(URL)
html = request.urlopen(req).read().decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')
title = soup.find(class_=TAG_TITLE).get_text()
title = ''.join(title.split())
content = soup.find(class_=TAG_CONTENT)

center_tag = soup.new_tag("center")
title_tag = soup.new_tag('h1')
title_tag.string = title
center_tag.insert(1, title_tag)
content.insert(0, center_tag)
content.insert(0, "\n")
html = str(content)

md5 = hashlib.md5()
pattern = '<img .*?src=\"(.*?)\"'
if not os.path.exists("images"):
    os.mkdir("images")

for url in re.compile(pattern).findall(html):
    print(url, type(url))
    md5.update(url.encode("utf-8"))
    filename = "images/" + md5.hexdigest() + os.path.splitext(url)[1]
    print(filename)
    try:
        request.urlretrieve(url, filename)
    except Exception as e:
        print("图片生成出错", e)
    html = html.replace(url, filename)

""" html合成 """
html = html_template.format(content=html)

""" 文件输出 """
filename = str(title) + ".html"
with open(filename, "w") as f:
    f.write(html)
