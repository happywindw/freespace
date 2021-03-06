import math
import os
import wx

from core.subwindows import DetailEditDialog
from core.taskcenter import MovieTask
from core.utils import get_fitted_bitmap
from fsui.rootframe import RootFrame
from settings import PICTURE_SIZE, PICTURE_GAP


class MainWindow(RootFrame):
    """the main window of the program"""
    def __init__(self, parent):
        super().__init__(parent)

        # init widgets on movie page
        self.movie_task = MovieTask()
        self.mr_label_dict = {'tabs': [], 'actor': 'All'}

        self.mr_total_num = 0
        self.mr_pics_per_page = 30
        self.mr_total_page = 1
        self.mr_current_page = 1
        self.mr_movie_list = []

        self.rcp_popup_menu = wx.Menu()
        for text in ['Play', 'Detail', 'Edit', 'Open Dir', 'Delete']:
            item = self.rcp_popup_menu.Append(-1, text)
            self.rcp_scrolled_window.Bind(wx.EVT_MENU, self.mr_popup_item_selected, item)
        self.init_movie_page()

    def init_home_page(self):
        pass

    def init_movie_page(self):
        self.mr_label_dict['tabs'] = self.movie_task.get_movie_rider_tabs('tabs')
        self.mr_label_dict['actor'] = self.movie_task.get_movie_rider_tabs('actor')
        self.load_movie_rider_tabs(self.mr_label_dict['tabs'], self.rlp_tabs_panel)
        self.load_movie_rider_tabs(self.mr_label_dict['actor'], self.rlp_actor_panel)
        self.mr_update_pic_pages()

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
        if not flag:
            child_list[0].SetValue(True)  # choose the first one as default
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

    def load_movie_rider_pictures(self):
        """
        load and show pictures on rcp_scrolled_window
        :return:
        """
        self.SetCursor(wx.Cursor(wx.CURSOR_WAIT))
        # calculate row and column counts
        width = self.rider_content_panel.GetSize()[0] - 20  # fixed width of rcp_scrolled_window
        self.rcp_scrolled_window.SetMinSize(wx.Size(width, -1))
        col_count = max(math.floor(width / (PICTURE_SIZE['rider'][0] + PICTURE_GAP['rider'][1])), 1)
        row_count = max(math.ceil(len(self.mr_movie_list) / col_count), 1)
        rp_sizer = self.rcp_scrolled_window.GetSizer()
        if rp_sizer:
            rp_sizer.SetRows(row_count)
            rp_sizer.SetCols(col_count)
        else:
            rp_sizer = wx.GridSizer(row_count, col_count, PICTURE_GAP['rider'][0], PICTURE_GAP['rider'][1])
        # add new pictures on panel
        child_list = self.rcp_scrolled_window.GetChildren()
        child_count = len(child_list)
        for i, pic in enumerate(self.mr_movie_list):
            pic = pic[1] if os.path.exists(pic[1]) else './test/temp.jpg'
            bitmap = get_fitted_bitmap(pic, PICTURE_SIZE['rider'], 'right')
            if i < child_count:
                child_list[i].SetBitmap(bitmap)
            else:
                sb = wx.StaticBitmap(self.rcp_scrolled_window, wx.ID_ANY, bitmap, wx.DefaultPosition,
                                     wx.Size(PICTURE_SIZE['rider']), wx.BU_AUTODRAW)
                rp_sizer.Add(sb, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 1)
                sb.Bind(wx.EVT_CONTEXT_MENU, self.mr_show_popup_menu)
                sb.Bind(wx.EVT_ENTER_WINDOW, self.mr_enter_picture)
                sb.Bind(wx.EVT_LEAVE_WINDOW, self.mr_leave_picture)
        # remove redundant pictures
        remove_count = child_count - len(self.mr_movie_list)
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
        self.SetCursor(wx.Cursor(wx.CURSOR_ARROW))

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

    def mr_clear_tabs(self, event):
        """
        clear selected tabs
        :param event:
        :return:
        """
        for cb in self.rlp_tabs_panel.GetChildren():
            cb.SetValue(False)
        self.mr_filter_rider(event)

    def mr_prev_page(self, event):
        """
        jump to prev page
        :param event:
        :return:
        """
        if self.mr_current_page > 1:
            self.mr_current_page -= 1
        else:
            return
        self.mr_update_pic_pages()

    def mr_next_page(self, event):
        """
        jump to next page
        :param event:
        :return:
        """
        if self.mr_current_page < self.mr_total_page:
            self.mr_current_page += 1
        else:
            return
        self.mr_update_pic_pages()

    def mr_jump_page(self, event):
        """
        jump to specified page
        :param event:
        :return:
        """
        try:
            if not self.rcp_text_ctrl.GetValue():
                return
            jump_page = int(self.rcp_text_ctrl.GetValue())
            if jump_page == self.mr_current_page:
                return
            elif jump_page < 1 or jump_page >= self.mr_total_page + 1:
                return
            else:
                self.mr_current_page = jump_page
                self.mr_update_pic_pages()
        except ValueError:
            wx.MessageBox('请输入正确的数字！')
            self.rcp_text_ctrl.Clear()
            self.rcp_text_ctrl.SetFocus()
            return

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
        self.mr_label_dict['tabs'] = tab_list
        if self.rlp_actor_panel.IsShown():
            for rdo in self.rlp_actor_panel.GetChildren():
                if rdo.GetValue():
                    self.mr_label_dict['actor'] = rdo.GetLabel()
        event.Skip()

    def mr_update_pic_pages(self):
        """
        update rider movies' pics
        :return:
        """
        res_tuple = self.movie_task.get_movie_rider_pics(
            self.mr_label_dict, self.mr_pics_per_page, self.mr_current_page)
        self.mr_total_num, self.mr_total_page, self.mr_movie_list = res_tuple
        self.rcp_page_text.SetLabel('%d / %d Pages' % (self.mr_current_page, self.mr_total_page))
        self.load_movie_rider_pictures()

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
        """
        show the picture from the 'right' or 'bottom' direction as well as show a tip window
        :param event:
        :return:
        """
        sb = event.GetEventObject()
        index = list(self.rcp_scrolled_window.GetChildren()).index(sb)
        bitmap = get_fitted_bitmap(self.mr_movie_list[index][1], PICTURE_SIZE['rider'], 'left')
        sb.SetBitmap(bitmap)
        # tw = wx.TipWindow(sb, self.movie_dict['rider']['pics'][index][0])
        # tw.SetBoundingRect(wx.Rect(sb.GetScreenPosition(), sb.GetBitmap().GetSize()))

    def mr_leave_picture(self, event):
        """
        show the picture from the 'left' or 'top' direction
        :param event:
        :return:
        """
        sb = event.GetEventObject()
        index = list(self.rcp_scrolled_window.GetChildren()).index(sb)
        bitmap = get_fitted_bitmap(self.mr_movie_list[index][1], PICTURE_SIZE['rider'], 'right')
        sb.SetBitmap(bitmap)

    def mr_popup_item_selected(self, event):
        """
        deal with selected item
        :param event:
        :return:
        """
        item = self.rcp_popup_menu.FindItemById(event.GetId())

        if item.GetText() == 'Play':
            pass
        elif item.GetText() == 'Detail':
            dl = DetailEditDialog(self)
            dl.ShowModal()
        elif item.GetText() == 'Edit':
            dl = DetailEditDialog(self)
            dl.ShowModal()
        elif item.GetText() == 'Open Dir':
            pass
        elif item.GetText() == 'Delete':
            pass

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
