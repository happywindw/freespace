import wx
import wx.xrc


class RootFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"FREE SPACE", pos=wx.DefaultPosition,
                          size=wx.Size(1400, 800), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        # self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        self.CreateStatusBar()  # 创建窗口底部的状态栏

        # 创建菜单及菜单项
        self.menu_file = wx.Menu()
        self.mi_add_video = wx.MenuItem(self.menu_file, wx.ID_ADD, 'Add Video...', 'Add a single video', wx.ITEM_NORMAL)
        self.menu_file.Append(self.mi_add_video)
        self.mi_add_video_folder = wx.MenuItem(self.menu_file, wx.ID_ADD, 'Add Video Folder...',
                                               'Add all videos in the folder and sub folders', wx.ITEM_NORMAL)
        self.menu_file.Append(self.mi_add_video_folder)
        self.menu_file.AppendSeparator()

        self.menu_help = wx.Menu()
        self.mi_about = wx.MenuItem(self.menu_help, wx.ID_ANY, 'About', 'Show information about FreeSpace',
                                    wx.ITEM_NORMAL)
        self.menu_help.Append(self.mi_about)

        # 创建并设置菜单栏
        self.menu_bar = wx.MenuBar()
        self.menu_bar.Append(self.menu_file, 'File')
        self.menu_bar.Append(self.menu_help, 'Help')
        self.SetMenuBar(self.menu_bar)

        self.Centre(wx.BOTH)
        self.Show()

    def __del__(self):
        pass


# for test
app = wx.App(False)
frame = RootFrame(None)
app.MainLoop()
