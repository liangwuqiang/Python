#!/usr/bin/env python
# coding:utf-8

from Tkinter import *


class App(Frame):
    pass


root = Tk()

myapp = App(master=root)
root.title("测试窗口")
width, height = 400, 400
root.geometry('%dx%d+%d+%d' % (width, height, (root.winfo_screenwidth()
              - width) / 2, (root.winfo_screenheight() - height) / 2))
#myapp.master.size(440, 400)

myapp.mainloop()
