# python2和python3的区别

## python2.7
import urllib2
filename = r'file:///home/ubuntu/Desktop/Python/temp.html'
response = urllib2.urlopen(filename)
html = response.read()
## python3.5
from urllib import request
filename = 'file://' + request.pathname2url(r'd:\windows\temp.html')
response = request.urlopen(filename)
html = response.read().decode('utf-8')

## 导入模块和引用模块的不同?
import os.path
for parent, dirnames, filenames in os.walk(rootdir):
所以直接使用import os就可? 反正在os.path中也得带os,不能单独使用path


