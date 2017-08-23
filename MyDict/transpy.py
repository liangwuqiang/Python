# coding=utf-8
"""
将一个目录下的所有.py文件中的注释部分添加中文注释
使用: 修改目录变量rootdir
"""
import os
import logging
import time
from urllib.request import quote, urlopen
import json
import re

rootdir = '/home/lwq/Python/MyDict/test/lwq'
regular = r'# (.*)'
re_comment = re.compile(regular)
regular = r'"""(.*?)"""'
re_oneline = re.compile(regular)
regular = r'(.*?)"""(.*)'
re_explain = re.compile(regular)


def translate(message):
    return '(翻译略)'
    api = 'http://fanyi.youdao.com/openapi.do' \
          '?keyfrom=wufeifei&key=716426270&type=data&doctype=json&version=1.1&q='
    # api = api + quote(message.encode('utf-8'))
    api = api + quote(message)
    # print(api, type(api))
    try:
        content = urlopen(api).read()
        content = json.loads(content.decode('utf-8'))
    except Exception as e:
        print('出错: ', e)
        return ''
    else:
        time.sleep(1)
        return content['translation'][0]


def deal(line, message):
    if not line.rstrip():
        return line
    message = translate(message)
    line = line.rstrip() + ' #--> ' + message + '\n'
    # logging.debug(line)
    return line


def handle(lines):
    content = []
    tag = [False]
    for line in lines:
        newline = line
        if not newline:
            newline = '\n'
        elif re_comment.findall(line):
            message = re_comment.search(line).group(1).strip()
            newline = deal(line, message)
            print(newline.rstrip())
        elif re_oneline.findall(line):
            message = re_oneline.search(line).group(1).strip()
            newline = deal(line, message)
            # print(newline.rstrip())
        elif tag[0] is True and line.find('"""') == -1:
            message = line.strip()
            newline = deal(line, message)
            # print(newline.rstrip())
        elif len(re_explain.findall(line)) == 1:
            if tag[0] is False:
                tag[0] = True
                message = re_explain.search(line).group(2).strip()  # 右边部分
                if message:
                    newline = deal(line, message)
                # print(newline.rstrip())
            else:
                tag[0] = False
                message = re_explain.search(line).group(1).strip()  # 左边部分
                if message:
                    newline = deal(line, message)
                # print(newline.rstrip())
        content.append(newline)
    return ''.join(content)


def openfile(path):
    try:
        with open(path) as f:
            lines = f.readlines()
    except Exception as e:
        message = path + '\n' + str(e)
        logging.error(message)
    else:
        return lines


def main():
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            path = os.path.join(parent, filename)
            ext = os.path.splitext(path)[-1]
            if ext == '.py':
                lines = openfile(path) if openfile(path) else ''
                if len(lines) > 0:
                    content = handle(lines)
                    filename = os.path.splitext(path)[0] + '_new.txt'
                    with open(filename, 'w') as f:
                        f.write(content)
            # time.sleep(1)


if __name__ == '__main__':
    main()
