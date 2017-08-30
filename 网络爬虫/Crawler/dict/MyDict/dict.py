#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys
import json
import re

try:

    from urllib.request import urlopen
    from urllib.parse import quote
except ImportError:

    from urllib2 import urlopen
    from urllib import quote


class Dict:
    key = '716426270'
    keyFrom = 'wufeifei'
    api = 'http://fanyi.youdao.com/openapi.do' \
          '?keyfrom=wufeifei&key=716426270&type=data&doctype=json&version=1.1&q='
    content = None

    def __init__(self, argv):
        print('ok')
        message = ''
        if len(argv) > 0:
            for s in argv:
                message = message + s + ' '
            self.api = self.api + quote(message.encode('utf-8'))
            self.translate()
        else:
            print('Usage: dict test')

    def translate(self):
        try:
            content = urlopen(self.api).read()

            self.content = json.loads(content.decode('utf-8'))
            self.parse()
        except Exception as e:
            print('ERROR: Network or remote service error!')
            print(e)

    def parse(self):
        code = self.content['errorCode']
        if code == 0:
            c = None
            try:
                u = self.content['basic']['us-phonetic']
                e = self.content['basic']['uk-phonetic']
            except KeyError:
                try:
                    c = self.content['basic']['phonetic']
                except KeyError:
                    c = 'None'
                u = 'None'
                e = 'None'

            try:
                explains = self.content['basic']['explains']
            except KeyError:
                explains = 'None'

            try:
                phrase = self.content['web']
            except KeyError:
                phrase = 'None'

            print('\033[1;31m################################### \033[0m')

            print('\033[1;31m# \033[0m {0} {1}'.format(
                self.content['query'], self.content['translation'][0]))
            if u != 'None':
                print('\033[1;31m# \033[0m (U: {0} E: {1})'.format(u, e))
            elif c != 'None':
                print('\033[1;31m# \033[0m (Pinyin: {0})'.format(c))
            else:
                print('\033[1;31m# \033[0m')

            print('\033[1;31m# \033[0m')

            if explains != 'None':
                for i in range(0, len(explains)):
                    print('\033[1;31m# \033[0m {0}'.format(explains[i]))
            else:
                print('\033[1;31m# \033[0m Explains None')


            if phrase != 'None':
                for p in phrase:
                    print('\033[1;31m# \033[0m {0} : {1}'.format(
                        p['key'], p['value'][0]))


                    if len(p['value']) > 0:
                        if re.match('[\u4e00-\u9fa5]+', p['key']) is None:

                            blank = len(p['key'])
                        else:
                            blank = len(p['key'].encode('gbk'))
                        for i in p['value'][1:]:
                            print('\033[1;31m# \033[0m {0} {1}'.format(
                                ' ' * (blank + 2), i))

            print('\033[1;31m################################### \033[0m')

        elif code == 20:
            print('WORD TO LONG')
        elif code == 30:
            print('TRANSLATE ERROR')
        elif code == 40:
            print('CAN\'T SUPPORT THIS LANGUAGE')
        elif code == 50:
            print('KEY FAILED')
        elif code == 60:
            print('DO\'T HAVE THIS WORD')


def main():
    Dict(sys.argv[1:])

if __name__ == '__main__':
    main()
