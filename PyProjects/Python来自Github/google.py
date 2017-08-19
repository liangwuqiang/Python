#!/usr/bin/env python
# -*- coding: utf-8 -*-
#---------------------
# 不会在python3下安装pyperclip，先用python2.7测试

"""
作者: Ankit Agarwal (ankit167)
用法: python google.py <keyword>
说明: Script googles the keyword and opens
     top 5 (max) search results in separate
     tabs in the browser
版本: 1.0
"""

import webbrowser, sys, pyperclip, requests, bs4

def main():
	if len(sys.argv) > 1:
		keyword = ' '.join(sys.argv[1:])	#提取命令行参数py
	else:
		keyword = pyperclip.paste()	#使用pyperclip读写剪贴板作为参数

	keyword = "?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=python&rsv_pq=9f86ce190007d135&rsv_t=f24dUvPK443Fa4DyNruraF2DaaQZxxUdjpdWP4%2Fn5cXcE6R7it4kNgz9fZk&rqlang=cn&rsv_enter=1&rsv_sug3=5&rsv_sug1=5&rsv_sug7=100"
#	res=requests.get('http://google.com/search?q='+	keyword)
	res=requests.get("https://www.baidu.com/s"+	keyword)	#发出请求，获得一个相应结果
	print(res.url)
	res.raise_for_status()
	#soup = bs4.BeautifulSoup(res.text)
	#linkElems = soup.select('.r a')
	#numOpen = min(5, len(linkElems))

	#for i in range(numOpen):
		# webbrowser.open('http://google.com' + linkElems[i].get('href'))

if __name__ == '__main__':
	main()
