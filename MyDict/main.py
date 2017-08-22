import os.path
import re
from urllib.request import quote, urlopen
import json
import time

rootdir = '/home/lwq/Python/MyDict/test'

regular = '[^ A-Za-z0-9,.?:@\-\n\`\*]'
re_program = re.compile(regular)


def translate(message):
    print(message)
    api = 'http://fanyi.youdao.com/openapi.do' \
          '?keyfrom=wufeifei&key=716426270&type=data&doctype=json&version=1.1&q='
    api = api + quote(message.encode('utf-8'))
    try:
        content = urlopen(api).read()
        content = json.loads(content.decode('utf-8'))
        print(content['translation'][0])
        print()
        time.sleep(1)
        return content['translation'][0]
    except Exception as e:
        print('出错: ', e)
        return ''


def open_file(full_filename):
    index = 0
    with open(full_filename, 'r') as fr:
        length = len(fr.readlines())
        with open(full_filename + '_new', 'w') as fw:
            fw.write('')
        with open(full_filename + '_new', 'a') as fa:
            for line in fr.readlines():
                fa.write(line)
                if len(re.findall(' ', line.strip())) > 3:
                    newline = translate(line)
                    if newline != line:
                        newline = translate(line) + "\n\n"
                        fa.write('### ' + newline)
                print('进度:' + str(index) + ' / ' + str(length))
                index += 1
                # break


def main():
    index = 0
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            full_filename = os.path.join(parent, filename)
            file_ext = os.path.splitext(full_filename)[1]
            if file_ext == '.rst':
                open_file(full_filename)
                index += 1
                print('完成' + str(index) + ' ==> ' + full_filename)


if __name__ == '__main__':
    main()
