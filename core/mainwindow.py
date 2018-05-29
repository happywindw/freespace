import math
import wx
import settings
from fsui.rootframe import RootFrame


class MainWindow(RootFrame):
    def __init__(self, parent):
        super().__init__(parent)
        tl = ['你好', '我不知道', '是的吗', '再见', '我要爬山去', '这是个问题', '过来', '一起么', '哈哈哈哈哈']
        self.show_rider_contents(tl, 25)

    def show_rider_contents(self, tl, pic_count=30):
        """
        show rider tab content
        :param tl:
        :param pic_count:
        :return:
        """
        # show widgets on rlp_tabs_panel
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

    def on_mh_about(self, event):
        """
        menu->help->about
        :param event:
        :return:
        """
        md = wx.MessageDialog(self, 'FreeSpace v1.0\n©2018-2019 Louis Young. All Rights Reserved.',
                              'About FreeSpace', wx.OK | wx.ICON_QUESTION)
        md.ShowModal()
        md.Destroy()

    def on_mm_add_movie(self, event):
        fd = wx.FileDialog(self, 'Add a Single Video File')
        if fd.ShowModal() == wx.ID_OK:
            print('ssss')
        fd.Destroy()

    def on_mm_add_movie_folder(self, event):
        print('here')
        pass

