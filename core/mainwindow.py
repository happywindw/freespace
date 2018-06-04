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
              'do you think so', 'yes i do', 'oh my god', 'how do you do', 'may i help you', 'leave me alone',
              'do you think so', 'yes i do', 'oh my god', 'how do you do', 'may i help you', 'leave me alone',
              'do you think so', 'yes i do', 'oh my god', 'how do you do', 'may i help you', 'leave me alone',
              'do you think so', 'yes i do', 'oh my god', 'how do you do', 'may i help you', 'leave me alone',
              'do you think so', 'yes i do', 'oh my god', 'how do you do', 'may i help you', 'leave me alone',
              'do you think so', 'yes i do', 'oh my god', 'how do you do', 'may i help you', 'leave me alone']
        tt = ['a', 'b', 'cc', 'alice', 'bob', 'tom', 'victor', 'troy', 'jim', 'this is not your fault', 'yes',
              'please forgive me', 'oh shirt', 'thanks a lot', 'come on baby', 'where are you', 'shut up',
              'a', 'b', 'cc', 'alice', 'bob', 'tom', 'victor', 'troy', 'jim', 'this is not your fault', 'yes',
              'please forgive me', 'oh shirt', 'thanks a lot', 'come on baby', 'where are you', 'shut up',
              'a', 'b', 'cc', 'alice', 'bob', 'tom', 'victor', 'troy', 'jim', 'this is not your fault', 'yes',
              'please forgive me', 'oh shirt', 'thanks a lot', 'come on baby', 'where are you', 'shut up',
              'a', 'b', 'cc', 'alice', 'bob', 'tom', 'victor', 'troy', 'jim', 'this is not your fault', 'yes',
              'please forgive me', 'oh shirt', 'thanks a lot', 'come on baby', 'where are you', 'shut up',
              ]
        self.load_movie_rider_tabs(tl, self.rlp_tabs_panel)
        self.load_movie_rider_tabs(tt, self.rlp_actor_panel)

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
            import random
            self.load_movie_rider_pictures(['E:/Pictures/wdfe.jpg'] * random.randint(2, 30))
            tl = ['a', 'yes', 'no', 'how', 'ok', 'environment'] * random.randint(1, 20)
            tt = ['1', '23', '9999', '7', '66', '87654', '-1', '000'] * random.randint(1, 20)
            self.load_movie_rider_tabs(tt, self.rlp_tabs_panel)
            self.load_movie_rider_tabs(tl, self.rlp_actor_panel)
        elif sm_page == 1:  # 'Saber' page
            pass
        elif sm_page == 2:  # 'Lancer' page
            pass
        elif sm_page == 3:  # 'Caster' page
            pass

    def load_movie_rider_tabs(self, tab_list, tab_panel):
        """
        a universal method to load and show given tabs on specified tab panel
        :param tab_list:
        :param tab_panel:
        :return:
        """
        child_list = tab_panel.GetChildren()
        child_count = len(child_list)
        rt_sizer = wx.WrapSizer() if not child_list else tab_panel.GetSizer()
        flag = True if tab_panel is self.rlp_tabs_panel else False
        for i, ts in enumerate(tab_list):
            if i < child_count:
                if child_list[i].GetLabel() == tab_list[i]:
                    continue
                child_list[i].SetLabel(ts)
            else:
                if flag:
                    tb = wx.CheckBox(tab_panel, wx.ID_ANY, ts, wx.DefaultPosition, wx.DefaultSize, 0)
                else:
                    tb = wx.RadioButton(tab_panel, wx.ID_ANY, ts, wx.DefaultPosition, wx.DefaultSize, 0)
                rt_sizer.Add(tb, 0, wx.ALL, 1)
        # remove the redundant widgets
        remove_count = child_count - len(tab_list)
        while remove_count > 0:
            rt_sizer.Hide(child_count - 1)
            rt_sizer.Remove(child_count - 1)
            tab_panel.RemoveChild(child_list[child_count - 1])
            child_count -= 1
            remove_count -= 1
        # resize panel
        tab_panel.SetSizer(rt_sizer)
        tab_panel.Layout()
        rt_sizer.Fit(tab_panel)
        self.rlp_scrolled_window.Layout()
        self.rlp_scrolled_window.GetSizer().FitInside(self.rlp_scrolled_window)

    def load_movie_rider_pictures(self, pic_list):
        """
        load and show pictures on rcp_scrolled_window
        :param pic_list: picture location list
        :return:
        """
        # calculate row and column counts
        width = self.rider_content_panel.GetSize()[0] - 20  # fixed width of rcp_scrolled_window
        self.rcp_scrolled_window.SetMinSize(wx.Size(width, -1))
        col_count = max(math.floor(width / (settings.PICTURE_SIZE['rider'][0] + settings.PICTURE_GAP['rider'][1])), 1)
        row_count = max(math.ceil(len(pic_list) / col_count), 1)
        rp_sizer = self.rcp_scrolled_window.GetSizer()
        if rp_sizer:
            rp_sizer.SetRows(row_count)
            rp_sizer.SetCols(col_count)
        else:
            rp_sizer = wx.GridSizer(row_count, col_count, settings.PICTURE_GAP['rider'][0],
                                    settings.PICTURE_GAP['rider'][1])
        # add new pictures on panel
        child_list = self.rcp_scrolled_window.GetChildren()
        child_count = len(child_list)
        for i, pic in enumerate(pic_list):
            bitmap = wx.Bitmap(pic, wx.BITMAP_TYPE_JPEG)
            if i < child_count:
                child_list[i].SetBitmap(bitmap)
            else:
                sb = wx.StaticBitmap(self.rcp_scrolled_window, wx.ID_ANY, bitmap, wx.DefaultPosition,
                                     wx.Size(settings.PICTURE_SIZE['rider']), wx.BU_AUTODRAW)
                rp_sizer.Add(sb, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 1)
        # remove redundant pictures
        remove_count = child_count - len(pic_list)
        while remove_count > 0:
            rp_sizer.Hide(child_count - 1)
            rp_sizer.Remove(child_count - 1)
            self.rcp_scrolled_window.RemoveChild(child_list[child_count - 1])
            child_count -= 1
            remove_count -= 1
        # layout and fit
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
        self.rlp_scrolled_window.Layout()
        self.rlp_scrolled_window.GetSizer().FitInside(self.rlp_scrolled_window)

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
