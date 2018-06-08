import math
import wx
import settings
from core.taskcenter import TaskCenter
from fsui.rootframe import RootFrame


class MainWindow(RootFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.tc = TaskCenter()

        # init widgets on movie page
        self.rcp_popup_menu = wx.Menu()
        for text in ['Play', 'Detail', 'Edit', 'Open Dir', 'Delete']:
            item = self.rcp_popup_menu.Append(-1, text)
            self.rcp_scrolled_window.Bind(wx.EVT_MENU, self.mr_popup_item_selected, item)
        self.init_movie_page()

    def init_home_page(self):
        pass

    def init_movie_page(self):
        tl = self.tc.get_movie_rider_tabs()
        self.load_movie_rider_tabs(tl['tabs'], self.rlp_tabs_panel)
        self.load_movie_rider_tabs(tl['actor'], self.rlp_actor_panel)

        pl = self.tc.get_movie_rider_pics()
        self.load_movie_rider_pictures(pl)

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
            pass
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
                    tb.Bind(wx.EVT_CHECKBOX, self.mr_filter_rider)
                else:
                    tb = wx.RadioButton(tab_panel, wx.ID_ANY, ts, wx.DefaultPosition, wx.DefaultSize, 0)
                    tb.Bind(wx.EVT_RADIOBUTTON, self.mr_filter_rider)
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
                sb.Bind(wx.EVT_CONTEXT_MENU, self.mr_show_popup_menu)
                sb.Bind(wx.EVT_ENTER_WINDOW, self.mr_enter_picture)
                sb.Bind(wx.EVT_LEAVE_WINDOW, self.mr_leave_picture)
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

    def mr_filter_rider(self, event):
        """
        filter rider movies which matches the selected tabs
        :param event:
        :return:
        """
        tab_list = []
        if self.rlp_tabs_panel.IsShown():
            for chk in self.rlp_tabs_panel.GetChildren():
                if chk.GetValue():
                    tab_list.append(chk.GetLabel())
        chosen_actor = ''
        if self.rlp_actor_panel.IsShown():
            for rdo in self.rlp_actor_panel.GetChildren():
                if rdo.GetValue():
                    chosen_actor = rdo.GetLabel()
        print(tab_list, chosen_actor)
        event.Skip()

    def mr_show_popup_menu(self, event):
        """
        show popup menu when user right click on pictures
        :param event:
        :return:
        """
        pos = event.GetPosition()
        pos = self.rcp_scrolled_window.ScreenToClient(pos)
        self.rcp_scrolled_window.PopupMenu(self.rcp_popup_menu, pos)

    def mr_enter_picture(self, event):
        sb = event.GetEventObject()
        img = wx.Image('./temp/test.jpg')
        ps = img.GetSize()
        img = img.Scale(int(ps[0] * 356 / ps[1]), 356, wx.IMAGE_QUALITY_HIGH)
        bitmap = wx.Bitmap(img.Resize((250, 356), wx.Point(0, 0)), wx.BITMAP_TYPE_JPEG)
        bitmap.SetSize((250, 356))
        sb.SetBitmap(bitmap)

    def mr_leave_picture(self, event):
        sb = event.GetEventObject()
        img = wx.Image('./temp/test.jpg')
        ps = img.GetSize()
        img = img.Scale(int(ps[0] * 356 / ps[1]), 356, wx.IMAGE_QUALITY_HIGH)
        bitmap = wx.Bitmap(img.Resize((250, 356), wx.Point(256 - img.GetSize()[0], 0)), wx.BITMAP_TYPE_JPEG)
        bitmap.SetSize((250, 356))
        sb.SetBitmap(bitmap)

    def mr_popup_item_selected(self, event):
        """
        deal with selected item
        :param event:
        :return:
        """
        item = self.rcp_popup_menu.FindItemById(event.GetId())
        wx.MessageBox("You selected item '%s'" % item.GetText())

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
