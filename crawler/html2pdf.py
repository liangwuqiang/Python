# coding=utf-8
import pdfkit
"""
安装软件包:
pip install pdfkit

sudo apt-get install wkhtmltopdf  # ubuntu
"""

def html2pdf(html, file_name):
    """ 将html文件合成pdf文件 """
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
        'cookie': [
            ('cookie-name1', 'cookie-value1'),
            ('cookie-name2', 'cookie-value2'),
        ],
        'outline-depth': 10,
    }
    pdfkit.from_file(html, file_name, options=options)


def main():
    html = 'pdf.html'
    file_name = 'test.pdf'
    html2pdf(html, file_name)

if __name__ == '__main__':
    main()
