# 学习
# 1.提取命令行参数
# 2.子进程调用call

import subprocess
import sys

video_link, threads = sys.argv[1], sys.argv[2]  #提取命令行参数
subprocess.call([   #子进程调用call,不需要交互，Popen可交互
    "youtube-dl",
    video_link,
    "--external-downloader",
    "aria2c",
    "--external-downloader-args",
    "-x"+threads
])
