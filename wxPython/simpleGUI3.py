# coding:utf-8
  
import wx


def main():
    app = wx.App()
    win = wx.Frame(None, title='NotePad', size=(440, 320))
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
