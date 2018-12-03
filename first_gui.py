import wx
app = wx.App()
frm = wx.Frame(None, wx.ID_ANY, title="Hello Python")
frm.Show()
app.MainLoop()
<<<<<<< HEAD
=======

def makeMenuBar(self):
        fileMenu = wx.Menu()
        helloItem = fileMenu.Append(-1, "&Hello...\tCtrl-H",
                                    "Help string shown in status bar")
        fileMenu.AppendSeparator()
        exitItem = fileMenu.Append(wx.ID_EXIT)

        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")
>>>>>>> 8712b4ae7b502503e14f774df90568c0ab226403
