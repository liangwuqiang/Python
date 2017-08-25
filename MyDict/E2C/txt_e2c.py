import time
from urllib.request import quote, urlopen
import json

filename = './project_star.txt'


def translate(message):
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


def main():
    with open(filename) as fIn, open('temp.txt', 'w') as fOut:
        lines = fIn.readlines()
        for line in lines:
            newline = translate(line.strip())
            print(newline)
            fOut.write(line + newline + '\n\n')

if __name__ == '__main__':
    main()
