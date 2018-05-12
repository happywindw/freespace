import wx
from fsui.rootframe import RootFrame


class MainWindow(RootFrame):
    def __init__(self, parent):
        super().__init__(parent)
        pass

    def mh_about(self, event):
        wx.MessageBox('Hello, welcome to free space!')

