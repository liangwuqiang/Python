# coding=utf-8
from urllib import request
import time

start = time.time()
# url = "http://blog.csdn.net/tangxl2008008/article/category/6340008"
url = "http://blog.csdn.net/tangxl2008008/article/category/6340008/2"
req = request.Request(url)
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
response = request.urlopen(req)
html = response.read().decode("utf-8")

with open("temp1.html", "w") as f:
    f.write(html)
print("用时:", time.time()-start)
