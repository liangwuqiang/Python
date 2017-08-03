#coding:utf-8

## 当然，之前说将各种控件的位置都写成绝对位置和大小，会有一些问题。这是不对的
## 有时需要动态布局，而有时则需要静态布局
  
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
