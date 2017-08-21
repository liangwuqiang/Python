# Script Name   : env_check.py
# Author        : Craig Richards
# Created       : 14th May 2012
# Last Modified	: 14 February 2016
# Version       : 1.0.1

# Modifications	: 1.0.1 - Tidy up comments and syntax

# Description   : 该脚本将检查是否所有我们需要的环境变量都被设置

import os

confdir = os.getenv("my_config")  # 设置变量confdir来自系统环境变量
conffile = 'env_check.conf'                     # 设置变量conffile
conffilename = os.path.join(confdir, conffile)  # 设置变量conffilename，通过连接confdir和conffile
for env_check in open(conffilename):            # 打开配置文件，并读出所有设置
  env_check = env_check.strip()                 # 设置变量为它自己本身，但去掉多余的部分
  print '[{}]'.format(env_check)                # 格式化为方括号输出
  newenv = os.getenv(env_check)                 # Set the variable newenv to get the settings from the OS what is currently set for the settings out the configfile

  if newenv is None:                            # If it doesn't exist
    print env_check, 'is not set'               # Print it is not set
  else:                                         # Else if it does exist
    print 'Current Setting for {}={}\n'.format(env_check, newenv)	# Print out the details
