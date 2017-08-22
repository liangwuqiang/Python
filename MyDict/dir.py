# coding=utf-8

import os.path
rootdir = '/home/lwq/Python/MyDict'  # 指明被遍历的文件夹

index = 0
for parent, dirnames, filenames in os.walk(rootdir):    # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    # for dirname in dirnames:                       # 输出文件夹信息
    #     print "父目录: " + parent
    #     print "目录名: " + dirname
    #

    for filename in filenames:                        # 输出文件信息
        # print "父目录: " + parent
        # print "文件名: " + filename
        # print "文件全名: " + os.path.join(parent, filename) #输出文件路径信
        # -------------------------------------------------
        full_filename = os.path.join(parent, filename)
        file_ext = os.path.splitext(full_filename)[1]
        if file_ext == '.rst':
            print(full_filename)
            index += 1
        # print(full_filename)
print('共有文件个数: ', str(index))
