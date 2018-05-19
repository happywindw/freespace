import wx
from core.mainwindow import MainWindow

fs_app = wx.App(False)
fs_main_window = MainWindow(None)
fs_main_window.Show()
fs_app.MainLoop()
