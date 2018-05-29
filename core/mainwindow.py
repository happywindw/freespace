import math
import wx
import settings
from fsui.rootframe import RootFrame


class MainWindow(RootFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.show_rider_pictures(25)

    def show_rider_tabs(self):
        pass

    def show_rider_pictures(self, pic_count=30):
        """
        show pictures
        :param pic_count:
        :return:
        """
        width, height = self.rcp_scrolled_window.GetSize()
        row_count = math.floor((width - 20) / settings.PICTURE_SIZE['rider'][0])
        col_count = math.ceil(pic_count / row_count)
        rcp_pic_sizer = wx.GridSizer(col_count, row_count, 1, 1)

        for i in range(pic_count):
            picture = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                      wx.Size(settings.PICTURE_SIZE['rider']), wx.BU_AUTODRAW)
            rcp_pic_sizer.Add(picture, 0, wx.ALL, 1)
            bitmap = wx.Bitmap('./resource/test.jpg', wx.BITMAP_TYPE_JPEG)
            picture.SetBitmap(bitmap)

        self.rcp_scrolled_window.SetSizer(rcp_pic_sizer)
        self.rcp_scrolled_window.Layout()
        rcp_pic_sizer.Fit(self.rcp_scrolled_window)
        self.Layout()

    def on_mh_about(self, event):
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


