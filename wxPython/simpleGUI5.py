#!/usr/bin/python
#coding:utf-8
  
import wx
  
def openfile(evt):
  filepath = text_filename.GetValue()
  fopen = file(filepath)
  fcontent = fopen.read()
  text_contents.SetValue(fcontent)
  fopen.close()
  
def savefile(evt):
  filepath = text_filename.GetValue()
  filecontents = text_contents.GetValue()
  fopen = file(filepath,'w')
  fopen.write(filecontents)
  fopen.close()
  
app = wx.App()
#创建Frame
win = wx.Frame(None,title='NotePad',size=(440,320))
#创建Panel
panel = wx.Panel(win)
#创建open，save按钮
bt_open = wx.Button(panel,label='open')
bt_open.Bind(wx.EVT_BUTTON,openfile) #添加open按钮事件绑定，openfile()函数处理
bt_save = wx.Button(panel,label='save')
bt_save.Bind(wx.EVT_BUTTON,savefile) #添加save按钮事件绑定，savefile()函数处理
#创建文本框，文本域
text_filename = wx.TextCtrl(panel)
text_contents = wx.TextCtrl(panel,style=wx.TE_MULTILINE|wx.HSCROLL)
#添加布局管理器
bsizer_top = wx.BoxSizer()
bsizer_top.Add(text_filename,proportion=1,flag=wx.EXPAND,border=5)
bsizer_top.Add(bt_open,proportion=0,flag=wx.LEFT,border=5)
bsizer_top.Add(bt_save,proportion=0,flag=wx.LEFT,border=5)
  
bsizer_all = wx.BoxSizer(wx.VERTICAL)
bsizer_all.Add(bsizer_top,proportion=0,flag=wx.EXPAND|wx.LEFT,border=5)
bsizer_all.Add(text_contents,proportion=1,flag=wx.EXPAND|wx.ALL,border=5)
  
panel.SetSizer(bsizer_all)
  
win.Show()
app.MainLoop()
                             #47,0-1    Bot
  
#######################################################
#   打开，保存功能基本实现，但还存在很多bug。    #
#   怎么也算自己的第二个Python小程序吧！！     #  
###########################################################################
