import wx


class MainNotebook(wx.Notebook):
    def __init__(self, parent):
        super().__init__(parent, id=wx.ID_ANY, style=wx.BK_DEFAULT)
