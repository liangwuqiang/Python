# coding=utf-8
"""
用于文本文件的翻译,运行正常
"""
import re
import json
from urllib import quote
from urllib2 import urlopen

# regular = '.*?[\.\?](?=\s+(?:[A-Z]|$))'  # 匹配句子
regular = '[^ A-Za-z0-9,.?:@\-\n]'
re_program = re.compile(regular)


def translate(message):
    api = 'http://fanyi.youdao.com/openapi.do' \
          '?keyfrom=wufeifei&key=716426270&type=data&doctype=json&version=1.1&q='
    api = api + quote(message.encode('utf-8'))
    content = urlopen(api).read()
    content = json.loads(content.decode('utf-8'))
    return content['translation'][0]

with open('temp.txt', 'w') as f:
    f.write('')

with open('/home/lwq/Python/MyDict/scrapy/README.rst') as f_in:
    for line in f_in.readlines():
        with open('temp.txt', 'a') as f_out:
            f_out.write(line)
            if len(re_program.findall(line)) == 0 \
                    and len(re.findall(' ', line.strip())) > 2:
                newline = translate(line).encode('utf-8') + '\n'
                print(newline)
                f_out.write(newline)

    pass
