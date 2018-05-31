import math
import wx
import settings
from fsui.rootframe import RootFrame


class MainWindow(RootFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.init_movie_page()

    def init_home_page(self):
        pass

    def init_movie_page(self):
        tl = ['this', 'i do not know', 'is that right', 'goodbye', 'i want it', 'show your heart', 'come on',
              'do you think so', 'yes i do']
        self.load_movie_rider_tabs(tl, self.rlp_tabs_panel)
        self.load_movie_rider_tabs(tl, self.rlp_actor_panel)

        pic_list = ['E:/Pictures/wdfe.jpg', 'E:/Pictures/wdfe.jpg', 'E:/Pictures/wdfe.jpg', 'E:/Pictures/wdfe.jpg',
                    'E:/Pictures/wdfe.jpg', 'E:/Pictures/wdfe.jpg', 'E:/Pictures/wdfe.jpg', 'E:/Pictures/wdfe.jpg',
                    'E:/Pictures/wdfe.jpg', 'E:/Pictures/wdfe.jpg', 'E:/Pictures/wdfe.jpg', 'E:/Pictures/wdfe.jpg',
                    'E:/Pictures/wdfe.jpg', 'E:/Pictures/wdfe.jpg', 'E:/Pictures/wdfe.jpg', 'E:/Pictures/wdfe.jpg',
                    'E:/Pictures/wdfe.jpg', 'E:/Pictures/wdfe.jpg', 'E:/Pictures/wdfe.jpg', 'E:/Pictures/wdfe.jpg']
        self.load_movie_rider_pictures(pic_list)

    def on_page_changed(self, event):
        """
        Switch between pages of the main window
        :param event:
        :return:
        """
        selected_page = self.root_listbook.GetSelection()
        if selected_page == 0:    # 'Home' page
            pass
        elif selected_page == 1:  # 'Movie' page
            self.on_movie_page_changed(event)
        elif selected_page == 2:  # 'Video' page
            pass
        elif selected_page == 3:  # 'Cartoon' page
            pass
        elif selected_page == 4:  # 'Comic' page
            pass
        elif selected_page == 5:  # 'Game' page
            pass

    def on_movie_page_changed(self, event):
        """
        Switch between sub pages of the Movie page
        :param event:
        :return:
        """
        sm_page = self.movie_notebook.GetSelection()
        if sm_page == 0:    # 'Rider' page
            self.load_movie_rider_pictures(['E:/Pictures/wdfe.jpg', 'E:/Pictures/wdfe.jpg',
                                            'E:/Pictures/wdfe.jpg'])
            # self.load_movie_rider_pictures(['E:/Pictures/wdfe.jpg'])
        elif sm_page == 1:  # 'Saber' page
            pass
        elif sm_page == 2:  # 'Lancer' page
            pass
        elif sm_page == 3:  # 'Caster' page
            pass

    def load_movie_rider_tabs(self, tab_list, tab_panel):
        """
        a universal method to load and show tabs on specified tab panel
        :param tab_list:
        :param tab_panel:
        :return:
        """
        # remove children widgets first
        for child in tab_panel.GetChildren():
            tab_panel.RemoveChild(child)

        rt_sizer = wx.WrapSizer()
        if tab_panel is self.rlp_tabs_panel:
            for tab in tab_list:
                cb = wx.CheckBox(self.rlp_tabs_panel, wx.ID_ANY, tab, wx.DefaultPosition, wx.DefaultSize, 0)
                rt_sizer.Add(cb, 0, wx.ALL, 1)
        else:
            for tab in tab_list:
                rb = wx.RadioButton(self.rlp_actor_panel, wx.ID_ANY, tab, wx.DefaultPosition, wx.DefaultSize, 0)
                rt_sizer.Add(rb, 0, wx.ALL, 1)
        tab_panel.SetSizer(rt_sizer)
        tab_panel.Layout()
        rt_sizer.Fit(tab_panel)

    def load_movie_rider_pictures(self, pic_list):
        """
        load and show pictures on rcp_scrolled_window
        :param pic_list: picture location list
        :return:
        """
        # remove children widgets first
        rp_sizer = self.rcp_scrolled_window.GetSizer()
        if rp_sizer:
            child_counts = len(self.rcp_scrolled_window.GetChildren())
            for i, cp in enumerate(self.rcp_scrolled_window.GetChildren()):
                rp_sizer.Hide(child_counts - i - 1)
                rp_sizer.Remove(child_counts - i - 1)
                self.rcp_scrolled_window.RemoveChild(cp)

        # calculate row and column counts
        width = self.rider_content_panel.GetSize()[0] - 20  # fixed width of rcp_scrolled_window
        self.rcp_scrolled_window.SetMinSize(wx.Size(width, -1))
        col_count = max(math.floor(width / (settings.PICTURE_SIZE['rider'][0] + settings.PICTURE_GAP['rider'][1])), 1)
        row_count = max(math.ceil(len(pic_list) / col_count), 1)
        if rp_sizer:
            rp_sizer.SetRows(row_count)
            rp_sizer.SetCols(col_count)
        else:
            rp_sizer = wx.GridSizer(row_count, col_count, settings.PICTURE_GAP['rider'][0],
                                    settings.PICTURE_GAP['rider'][1])

        # put pictures on rcp_scrolled_window
        for pic in pic_list:
            bitmap = wx.Bitmap(pic, wx.BITMAP_TYPE_JPEG)
            sb = wx.StaticBitmap(self.rcp_scrolled_window, wx.ID_ANY, bitmap, wx.DefaultPosition,
                                 wx.Size(settings.PICTURE_SIZE['rider']), wx.BU_AUTODRAW)
            rp_sizer.Add(sb, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 1)
        self.rcp_scrolled_window.SetSizer(rp_sizer)
        self.rcp_scrolled_window.Layout()
        rp_sizer.FitInside(self.rcp_scrolled_window)

    def mr_show_hide_panel(self, event):
        """
        show or hide a tab rlp panel when user click these panels
        :param event:
        :return:
        """
        ob = event.GetEventObject()
        tb = None
        if ob is self.rlp_tabs or ob.GetParent() is self.rlp_tabs:
            tb = self.rlp_tabs_panel
        elif ob is self.rlp_actor or ob.GetParent() is self.rlp_actor:
            tb = self.rlp_actor_panel
        if tb.IsShown():
            tb.Hide()
        else:
            tb.Show()

    def on_mm_add_movie(self, event):
        """
        menu->movie->Add Movie...
        :param event:
        :return:
        """
        fd = wx.FileDialog(self, 'Choose a movie file...')
        if fd.ShowModal() == wx.ID_OK:
            print('choose file')
        fd.Destroy()

    def on_mm_add_movie_folder(self, event):
        """
        menu->movie->Add Movie Folder...
        :param event:
        :return:
        """
        dd = wx.DirDialog(self, 'Choose a movie dir...')
        if dd.ShowModal() == wx.ID_OK:
            print('choose dir')
        dd.Destroy()

    def on_mh_about(self, event):
        """
        menu->help->About
        :param event:
        :return:
        """
        md = wx.MessageDialog(self, 'FreeSpace v1.0\n©2018-2019 Louis Young. All Rights Reserved.',
                              'About FreeSpace', wx.OK | wx.ICON_QUESTION)
        md.ShowModal()
        md.Destroy()
