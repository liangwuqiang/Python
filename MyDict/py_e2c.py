# coding=utf-8
"""
整个目录中的 *.py 文件
英文注释 ---> 添加中文注释

使用方法:
python3 py_e2c.py
测试成功
"""
import os
import logging
import time
from urllib.request import quote, urlopen
import json
import re

istest = True  # True / False 调试程序用

rootdir = '.'  # 当前目录, 可修改为特定目录

regular = r'# (.*)'
re_comment = re.compile(regular)
regular = r'"""(.*?)"""'
re_one_line = re.compile(regular)
regular = r'.*?"""(.*)'
re_multi_line_start = re.compile(regular)
regular = r'(.*?)""".*'
re_multi_line_end = re.compile(regular)
regular = r'(.*?)# >>'
re_translate = re.compile(regular)
regular = r':\s+#'
re_indent = re.compile(regular)
regular = r'(.*)'
re_whole_line = re.compile(regular)
regular = r'#.*?coding.*?utf-8.*'
re_utf_8 = re.compile(regular)


def translate(message):
    """ 翻译 """
    if istest is True:
        return '(翻译略, 修改istest变量可实现在线翻译)'
    else:
        api = 'http://fanyi.youdao.com/openapi.do' \
              '?keyfrom=wufeifei&key=716426270&type=data&doctype=json&version=1.1&q='
        api = api + quote(message)
        time.sleep(1)
        try:
            content = urlopen(api).read()
            content = json.loads(content.decode('utf-8'))
            return content['translation'][0]
        except Exception as e:
            print('出错: ', e)
            return ''


def handle_line(line, re_compile):
    """ 处理一行内容,参数:行,相应的正则表达方法 """
    newline = line
    comment_en = re_compile.search(line).group(1).strip()
    if comment_en.strip():
        comment_cn = translate(comment_en.strip())
        blank_num = re.search('["#\w]', line).span()[0]
        if re_indent.search(line):
            blank_num = blank_num + 4
        newline = line + ' ' * blank_num + '# >> ' + comment_cn + '\n'
    return newline


def handle_whole(lines):
    """整个文件进行逐行提取检验,需处理的交 handle_line() """
    content = []
    tag = [False]
    for line in lines:
        newline = line
        if not newline:  # 空行跳过
            newline = '\n'
        elif re_translate.search(line):  # 行中存在翻译,清除
            continue
        elif re_comment.search(line):  # 单行注释#的处理
            if not re_utf_8.match(line):
                newline = handle_line(line, re_comment)
                logging.info(newline)  # ok
        elif re_one_line.findall(line):  # 单行说明"""xxx"""的处理
            newline = handle_line(line, re_one_line)
            logging.info(newline)  # ok
        elif tag[0] is True and line.find('"""') == -1:  # 多行注释"""的处理
            newline = handle_line(line, re_whole_line)
            logging.info(newline)  # ok
        elif len(re_multi_line_start.findall(line)) == 1:  # 多行注释"""前后的处理
            if tag[0] is False:
                tag[0] = True
                newline = handle_line(line, re_multi_line_start)
                logging.info(newline)  # ok
            else:
                tag[0] = False
                newline = handle_line(line, re_multi_line_end)
                logging.info(newline)  # ok
        content.append(newline)
        print(newline)
    return ''.join(content)


def read_file(path):
    """打开文件,并检查,正常提交 handle_whole() """
    content = ''
    try:
        with open(path) as f:
            lines = f.readlines()
    except Exception as e:
        message = path + '\n' + str(e)
        logging.error(message)
        return []
    else:
        if len(lines) > 0:
            content = handle_whole(lines)
    return content


def main():
    """在目录中遍历文件,找到 *.py 文件交 handle_whole() """
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            path = os.path.join(parent, filename)
            ext = os.path.splitext(path)[-1]
            if ext == '.py' and filename != 'py_e2c.py':
                content = read_file(path)
                if content:
                    with open(path, 'w') as f:
                        f.write(content)
                logging.info('已完成: ' + path + '\n========================================')


def setter():
    """ 设置,日志输出控制 """
    logging.basicConfig(level=logging.INFO, format='%(message)s',
                        filename='py_e2c.log', filemode='w')

if __name__ == '__main__':
    setter()
    main()
