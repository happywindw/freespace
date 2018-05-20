import wx
from fsui.rootframe import RootFrame


class MainWindow(RootFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.show_rider_pictures()

    def show_rider_pictures(self):
        rcp_pic_sizer = wx.GridSizer(2, 6, 0, 0)
        i = 0
        while i < 7:
            picture = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                      wx.Size(250, 356), wx.BU_AUTODRAW)
            rcp_pic_sizer.Add(picture, 0, wx.ALL, 5)

            bitmap = wx.Bitmap('./resource/test.jpg', wx.BITMAP_TYPE_JPEG)
            picture.SetBitmap(bitmap)
            i += 1

        self.rcp_scrolled_window.SetSizer(rcp_pic_sizer)
        self.rcp_scrolled_window.Layout()
        rcp_pic_sizer.Fit(self.rcp_scrolled_window)

    def on_mh_about(self, event):
        wx.MessageBox('Hello, welcome to free space!')

    def on_mm_add_movie(self, event):
        fd = wx.FileDialog(self, 'Add a Single Video File')
        if fd.ShowModal() == wx.ID_OK:
            print('ssss')
        fd.Destroy()

    def on_mm_add_movie_folder(self, event):
        print('here')
        pass


