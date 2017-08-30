#!/usr/bin/env python
# -*- coding: utf-8 -*-
#文件前面添加以上两句，就可以输出中文字符

"""
调用方法 python 文件名 文件目录 .旧扩展名 .新扩展名
1.截取命令行参数
2.文件改名，遍历目录中的文件，splitext分开文件名和扩展名，list将文件名拆分为单独字母，替换掉最后的部分，join重新组合。

"""


# batch_file_rename.py
# Created: 6th August 2012

'''
批量重命名一组指定目录的文件 This will batch rename a group of files in a given directory,
一旦通过当前和新的扩展名 once you pass the current and new extensions
'''

__author__  = 'Craig Richards'
__version__ = '1.0'

import os
import sys
import argparse

def batch_rename(work_dir, old_ext, new_ext):
    '''
    批量重命名一组指定目录的文件，
    once you pass the current and new extensions
    '''
    # files = os.listdir(work_dir)

    # os.listdir(work_dir)
    # ['dgdf.old', 'abc.lwq']
    for filename in os.listdir(work_dir):   # 遍历指定目录中的文件

        # Get the file extension 给出文件扩展名
        # os.path.splitext(filename)
        # ('dgdf', '.old')
        # os.path.splitext(filename)[1]
        # .lql
        file_ext = os.path.splitext(filename)[1]   # 提取文件扩展名，分离出来的扩展名是带点.的
        # splitext 将文件名与扩展名分开，即使文件名中带有.分隔符 如：dsf.sfds.dsf

        if old_ext == file_ext:  # 判断是否是要改动的扩展名
            # Returns changed name of the file with new extention
            name_list=list(filename)     # 拆分文件名为字母列表
            # ['d', 'g', 'd', 'f', '.', 'o', 'l', 'd']

            name_list[len(name_list)-len(old_ext):]=list(new_ext)  # 进行替换
            # name_list[8-4:]=list(new_ext)

            newfile=''.join(name_list)   # 字母重新组合
            # newfile
            # dgdf.new

            # 写到文件中
            os.rename(   #调用系统的rename命令  旧文件名 新文件名
                os.path.join(work_dir, filename),   #文件路径的表示法
                os.path.join(work_dir, newfile)
            )

def get_parser():
    parser = argparse.ArgumentParser(description='在工作目录中改变文件扩展名')
    # argparse是python用于解析命令行参数和选项的标准模块
    parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1, help='要改变扩展名的目录')
    parser.add_argument('old_ext', metavar='OLD_EXT', type=str, nargs=1, help='原扩展名')
    parser.add_argument('new_ext', metavar='NEW_EXT', type=str, nargs=1, help='新扩展名')
    return parser

""" 带参数-h的运行结果：
/usr/bin/python2.7 /home/lwq/PyProjects/Python/batch_file_rename.py -h
usage: batch_file_rename.py [-h] WORK_DIR OLD_EXT NEW_EXT

在工作目录中改变文件扩展名

positional arguments:
  WORK_DIR    要改变扩展名的目录
  OLD_EXT     原扩展名
  NEW_EXT     新扩展名

optional arguments:
  -h, --help  show this help message and exit

Process finished with exit code 0
"""

def main():
    '''
    直接调用该脚本文件就会执行该函数
    '''
    # 添加命令行参数说明
    parser = get_parser()
    # parser
    #　ArgumentParser(prog='batch_file_rename.py', usage=None,
    # description='在工作目录中改变文件扩展名',
    # version=None, formatter_class=<class 'argparse.HelpFormatter'>,
    # conflict_handler='error', add_help=True)
    args = vars(parser.parse_args())
    # parser.parse_args()
    # Namespace(new_ext=['new'], old_ext=['old'], work_dir=['dir'])
    # args
    # {'old_ext': ['old'], 'new_ext': ['new'], 'work_dir': ['dir']}

    # 设置变量work_dir为第一个传递参数
    work_dir = args['work_dir'][0]     # 取到命令行的参数
    #['dir']　=> dir

    # 设置变量old_ext为第二个传递参数
    old_ext = args['old_ext'][0]

    # 设置变量new_ext为第三个传递参数
    new_ext = args['new_ext'][0]

    batch_rename(work_dir, old_ext, new_ext)


if __name__ == '__main__':  # 直接调用该文件时执行main函数
    main()

"""
argparse模块

一、简介：
argparse模块的作用是用于解析命令行参数，
例如python parseTest.py input.txt output.txt --user=name --port=8080。

二、使用步骤：
1：import argparse                       #导入该模块
2：parser = argparse.ArgumentParser()    #创建一个解析对象
3：parser.add_argument()                 #向该对象中添加你要关注的命令行参数和选项
4：parser.parse_args()                   #调用parse_args()方法进行解析
"""