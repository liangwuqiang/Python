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