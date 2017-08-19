#!/usr/bin/env python
# coding:utf-8

"""Hello, wxPython! program."""

import wx


class Frame(wx.Frame):  # 自定义一个框架类
    """Frame class that displays an image. 显示一个图像的框架类"""

    def __init__(self, image, parent=None, id=-1,
                 pos=wx.DefaultPosition, title='Hello, wxPython!'):
        """Create a Frame instance and display image. 创建框架实例,显示图像"""
        temp = image.ConvertToBitmap()  # 将jpg图像转换成位图
        size = temp.GetWidth(), temp.GetHeight()  # 尺寸,这里定义为tuple,从图像中获取
        wx.Frame.__init__(self, parent, id, title, pos, size)  # 用图像尺寸来初始化父类
        self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)  # 设置本类的属性,这里通过wx中的静态位图类来取值
        self.SetClientSize(size)  # 设置客户端尺寸,这个是干啥用的, 方法?没定义,父类的方法?


class App(wx.App):
    """Application class.应用类"""

    def OnInit(self):  # 这个函数在什么时候会调用呢?
        image = wx.Image('wxPython.jpg', wx.BITMAP_TYPE_JPEG)  # 实例化一个图像
        self.frame = Frame(image)  # 初始化一个框架实例,这里是自定义的框架
        self.frame.Show()  # 把框架呈现出来
        self.SetTopWindow(self.frame)  # 将该框架设置为顶层窗口
        return True


def main():
    app = App()  # 通过自定义的类来实例化一个wx.App
    app.MainLoop()  # 程序进入主循环

if __name__ == '__main__':
    main()  # 直接调用main函数,也有直接将main内容放顶层,我觉得这样不太好
