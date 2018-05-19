import wx
from fsui.rootframe import RootFrame


class MainWindow(RootFrame):
    def __init__(self, parent):
        super().__init__(parent)
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


