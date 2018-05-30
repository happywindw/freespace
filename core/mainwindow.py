import math
import wx
import settings
from fsui.rootframe import RootFrame


class MainWindow(RootFrame):
    def __init__(self, parent):
        super().__init__(parent)

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
            self.show_movie_rider_page()
        elif sm_page == 1:  # 'Saber' page
            pass
        elif sm_page == 2:  # 'Lancer' page
            pass
        elif sm_page == 3:  # 'Caster' page
            pass

    def show_movie_rider_page(self):
        """
        show contents of the Movie->Rider page
        :return:
        """
        # show widgets on rlp_tabs_panel
        tl = ['this', 'i do not know', 'is that right', 'goodbye', 'i want it', 'show your heart', 'come on',
              'do you think so', 'yes i do']
        rlp_tabs_sizer = wx.WrapSizer()
        for i in range(len(tl)):
            cb = wx.CheckBox(self.rlp_tabs_panel, wx.ID_ANY, tl[i], wx.DefaultPosition, wx.DefaultSize, 0)
            rlp_tabs_sizer.Add(cb, 0, wx.ALL, 1)
        self.rlp_tabs_panel.SetSizer(rlp_tabs_sizer)
        self.rlp_tabs_panel.Layout()
        rlp_tabs_sizer.Fit(self.rlp_tabs_panel)

        rlp_actor_sizer = wx.WrapSizer()
        for ac in tl:
            rb = wx.RadioButton(self.rlp_actor_panel, wx.ID_ANY, ac, wx.DefaultPosition, wx.DefaultSize, 0)
            rlp_actor_sizer.Add(rb, 0, wx.ALL, 1)
        self.rlp_actor_panel.SetSizer(rlp_actor_sizer)
        self.rlp_actor_panel.Layout()
        rlp_actor_sizer.Fit(self.rlp_actor_panel)

        # show pictures on rcp_scrolled_window
        pic_count = 30
        width, height = self.rcp_scrolled_window.GetSize()
        col_count = math.floor((width - 20) / settings.PICTURE_SIZE['rider'][0])
        row_count = math.ceil(pic_count / col_count)
        rcp_pic_sizer = wx.GridSizer(row_count, col_count, 1, 1)
        for i in range(pic_count):
            picture = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                      wx.Size(settings.PICTURE_SIZE['rider']), wx.BU_AUTODRAW)
            rcp_pic_sizer.Add(picture, 0, wx.ALL, 1)
            bitmap = wx.Bitmap('./resource/test.jpg', wx.BITMAP_TYPE_JPEG)
            picture.SetBitmap(bitmap)
        self.rcp_scrolled_window.SetSizer(rcp_pic_sizer)
        self.rcp_scrolled_window.Layout()
        rcp_pic_sizer.Fit(self.rcp_scrolled_window)

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
