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

        self.SetSizeHints(wx.Size(1200, 800), wx.Size(1900, 1000))

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
        rider_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.rider_splitter = wx.SplitterWindow(self.rider_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                                wx.SP_3D)
        self.rider_splitter.SetSashGravity(0)
        self.rider_splitter.Bind(wx.EVT_IDLE, self.rider_splitterOnIdle)

        self.rider_left_panel = wx.Panel(self.rider_splitter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                         wx.TAB_TRAVERSAL)
        wSizer1 = wx.WrapSizer(wx.HORIZONTAL)

        self.m_button9 = wx.Button(self.rider_left_panel, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0)
        wSizer1.Add(self.m_button9, 0, wx.ALL, 5)

        self.m_button10 = wx.Button(self.rider_left_panel, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize,
                                    0)
        wSizer1.Add(self.m_button10, 0, wx.ALL, 5)

        self.rider_left_panel.SetSizer(wSizer1)
        self.rider_left_panel.Layout()
        wSizer1.Fit(self.rider_left_panel)
        self.rider_right_panel = wx.Panel(self.rider_splitter, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                          wx.TAB_TRAVERSAL)
        rrp_sizer = wx.BoxSizer(wx.VERTICAL)

        self.rider_content_panel = wx.Panel(self.rider_right_panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                            wx.TAB_TRAVERSAL)
        bSizer16 = wx.BoxSizer(wx.VERTICAL)

        self.rcp_page_panel = wx.Panel(self.rider_content_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 50),
                                       wx.TAB_TRAVERSAL)
        self.rcp_page_panel.SetMaxSize(wx.Size(-1, 50))

        rcp_page_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.rcp_text = wx.StaticText(self.rcp_page_panel, wx.ID_ANY,
                                      u"There are 0 movies in total, 0 pages in total.          Jump to page: ",
                                      wx.DefaultPosition, wx.DefaultSize, 0)
        self.rcp_text.Wrap(-1)
        rcp_page_sizer.Add(self.rcp_text, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.rcp_text_ctrl = wx.TextCtrl(self.rcp_page_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        rcp_page_sizer.Add(self.rcp_text_ctrl, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.rcp_jump_btn = wx.Button(self.rcp_page_panel, wx.ID_ANY, u"Go", wx.DefaultPosition, wx.DefaultSize, 0)
        rcp_page_sizer.Add(self.rcp_jump_btn, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.rcp_staticline = wx.StaticLine(self.rcp_page_panel, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 50),
                                            wx.LI_VERTICAL)
        rcp_page_sizer.Add(self.rcp_staticline, 0, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 5)

        self.rcp_pageup_btn = wx.Button(self.rcp_page_panel, wx.ID_ANY, u"PageUp", wx.DefaultPosition, wx.DefaultSize,
                                        0)
        rcp_page_sizer.Add(self.rcp_pageup_btn, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.rcp_pagedown_btn = wx.Button(self.rcp_page_panel, wx.ID_ANY, u"PageDown", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        rcp_page_sizer.Add(self.rcp_pagedown_btn, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.rcp_page_panel.SetSizer(rcp_page_sizer)
        self.rcp_page_panel.Layout()
        bSizer16.Add(self.rcp_page_panel, 1, wx.EXPAND | wx.ALL, 5)

        self.rcp_scrolled_window = wx.ScrolledWindow(self.rider_content_panel, wx.ID_ANY, wx.DefaultPosition,
                                                     wx.DefaultSize, wx.HSCROLL | wx.VSCROLL)
        self.rcp_scrolled_window.SetScrollRate(5, 20)
        rcp_pic_sizer = wx.GridSizer(5, 6, 0, 0)

        self.rcp_pic_01 = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                          wx.Size(250, 356), wx.BU_AUTODRAW)
        rcp_pic_sizer.Add(self.rcp_pic_01, 0, wx.ALL, 5)

        self.rcp_pic_02 = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                          wx.Size(250, 356), wx.BU_AUTODRAW)
        rcp_pic_sizer.Add(self.rcp_pic_02, 0, wx.ALL, 5)

        self.rcp_pic_03 = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                          wx.Size(250, 356), wx.BU_AUTODRAW)
        rcp_pic_sizer.Add(self.rcp_pic_03, 0, wx.ALL, 5)

        self.rcp_pic_04 = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                          wx.Size(250, 356), wx.BU_AUTODRAW)
        rcp_pic_sizer.Add(self.rcp_pic_04, 0, wx.ALL, 5)

        self.rcp_pic_05 = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                          wx.Size(250, 356), wx.BU_AUTODRAW)
        rcp_pic_sizer.Add(self.rcp_pic_05, 0, wx.ALL, 5)

        self.rcp_pic_06 = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                          wx.Size(250, 356), wx.BU_AUTODRAW)
        rcp_pic_sizer.Add(self.rcp_pic_06, 0, wx.ALL, 5)

        self.rcp_pic_07 = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                          wx.Size(250, 356), wx.BU_AUTODRAW)
        rcp_pic_sizer.Add(self.rcp_pic_07, 0, wx.ALL, 5)

        self.rcp_pic_08 = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                          wx.Size(250, 356), wx.BU_AUTODRAW)
        rcp_pic_sizer.Add(self.rcp_pic_08, 0, wx.ALL, 5)

        self.rcp_pic_09 = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                          wx.Size(250, 356), wx.BU_AUTODRAW)
        rcp_pic_sizer.Add(self.rcp_pic_09, 0, wx.ALL, 5)

        self.rcp_pic_10 = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                          wx.Size(250, 356), wx.BU_AUTODRAW)
        rcp_pic_sizer.Add(self.rcp_pic_10, 0, wx.ALL, 5)

        self.rcp_pic_11 = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                          wx.Size(250, 356), wx.BU_AUTODRAW)
        rcp_pic_sizer.Add(self.rcp_pic_11, 0, wx.ALL, 5)

        self.rcp_pic_12 = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                          wx.Size(250, 356), wx.BU_AUTODRAW)
        rcp_pic_sizer.Add(self.rcp_pic_12, 0, wx.ALL, 5)

        self.rcp_pic_13 = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                          wx.Size(250, 356), wx.BU_AUTODRAW)
        rcp_pic_sizer.Add(self.rcp_pic_13, 0, wx.ALL, 5)

        self.rcp_pic_14 = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                          wx.Size(250, 356), wx.BU_AUTODRAW)
        rcp_pic_sizer.Add(self.rcp_pic_14, 0, wx.ALL, 5)

        self.rcp_pic_15 = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                          wx.Size(250, 356), wx.BU_AUTODRAW)
        rcp_pic_sizer.Add(self.rcp_pic_15, 0, wx.ALL, 5)

        self.rcp_pic_16 = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                          wx.Size(250, 356), wx.BU_AUTODRAW)
        rcp_pic_sizer.Add(self.rcp_pic_16, 0, wx.ALL, 5)

        self.rcp_pic_17 = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                          wx.Size(250, 356), wx.BU_AUTODRAW)
        rcp_pic_sizer.Add(self.rcp_pic_17, 0, wx.ALL, 5)

        self.rcp_pic_18 = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                          wx.Size(250, 356), wx.BU_AUTODRAW)
        rcp_pic_sizer.Add(self.rcp_pic_18, 0, wx.ALL, 5)

        self.rcp_pic_19 = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                          wx.Size(250, 356), wx.BU_AUTODRAW)
        rcp_pic_sizer.Add(self.rcp_pic_19, 0, wx.ALL, 5)

        self.rcp_pic_20 = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                          wx.Size(250, 356), wx.BU_AUTODRAW)
        rcp_pic_sizer.Add(self.rcp_pic_20, 0, wx.ALL, 5)

        self.rcp_pic_21 = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                          wx.Size(250, 356), wx.BU_AUTODRAW)
        rcp_pic_sizer.Add(self.rcp_pic_21, 0, wx.ALL, 5)

        self.rcp_pic_22 = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                          wx.Size(250, 356), wx.BU_AUTODRAW)
        rcp_pic_sizer.Add(self.rcp_pic_22, 0, wx.ALL, 5)

        self.rcp_pic_23 = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                          wx.Size(250, 356), wx.BU_AUTODRAW)
        rcp_pic_sizer.Add(self.rcp_pic_23, 0, wx.ALL, 5)

        self.rcp_pic_24 = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                          wx.Size(250, 356), wx.BU_AUTODRAW)
        rcp_pic_sizer.Add(self.rcp_pic_24, 0, wx.ALL, 5)

        self.rcp_pic_25 = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                          wx.Size(250, 356), wx.BU_AUTODRAW)
        rcp_pic_sizer.Add(self.rcp_pic_25, 0, wx.ALL, 5)

        self.rcp_pic_26 = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                          wx.Size(250, 356), wx.BU_AUTODRAW)
        rcp_pic_sizer.Add(self.rcp_pic_26, 0, wx.ALL, 5)

        self.rcp_pic_27 = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                          wx.Size(250, 356), wx.BU_AUTODRAW)
        rcp_pic_sizer.Add(self.rcp_pic_27, 0, wx.ALL, 5)

        self.rcp_pic_28 = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                          wx.Size(250, 356), wx.BU_AUTODRAW)
        rcp_pic_sizer.Add(self.rcp_pic_28, 0, wx.ALL, 5)

        self.rcp_pic_29 = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                          wx.Size(250, 356), wx.BU_AUTODRAW)
        rcp_pic_sizer.Add(self.rcp_pic_29, 0, wx.ALL, 5)

        self.rcp_pic_30 = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                          wx.Size(250, 356), wx.BU_AUTODRAW)
        rcp_pic_sizer.Add(self.rcp_pic_30, 0, wx.ALL, 5)

        self.rcp_scrolled_window.SetSizer(rcp_pic_sizer)
        self.rcp_scrolled_window.Layout()
        rcp_pic_sizer.Fit(self.rcp_scrolled_window)
        bSizer16.Add(self.rcp_scrolled_window, 1, wx.EXPAND | wx.ALL, 5)

        self.rider_content_panel.SetSizer(bSizer16)
        self.rider_content_panel.Layout()
        bSizer16.Fit(self.rider_content_panel)
        rrp_sizer.Add(self.rider_content_panel, 1, wx.EXPAND | wx.ALL, 5)

        self.rider_right_panel.SetSizer(rrp_sizer)
        self.rider_right_panel.Layout()
        rrp_sizer.Fit(self.rider_right_panel)
        self.rider_splitter.SplitVertically(self.rider_left_panel, self.rider_right_panel, 300)
        rider_sizer.Add(self.rider_splitter, 1, wx.ALIGN_CENTER | wx.EXPAND, 0)

        self.rider_panel.SetSizer(rider_sizer)
        self.rider_panel.Layout()
        rider_sizer.Fit(self.rider_panel)
        self.movie_notebook.AddPage(self.rider_panel, u"Rider", True)
        self.saber_panel = wx.Panel(self.movie_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                    wx.TAB_TRAVERSAL)
        self.movie_notebook.AddPage(self.saber_panel, u"Saber", False)
        self.lancer_panel = wx.Panel(self.movie_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TAB_TRAVERSAL)
        self.movie_notebook.AddPage(self.lancer_panel, u"Lancer", False)
        self.caster_panel = wx.Panel(self.movie_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TAB_TRAVERSAL)
        self.movie_notebook.AddPage(self.caster_panel, u"Caster", False)

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

    def rider_splitterOnIdle(self, event):
        self.rider_splitter.SetSashPosition(300)
        self.rider_splitter.Unbind(wx.EVT_IDLE)


