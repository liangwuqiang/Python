#!/usr/bin/env python
# coding=utf-8

"""
    窗口屏幕居中,设置窗口最大,最小尺寸...
    版权所有 2014 yao_yu (http://blog.csdn.net/yao_yu_126)
    本代码以MIT许可协议发布
    2014-04-15  创建
"""

import Tkinter as tK


def get_screen_size(window):
    return window.winfo_screenwidth(), window.winfo_screenheight()  # 返回的是屏幕尺寸


def get_window_size(window):
    """Return requested width of this widget."""
    return window.winfo_reqwidth(), window.winfo_reqheight()  # 这个返回的是什么值呢


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    print(size)
    root.geometry(size)


root = tK.Tk()
root.title('测试窗口')
center_window(root, 300, 640)
root.maxsize(600, 400)
root.minsize(300, 240)
tK.Label(root, relief=tK.FLAT, text='屏幕大小(%sx%s)\n窗口大小(%sx%s)'
                                    % (get_screen_size(root) + get_window_size(root))).pack(expand=tK.YES)
tK.mainloop()
