http://www.jb51.net/article/79670.htm

# 在Ubuntu系统下安装使用Python的GUI工具wxPython

这篇文章主要介绍了在Ubuntu系统下安装使用Python的GUI工具wxPython的方法,
wxPython可以为Python提供强大的图形化界面开发支持,需要的朋友可以参考下

## （一）wxpython的安装

    Ubuntu下的安装，还是比较简单的。
```bash	
#使用：apt-cache search wxpython 测试一下，可以看到相关信息
dizzy@dizzy-pc:~/Python$ apt-cache search wxpython
cain - simulations of chemical reactions
cain-examples - simulations of chemical reactions
cain-solvers - simulations of chemical reactions
gnumed-client - medical practice management - Client
...

#这样的话，直接使用： sudo apt-get install python-wxtools 即可安装
dizzy@dizzy-pc:~/Python$ sudo apt-get install python-wxtools
[sudo] password for dizzy: 
Reading package lists... Done
Building dependency tree 
...
```

测试是否安装成功。进入Python，import wx 不报错，即可

```bash
dizzy@dizzy-pc:~/Python$ python
Python 2.7.3 (default, Apr 20 2012, 22:44:07) 
[GCC 4.6.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import wx
>>>
```

## （二）显示出一个窗口

```pyhton
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
```

## （三）添加可视化组建及简单布局

```python
# coding:utf-8
  
import wx


def main():
    app = wx.App()
    win = wx.Frame(None, title='测试窗口NotePad', size=(880, 640))
    # 很明显，title就是标题，size就是大小
  
    bt_open = wx.Button(win, label='open', pos=(275, 2), size=(80, 30))
    bt_save = wx.Button(win, label='save', pos=(355, 2), size=(80, 30))
    # label就是按钮显示的标签，pos是控件左上角的相对位置，size就是控件的绝对大小
  
    text_title = wx.TextCtrl(win, pos=(5, 2), size=(265, 30))
    text_content = wx.TextCtrl(win, pos=(5, 34), size=(430, 276), style=wx.TE_MULTILINE|wx.HSCROLL)
    # style样式，wx.TE_MULTILINE使其能够多行输入，wx.HSCROOL使其具有水平滚动条
  
    win.Show()
    app.MainLoop()
  
if __name__ == '__main__':
    main()
  
# 做过桌面软件开发的，对这个肯定很熟悉。
# 由于之前学过一点VB，VC，Delphi等，学起来感觉很简单。
# 将wx提供的控件添加到某个Frame上，并进行各自的属性设置即可完成
# 由于文本控件的size属性，设置的为绝对值。这样就会有一些问题......
```

## （四）界面布局管理

    由于之前的控件直接绑定在Frame上，这样会有一些问题。下面将使用Panel面板进行管理。

```python	
# 当然，之前说将各种控件的位置都写成绝对位置和大小，会有一些问题。这是不对的
# 有时需要动态布局，而有时则需要静态布局
  
import wx
  
def main():
  #创建App
  app = wx.App()
  #创建Frame
  win = wx.Frame(None,title='NotePad',size=(440,320))
  win.Show()
  #创建Panel
  panel = wx.Panel(win)
  #创建open，save按钮
  bt_open = wx.Button(panel,label='open')
  bt_save = wx.Button(panel,label='save')
  #创建文本框，文本域
  text_filename = wx.TextCtrl(panel)
  text_contents = wx.TextCtrl(panel,style=wx.TE_MULTILINE|wx.HSCROLL)
  
  #添加布局管理器
  bsizer_top = wx.BoxSizer()
  bsizer_top.Add(text_filename,proportion=1,flag=wx.EXPAND)
  bsizer_top.Add(bt_open,proportion=0,flag=wx.LEFT,border=5)
  bsizer_top.Add(bt_save,proportion=0,flag=wx.LEFT,border=5)
  
  bsizer_all = wx.BoxSizer(wx.VERTICAL)
    #wx.VERTICAL 横向分割
  bsizer_all.Add(bsizer_top,proportion=0,flag=wx.EXPAND|wx.LEFT,border=5)
  bsizer_all.Add(text_contents,proportion=1,flag=wx.EXPAND|wx.ALL,border=5)
  
  panel.SetSizer(bsizer_all)
  
  app.MainLoop()
  
if __name__ == '__main__':
  main()
  
#这个是动态布局。当然这只是一个视图而已。
#这只是个表面而已，灵魂不在此！
```

## （五）添加控件的事件处理

    直接上代码。
```python
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
  
#######################################################
#   打开，保存功能基本实现，但还存在很多bug。    #
#   怎么也算自己的第二个Python小程序吧！！     #  
###########################################################################
```
## （六）ListCtrl列表控件的使用示例
ListCtrl这个控件比较强大，是我比较喜欢使用的控件之一。
下面是list_report.py中提供的简单用法：
```python
import wx
import sys, glob, random
import data
 
class DemoFrame(wx.Frame):
  def __init__(self):
    wx.Frame.__init__(self, None, -1,
             "wx.ListCtrl in wx.LC_REPORT mode",
             size=(600,400))
 
    il = wx.ImageList(16,16, True)
    for name in glob.glob("smicon??.png"):
      bmp = wx.Bitmap(name, wx.BITMAP_TYPE_PNG)
      il_max = il.Add(bmp)
    self.list = wx.ListCtrl(self, -1, style=wx.LC_REPORT)
    self.list.AssignImageList(il, wx.IMAGE_LIST_SMALL)
 
    # Add some columns
    for col, text in enumerate(data.columns):
      self.list.InsertColumn(col, text)
 
    # add the rows
    for item in data.rows:
      index = self.list.InsertStringItem(sys.maxint, item[0])
      for col, text in enumerate(item[1:]):
        self.list.SetStringItem(index, col+1, text)
 
      # give each item a random image
      img = random.randint(0, il_max)
      self.list.SetItemImage(index, img, img)
         
    # set the width of the columns in various ways
    self.list.SetColumnWidth(0, 120)
    self.list.SetColumnWidth(1, wx.LIST_AUTOSIZE)
    self.list.SetColumnWidth(2, wx.LIST_AUTOSIZE)
    self.list.SetColumnWidth(3, wx.LIST_AUTOSIZE_USEHEADER)
 
 
app = wx.PySimpleApp()
frame = DemoFrame()
frame.Show()
app.MainLoop()
```
 

如何获取选中的项目？
 最常用的方法就是获取选中的第一项：GetFirstSelected()，这个函数返回一个int，即ListCtrl中的项(Item)的ID。

 还有一个方法是：GetNextSelected(itemid)，获取指定的itemid之后的第一个被选中的项，同样也是返回itemid。

 通过这两个方法，我们就可以遍历所有选中的项了。
