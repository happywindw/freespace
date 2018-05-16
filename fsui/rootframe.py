import wx
import wx.xrc


class RootFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"FREE SPACE", pos=wx.DefaultPosition,
                          style=wx.MAXIMIZE | wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

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

        root_sizer = wx.BoxSizer(wx.VERTICAL)

        self.top_panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.top_panel.SetMaxSize(wx.Size(-1, 100))
        root_sizer.Add(self.top_panel, 1, wx.EXPAND | wx.ALL, 5)

        self.notebook = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.main_page_panel = wx.Panel(self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.notebook.AddPage(self.main_page_panel, u"Main page", False)
        self.movie_page_panel = wx.Panel(self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.notebook.AddPage(self.movie_page_panel, u"Movie page", False)
        self.video_page_panel = wx.Panel(self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.notebook.AddPage(self.video_page_panel, u"Video page", False)

        root_sizer.Add(self.notebook, 1, wx.EXPAND | wx.ALL, 5)

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
