# coding=utf-8
import re

regular = r'#.*?coding.*?utf-8.*'
re_utf = re.compile(regular)
content = ' # -*- coding: utf-8 -*-'

a = re_utf.match(content)
if a:
    print(a)
    print('ok')
