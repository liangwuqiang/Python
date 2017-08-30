# 在home目录中创建新目录
# 学习：
# 1.系统命令expanduser、exists、makedirs
# 2.错误处理方法

import os		
MESSAGE = '目录已存在'   #用变量存储字符串，有利于维护
TESTDIR = '测试目录'
try:    #使用错误处理方法
    home = os.path.expanduser("~")  #有则转，无则创建目录
    print(home)                             
    
    if not os.path.exists(os.path.join(home, TESTDIR)):     #目录是否已存在
        os.makedirs(os.path.join(home, TESTDIR))    #创建目录
    else:
        print(MESSAGE)
except Exception as e:  #错误响应
    print(e)
    
