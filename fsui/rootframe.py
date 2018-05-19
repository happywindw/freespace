# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jan 23 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class RootFrame
###########################################################################

class RootFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"FreeSpace", pos=wx.DefaultPosition, size=wx.Size(-1, -1),
                          style=wx.DEFAULT_FRAME_STYLE | wx.MAXIMIZE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(1200, 800), wx.DefaultSize)

        root_sizer = wx.BoxSizer(wx.VERTICAL)

        self.root_listbook = wx.Listbook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_TOP)
        self.home_panel = wx.Panel(self.root_listbook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.root_listbook.AddPage(self.home_panel, u"Home", False)
        self.movie_panel = wx.Panel(self.root_listbook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        movie_sizer = wx.BoxSizer(wx.VERTICAL)

        self.movie_notebook = wx.Notebook(self.movie_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                          wx.NB_FIXEDWIDTH | wx.NB_TOP)
        self.rider_panel = wx.Panel(self.movie_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                    wx.TAB_TRAVERSAL)
        self.movie_notebook.AddPage(self.rider_panel, u"Rider", True)
        self.saber_panel = wx.Panel(self.movie_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                    wx.TAB_TRAVERSAL)
        self.movie_notebook.AddPage(self.saber_panel, u"Saber", False)
        self.lancer_panel = wx.Panel(self.movie_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TAB_TRAVERSAL)
        self.movie_notebook.AddPage(self.lancer_panel, u"Lancer", False)

        movie_sizer.Add(self.movie_notebook, 1, wx.EXPAND | wx.ALL, 0)

        self.movie_panel.SetSizer(movie_sizer)
        self.movie_panel.Layout()
        movie_sizer.Fit(self.movie_panel)
        self.root_listbook.AddPage(self.movie_panel, u"Movie", True)
        self.video_panel = wx.Panel(self.root_listbook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.root_listbook.AddPage(self.video_panel, u"Video", False)
        self.cartoon_panel = wx.Panel(self.root_listbook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                      wx.TAB_TRAVERSAL)
        self.root_listbook.AddPage(self.cartoon_panel, u"Cartoon", False)
        self.comic_panel = wx.Panel(self.root_listbook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.root_listbook.AddPage(self.comic_panel, u"Comic", False)

        root_sizer.Add(self.root_listbook, 1, wx.EXPAND | wx.ALL, 0)

        self.SetSizer(root_sizer)
        self.Layout()
        root_sizer.Fit(self)
        self.status_bar = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)
        self.menu_bar = wx.MenuBar(0)
        self.m_video = wx.Menu()
        self.mm_add_movie = wx.MenuItem(self.m_video, wx.ID_ANY, u"Add Movie...", u"Add a single movie", wx.ITEM_NORMAL)
        self.m_video.Append(self.mm_add_movie)

        self.mm_add_folder = wx.MenuItem(self.m_video, wx.ID_ANY, u"Add Movie Folder...",
                                         u"Add all movies in the folder and sub folders", wx.ITEM_NORMAL)
        self.m_video.Append(self.mm_add_folder)

        self.menu_bar.Append(self.m_video, u"Movie")

        self.m_help = wx.Menu()
        self.mh_about = wx.MenuItem(self.m_help, wx.ID_ANY, u"About", u"Show information about FreeSpace",
                                    wx.ITEM_NORMAL)
        self.m_help.Append(self.mh_about)

        self.menu_bar.Append(self.m_help, u"Help")

        self.SetMenuBar(self.menu_bar)

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_MENU, self.on_mm_add_movie, id=self.mm_add_movie.GetId())
        self.Bind(wx.EVT_MENU, self.on_mm_add_movie_folder, id=self.mm_add_folder.GetId())
        self.Bind(wx.EVT_MENU, self.on_mh_about, id=self.mh_about.GetId())

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def on_mm_add_movie(self, event):
        event.Skip()

    def on_mm_add_movie_folder(self, event):
        event.Skip()

    def on_mh_about(self, event):
        event.Skip()


