import wx
from fsui.rootframe import RootFrame


class MainWindow(RootFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.show_rider_pictures()

    def show_rider_pictures(self):
        print(self.rcp_scrolled_window.GetSize())
        row_count = (self.rcp_scrolled_window.GetSize()[0] - 10) // 252
        col_count = 30 // row_count
        print(row_count, col_count)
        rcp_pic_sizer = wx.GridSizer(col_count, row_count, 1, 1)
        i = 0
        while i < row_count * col_count:
            picture = wx.BitmapButton(self.rcp_scrolled_window, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                      wx.Size(250, 356), wx.BU_AUTODRAW)
            rcp_pic_sizer.Add(picture, 0, wx.ALL, 1)

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


