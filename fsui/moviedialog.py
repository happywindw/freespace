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
## Class MovieDialog
###########################################################################

class MovieDialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        movie_sizer = wx.BoxSizer(wx.VERTICAL)

        self.movie_notebook = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.detail_panel = wx.Panel(self.movie_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TAB_TRAVERSAL)
        d_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.detail_bmp = wx.StaticBitmap(self.detail_panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                          wx.Size(500, 356), 0)
        d_sizer.Add(self.detail_bmp, 0, wx.ALL, 5)

        detail_sizer = wx.GridBagSizer(0, 0)
        detail_sizer.SetFlexibleDirection(wx.BOTH)
        detail_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
        detail_sizer.SetEmptyCellSize(wx.Size(-1, 30))

        d_sizer.Add(detail_sizer, 1, wx.EXPAND, 5)

        self.detail_panel.SetSizer(d_sizer)
        self.detail_panel.Layout()
        d_sizer.Fit(self.detail_panel)
        self.movie_notebook.AddPage(self.detail_panel, u"Deatil", True)
        self.modify_panel = wx.Panel(self.movie_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TAB_TRAVERSAL)
        modify_sizer = wx.GridBagSizer(0, 0)
        modify_sizer.SetFlexibleDirection(wx.BOTH)
        modify_sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.modify_panel.SetSizer(modify_sizer)
        self.modify_panel.Layout()
        modify_sizer.Fit(self.modify_panel)
        self.movie_notebook.AddPage(self.modify_panel, u"Modify", False)

        movie_sizer.Add(self.movie_notebook, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(movie_sizer)
        self.Layout()
        movie_sizer.Fit(self)

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


