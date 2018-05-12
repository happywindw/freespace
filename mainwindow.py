import wx
from fsui.rootframe import RootFrame


class MainWindow(RootFrame):
    def __init__(self, parent):
        super().__init__(parent)
        pass

    def mh_about(self, event):
        wx.MessageBox('Hello, welcome to free space!')


# for test
fs_app = wx.App(False)
fs_main_window = MainWindow(None)
fs_main_window.Show()
fs_app.MainLoop()

