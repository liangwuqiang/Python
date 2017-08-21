# 学习
# 1.判断解释器版本，提高兼容性
# 2.系统命令的使用exists、makedirs

from __future__ import print_function   
import os  
import sys  


def main():
    if sys.version_info.major >= 3:     #根据解释器版本选择输入命令
        input_func = input          
    else:
        input_func = raw_input

    CheckDir = input_func("输入目录名称: ")   #用户输入
    print() #空行输出

    if os.path.exists(CheckDir):    #系统命令exists
        print("目录已存在")
    else:
        print("不存在目录：" + CheckDir)
        print() 
        os.makedirs(CheckDir)   #系统命令makedirs
        print("创建目录：" + CheckDir)


if __name__ == '__main__':  
    main()     
