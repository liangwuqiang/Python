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

##
【正则基础之——捕获组（capture group）】
http://blog.csdn.net/lxcnn/article/details/4146148

【Python正则之(?P=name)匹配前面已命名的组】
http://www.crifan.com/detailed_explanation_about_python_regular_express_match_named_group/

【Python正则之(?P<name>…)带命名的组】
http://www.crifan.com/detailed_explanation_about_python_regular_express_named_group/


re.sub()中后续通过\g<name>方式被引用。

u'.+?<a href="/tag/(?P<tagName>.+?)/">(?P=tagName)</a>'
u'所捕获的tag值为：\g<tagName>'

### http://www.jb51.net/article/50511.htm

re.M
re.MULTILINE
影响'^'和'$'的行为，指定了以后，'^'会增加匹配每行的开始（也就是换行符后的位置）；'$'会增加匹配每行的结束（也就是换行符前的位置）。

re.S
re.DOTALL
影响'.'的行为，平时'.'匹配除换行符以外的所有字符，指定了本标志以后，也可以匹配换行符。

##3

for key, value in dict.items():

