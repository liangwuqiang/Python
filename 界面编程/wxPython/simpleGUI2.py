#!/usr/bin/python
#coding:utf-8
  
import wx


def main():
    app = wx.App()
    win = wx.Frame(None)
    win.Show()
    app.MainLoop()
  
if __name__ == '__main__':
    main()

# 这便是一个最简单的可视化窗口的实现
"""
# 基本的wxPython程序说明了开发任一wxPython程序所必须的五个基本步骤：
# 1.导入必须的wxPython包
# 2.子类化wxPython应用程序类
# 3.定义一个应用程序的初始化方法
# 4.创建一个应用程序类的实例
# 5.进入这个应用程序的主事件循环

import wx
class App(wx.App):
    def OnInit(self):
        frame=wx.Frame(parent=None,title='MyFirstWxPythonApplication')
        frame.Show()
        return True
app=App()
app.MainLoop()
"""
