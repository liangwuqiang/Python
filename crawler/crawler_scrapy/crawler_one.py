from urllib import request
from bs4 import BeautifulSoup
import time
import hashlib
import re
import os

"""设置变量,要根据实际情况改动"""
# """----------简书------------------"""
# URL = r"http://www.jianshu.com/p/a8aad3bf4dc4"
# TAG_TITLE = 'title'
# TAG_CONTENT = "show-content"
"""-----------伯乐在线-----------------"""
URL = r"http://python.jobbole.com/86405/"
TAG_TITLE = 'entry-header'
TAG_CONTENT = "entry"
"""-----------图灵社区-----------------"""
# URL = r"http://www.ituring.com.cn/article/114408"
# TAG_TITLE = ''
# TAG_TITLEH = 'h1'
# TAG_CONTENT = "markdown-body"

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
# if TAG_TITLE:
#     title = soup.find(class_=TAG_TITLE).get_text()
# elif TAG_TITLEH:
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
    # if url.startswith("http"):
    #     path = url.encode("utf-8")
    #     print("1")
    # else:
    #     path = "http://www.ituring.com.cn" + url
    #     print("2")
    path = url.encode('utf-8')
    md5.update(path)
    ext = os.path.splitext(path)[1].decode("utf-8")

    if ext == '.png' or ext == '.jpg':
        filename = "images/" + md5.hexdigest() + ext
    else:
        filename = "images/" + md5.hexdigest() + ".jpg"
    try:
        request.urlretrieve("http://www.ituring.com.cn" + url, '' + filename)
    except Exception as e:
        print("图片生成出错", e)
    # print(url)
    html = html.replace(url, filename)

""" html合成 """
html = html_template.format(content=html)  # 形成完整的html文件

""" 文件输出 """
filename = str(title) + ".html"
with open(filename, "w") as f:
    f.write(html)
