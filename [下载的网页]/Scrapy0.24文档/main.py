from urllib import request
from bs4 import BeautifulSoup
import time
import hashlib
import re
import os

# 设置变量,要根据实际情况改动
URL = r'http://crawler_scrapy-chs.readthedocs.io/zh_CN/0.24/index.html'  # Scrapy 0.24 文档
# URL = 
TAG_TITLE = ''
# TAG_CONTENT = 'wy-menu wy-menu-vertical'
TAG_CONTENT = "document"

html_template = """
<!DOCTYPE html>
<html lang="en"><head>
    <meta charset="UTF-8">
</head><body>

    {content}
    
</body></html>
"""


def download(url):
    """ 直接下载网页,保存到download.html """
    request.urlretrieve(url=url, filename="download.html")


def extract():
    """ 从下载的网页中提取有用部分,保存到extract.html """

    """ 打开html文件 """
    with open(file="download.html") as f:
        html = f.read()

    html = output(html)

    with open(file="extract.html", mode="w") as f:
        f.write(html)


def links():
    """ 从singlepage.html中单独提取要批量下载的URL,并存入links.txt """

    """ 打开extract.html文件 """
    with open(file="extract.html") as f:
        html = f.read()

    """ 提取目录列表 """
    soup = BeautifulSoup(markup=html, features="html.parser")
    items = soup.find_all(name="a")

    itemlist = []
    for item in items:
        itemlist.append("<p>" + str(item) + "</p>\n")
    content = "".join(itemlist)
    html = html_template.format(content=content)  # 形成完整的html文件

    """ 写入links.html文件 """
    with open("links.html", "w") as f:
        f.write(html)


def output(html, index=" "):
    """ 从html中提取数据,处理后输出到文件 """

    """ 根据传入的html,提取标题和内容数据 """
    soup = BeautifulSoup(html, 'html.parser')
    # title = soup.find(class_=TAG_TITLE).get_text()
    title = soup.find("h1").get_text()
    title = ''.join(title.split()).replace("¶", "")
    content = soup.find(class_=TAG_CONTENT)

    """ 内容重新布局 """
    center_tag = soup.new_tag("center")
    title_tag = soup.new_tag('h3')
    title_tag.string = title
    center_tag.insert(1, title_tag)
    content.insert(0, center_tag)
    content.insert(0, "\n")
    html = str(content).replace("¶", "")

    """ 处理图片链接,下载图片 """
    md5 = hashlib.md5()
    pattern = '<img .*?src=\"(.*?)\"'
    if not os.path.exists("images"):
            os.mkdir("images")

    for url in re.compile(pattern).findall(html):
        path = url.encode("utf-8")
        md5.update(path)
        ext = os.path.splitext(path)[1].decode("utf-8")
        if ext:
            filename = "images/" + md5.hexdigest() + ext
        else:
            filename = "images/" + md5.hexdigest() + ".jpg"
        try:
            request.urlretrieve(url, '' + filename)
        except Exception as e:
            print("图片生成出错", e)
        print(filename)
        html = html.replace(url, filename)

    """ html合成 """
    html = html_template.format(content=html)  # 形成完整的html文件

    """ 文件输出 """
    if str(title) != "":
        if index != " ":
            filename = str(index) + "." + str(title).replace("/", "_") + ".html"
        else:
            filename = "" + str(title).replace("/", "_") + ".html"

        with open(file=filename, mode="w") as f:
            f.write(html)

    return html


def output2(url, index):

    html = request.urlopen(url).read().decode('utf-8')
    output(html, index)
    print("完成:", str(index), "---" + url)

    # 延迟处理
    time.sleep(1)


def batch():
    """ 从links.html中提取URL,进行批量下载 """

    """ 打开links.html文件 """
    with open('links.html') as f:
        html = f.read()

    """" 提取超链接,将每个html提交output()处理 """
    soup = BeautifulSoup(html, 'html.parser')
    itemlist = soup.find_all('a')
    urllist = []
    for item in itemlist:
        urllist.append(os.path.split(URL)[0] + "/" + item.get("href"))

    # output2(urllist[0], 0)
    htmls = [output2(url, index) for index, url in enumerate(urllist)]
    return htmls


def main():
    # download(URL)  # 步骤1,根据URL,下载保存为download.html
    # extract()  # 步骤2,根据download.html,提取内容
    # links()  # 步骤3,根据extract.html,提取链接
    batch()  # 步骤4,根据links.html,批量下载

if __name__ == '__main__':
    main()
