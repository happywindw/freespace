import wx
from fsui.rootframe import RootFrame


class MainWindow(RootFrame):
    def __init__(self, parent):
        super().__init__(parent)
        rider_pic_list = [self.rcp_pic_01, self.rcp_pic_02, self.rcp_pic_03, self.rcp_pic_04, self.rcp_pic_05,
                          self.rcp_pic_06, self.rcp_pic_07, self.rcp_pic_08, self.rcp_pic_09, self.rcp_pic_10,
                          self.rcp_pic_11, self.rcp_pic_12, self.rcp_pic_13, self.rcp_pic_14, self.rcp_pic_15,
                          self.rcp_pic_16, self.rcp_pic_17, self.rcp_pic_18, self.rcp_pic_19, self.rcp_pic_20,
                          self.rcp_pic_21, self.rcp_pic_22, self.rcp_pic_23, self.rcp_pic_24, self.rcp_pic_25,
                          self.rcp_pic_26, self.rcp_pic_27, self.rcp_pic_28, self.rcp_pic_29, self.rcp_pic_30]
        for pic in rider_pic_list:
            bitmap = wx.Bitmap('./resource/test.jpg', wx.BITMAP_TYPE_JPEG)
            pic.SetBitmap(bitmap)
        pass

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


