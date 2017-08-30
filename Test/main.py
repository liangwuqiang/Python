"""
下载单独一个网页,需要指定url,标题和内容的class标签名

使用方法:
修改main中的实参,运行
测试成功
"""
from urllib import request
from bs4 import BeautifulSoup
import re
import os


class WebPageDownload:
    """ 网页下载, 只截取标题,内容及内容中所包含的图片 """

    def __init__(self, url, title_key, content_key):
        self.url = url
        self.titleKey = title_key
        self.contentKey = content_key
        self.title = ''
        self.content = ''

    def url_to_html(self):
        """ 通过url取得网页 """
        req = request.Request(self.url)
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        return html

    def extract_from_soup(self, html):
        """ 提取标题和文章内容 """
        soup = BeautifulSoup(html, 'html.parser')
        self.title = soup.select(self.titleKey)[0].text.strip()
        print(self.title)
        self.content = soup.select(self.contentKey)[0]
        print(self.content)

    @staticmethod
    def md5(string):
        """ 将字符串转成哈希码 """
        import hashlib
        if not isinstance(string, str):
            string = str(string)
        md5 = hashlib.md5()
        md5.update(string.encode('utf-8'))
        return md5.hexdigest()

    def download_images(self):
        """ 下载文章中的图片 """
        content = str(self.content)
        pattern = '<img .*?src=\"(.*?)\"'
        re_image = re.compile(pattern)
        for imageUrl in re_image.findall(content):
            if not os.path.exists('images'):
                os.mkdir('images')
            filename = 'images/' + self.md5(imageUrl) + os.path.splitext(imageUrl)[-1]
            try:
                request.urlretrieve(imageUrl, filename)
            except Exception as e:
                print('图片出错', e)
            else:
                content = content.replace(imageUrl, filename)
        self.content = content

    def ouput_html(self):
        """ 输出html文件 """
        html_template = """<!DOCTYPE html>
            <html><head><meta charset="UTF-8">
            </head><body>
            <p><a href="{origin}">原文链接</a></p>
            <p><center><h1>{title}</h1></center></p>
                {content}
            </body></html>"""
        html = html_template.format(origin=self.url, title=self.title, content=self.content)
        filename = str(self.title) + ".html"
        with open(filename, "w") as f:
            f.write(html)

    def run(self):
        """ 跑起来 """
        html = self.url_to_html()
        self.extract_from_soup(html)
        self.download_images()
        self.ouput_html()


def main():
    """ 主函数 """
    # """ 编程派网址 (测试通过)"""
    # url = 'http://www.codingpy.com/article/getting-started-with-jupyter-notebook-part-2/'
    # title_key = '.header h1'
    # content_key = '.article-content'
    # """ IBM """
    # url = r"https://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/"
    # title_key = '.ibm-h1'
    # content_key = ".ibm-col-6-4"
    # """ 伯乐在线 (测试通过)"""
    # url = r"http://python.jobbole.com/86405/"
    # title_key = '.entry-header'
    # content_key = ".entry"
    # """ CSDN博客 (测试通过)"""
    # url = r"http://blog.csdn.net/pleasecallmewhy/article/details/24021695"
    # title_key = '.article_title'
    # content_key = ".article_content"

    """ 其它 """

    """ =============================================== """
    download = WebPageDownload(url, title_key, content_key)
    download.run()

if __name__ == '__main__':
    main()
