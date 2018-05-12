import wx
import wx.xrc


class RootFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"FREE SPACE", pos=wx.DefaultPosition,
                          size=wx.Size(1400, 800), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        # self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        self.CreateStatusBar()

        # Create and set menu and menu items
        self.menu_file = wx.Menu()
        self.mi_add_video = wx.MenuItem(self.menu_file, wx.ID_ANY, 'Add Video...', 'Add a single video', wx.ITEM_NORMAL)
        self.mi_add_video_folder = wx.MenuItem(self.menu_file, wx.ID_ANY, 'Add Video Folder...',
                                               'Add all videos in the folder and sub folders', wx.ITEM_NORMAL)
        self.menu_file.Append(self.mi_add_video)
        self.menu_file.Append(self.mi_add_video_folder)
        self.menu_file.AppendSeparator()

        self.menu_help = wx.Menu()
        self.mi_about = wx.MenuItem(self.menu_help, wx.ID_ANY, 'About', 'Show information about FreeSpace',
                                    wx.ITEM_NORMAL)
        self.menu_help.Append(self.mi_about)

        # Create and set a menu bar
        self.menu_bar = wx.MenuBar()
        self.menu_bar.Append(self.menu_file, 'File')
        self.menu_bar.Append(self.menu_help, 'Help')
        self.SetMenuBar(self.menu_bar)

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_MENU, self.mf_add_video, id=self.mi_add_video.GetId())
        self.Bind(wx.EVT_MENU, self.mf_add_video_folder, id=self.mi_add_video_folder.GetId())
        self.Bind(wx.EVT_MENU, self.mh_about, id=self.mi_about.GetId())

    def __del__(self):
        pass

    # Virtual event handlers, override them in derived class
    def mf_add_video(self, event):
        event.Skip()

    def mf_add_video_folder(self, event):
        event.Skip()

    def mh_about(self, event):
        event.Skip()
