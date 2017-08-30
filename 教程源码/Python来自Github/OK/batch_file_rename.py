# 用法：
# python3 该文件名.py 目录名 .原扩展名 .新扩展名
# 学习：
# 1.构造和提取命令行参数
# 2.针对文件的操作（分离扩展名splitext，分离成字母表list，然后替换，合并join）
# 3.系统命令rename、join

import os
import argparse

def batch_rename(work_dir, old_ext, new_ext):
    for filename in os.listdir(work_dir):   #遍历目录中的文件
        file_ext = os.path.splitext(filename)[1]    #提取扩展名
        if old_ext == file_ext: #扩展名对比
            name_list=list(filename)    #文件名拆散成字母表
            name_list[len(name_list)-len(old_ext):]=list(new_ext)   #替换最后的部分
            newfile=''.join(name_list)  #字母表重新连接成文件名
            os.rename(  #文件改名
                os.path.join(work_dir, filename),   #文件路径由目录连接文件名组成
                os.path.join(work_dir, newfile)
            )

def get_parser():
    parser = argparse.ArgumentParser(description='改变目录中文件的扩展名') #构造命令行参数和选项
    parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1, help='目录名')
    parser.add_argument('old_ext', metavar='OLD_EXT', type=str, nargs=1, help='原扩展名')
    parser.add_argument('new_ext', metavar='NEW_EXT', type=str, nargs=1, help='新扩展名')
    return parser   #构造了带三个参数的调用

def main():
    #调用argparse来构造命令行参数
    parser = get_parser()
    args = vars(parser.parse_args())

    #从命令行中提取的参数
    work_dir = args['work_dir'][0]
    old_ext = args['old_ext'][0]
    new_ext = args['new_ext'][0]

    #调用函数对文件重命名
    batch_rename(work_dir, old_ext, new_ext)

if __name__ == '__main__':
    main()

