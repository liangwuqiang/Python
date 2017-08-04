#!/usr/bin/env python
# coding:utf-8

from Tkinter import *


class Application(Frame):  # 新建一个程序类,继承于Frame

    @staticmethod
    def say_hi():  # 定义一个打招呼的方法
        print "hi there, everyone!"

    def createWidgets(self):  # 创建组件的方法
        btnquit = Button(self)  # 类属性应该在构造方法中定义,这里定义了一个退出按钮
        btnquit["text"] = "退出"  # 按钮上显示的文字
        btnquit["fg"] = "red"  # 按钮的前景色,即文字的颜色
        btnquit["command"] = self.quit  # 这里是调用的父类的方法,由于是command,这里不用写()

        btnquit.pack({"side": "left"})  # 对按钮进行包装,左边对齐,应该也可以使用上面的方法来定义
        # self.btnquit.pack["side"] = "left"  # TypeError: 'instancemethod' object does not support item assignment

        # 这里为什么不直接使用局部变量呢?
        self.hi_there = Button(self)  # 创建的另一个按钮
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):  # 怎么把构造方法写在后面了,在这里参数会传入Tk类
        Frame.__init__(self, master)  # 通过传入的Tk类来初始化父类的构造方法
        self.pack()  # 对Frame执行pack()操作
        self.createWidgets()  # 用于创建其它组件

root = Tk()  # 实例化Tk,以便在自己的应用中调用
app = Application(master=root)  # 实例化自定义的类,传入实例化的Tk类
app.mainloop()  # 程序进入主循环状态
# root.destroy()
