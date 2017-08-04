#!/usr/bin/env python
# coding:utf-8

from Tkinter import *


class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        self.entrythingy = Entry()  # 定义的输入框
        self.entrythingy.pack()

        # here is the application variable 这是应用程序变量
        self.contents = StringVar()
        # set it to some value 给它赋值
        self.contents.set("this is a variable")
        # tell the entry widget to watch this variable 将输入框设为这个变量
        self.entrythingy["textvariable"] = self.contents

        # and here we get a callback when the user hits return.
        # 当用户从输入中返回时.我们给出一个回调方法.
        # we will have the program print out the value of the
        # 我们使程序打印出那个值
        # application variable when the user hits return
        # 应用程序的变量,当用户在输入中返回时
        self.entrythingy.bind('<Key-Return>',  # 文本框绑定特定的方法
                              self.print_contents)

    def print_contents(self, event):  # 定义的类方法,是对文本框内容发生变化后做出响应
        print "hi. contents of entry is now ---->", \
              self.contents.get()

root = Tk()
app = App(master=root)
app.mainloop()
