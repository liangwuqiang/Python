#!/usr/bin/env python
# -*- coding: utf-8 -*-
#文件前面添加以上两句，就可以输出中文字符


# 脚本名称      		: dir_test.py
# 作者				: Craig Richards
# 创建时间			: 29th November 2011
# 最后的修改     		:
# 版本				: 1.0
# 修改        		:

# 描述    			: 测试一下目录是否已存在，如果没有就创建目录

from __future__ import print_function   #在print()这行里使用
import os  # 与操作系统之间进行交互，这里用于判断目录是否存在，建立目录
import sys  # 与python解释器之间的交互，这里用于提取解释器版本信息


def main():
    if sys.version_info.major >= 3: # interpreter 解释者
        input_func = input          # 由用户进行输入 2与3之间的区别
    else:
        input_func = raw_input

    CheckDir = input_func("输入目录名称: ")   #给用户输入的内容指定一个名字
    print()  # python2中输出(),Python3输出为空行

    if os.path.exists(CheckDir):  # 目录是否已存在
        print("目录已存在")
    else:
        print("没有发现目录 " + CheckDir)  # 提示说明
        print() # python2中输出(),Python3输出为空行
        os.makedirs(CheckDir)  # 创建目录 mkdir、makedirs
        print("创建目录 " + CheckDir)


if __name__ == '__main__':  # 当直接调用给文件时，name是main。由别的文件import引用时，name是该文件名dir_test.py
    main()     # 直接调用该文件时，可运行这里的内容
