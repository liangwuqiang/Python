from urllib import request
from bs4 import BeautifulSoup
import time
import hashlib
import re

# 列出设置变量
url = r'http://blog.csdn.net//u013088062/article/details/50388329'  # 我的Pycharm，我做主
tag_title = 'article_title'
tag_content = 'article_content tracking-ad'

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

def url2list(url):
    """将网页内容导出为目录列表"""
    # req = request.Request(url)
    # req.add_header('User-Agent', "Mozilla/5.0 (X11; Ubuntu; Lin… Gecko/20100101 Firefox/54.0")
    # response = request.urlopen(req)
    # html = response.read().decode('utf-8')
    with open('test.html') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    # title = soup.find('article_title').get_text()
    # print(title)
    # print('---------------------------')
    hrefs = soup.find_all('a')
    for href in hrefs:
        # print(href.get('href'))
        url = href.get('href')
        response = request.urlopen(url)
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find(class_=tag_title).get_text().strip()
        content = soup.find(class_=tag_content)
        # 重新对内容布局
        center_tag = soup.new_tag("center")
        title_tag = soup.new_tag('h3')
        title_tag.string = title
        center_tag.insert(1, title_tag)
        content.insert(0, center_tag)
        html = str(content)

        md5 = hashlib.md5()
        pattern = "<img .*?src=\"(.*?)\""
        for url in re.compile(pattern).findall(html):
            md5.update(url.encode('utf-8'))
            filename = "images/" + md5.hexdigest() + ".png"
            html = html.replace(url, filename)
            request.urlretrieve(url, 'output/' + filename)

        html = html_template.format(content=html)  # 形成完整的html文件

        html = html_template.format(content=html)  # 形成完整的html文件

        # 文件输出
        filename = "output/" + str(title).replace('/', '_') + ".html"
        with open(filename, 'w') as f:
            f.write(html)

        time.sleep(10)

    # html = str(content)

    # html = html_template.format(content=html)
    # with open('test.html', 'w') as f:
    #     f.write(html)


def main():
    url2list(url)

if __name__ == '__main__':
    main()
