import wx
 
########################################################################
class CustomTaskBarIcon(wx.TaskBarIcon):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, frame):
        """Constructor"""
        wx.TaskBarIcon.__init__(self)
        self.frame = frame
 
        # img = wx.Image("icon.ico",   wx.BITMAP_TYPE_ANY)
        # img = wx.Image("quad.png",   wx.BITMAP_TYPE_ANY)
        img = wx.Image("comp.png",   wx.BITMAP_TYPE_ANY)
        bmp = wx.BitmapFromImage(img)
        self.icon = wx.EmptyIcon()
        self.icon.CopyFromBitmap(bmp)
 
        self.SetIcon(self.icon, "Restore")
        self.Bind(wx.EVT_TASKBAR_LEFT_DOWN, self.OnTaskBarLeftClick)
 
    #----------------------------------------------------------------------
    def OnTaskBarActivate(self, evt):
        """"""
        pass
 
    #----------------------------------------------------------------------
    def OnTaskBarClose(self, evt):
        """
        Destroy the taskbar icon and frame from the taskbar icon itself
        """
        self.frame.Close()
 
    #----------------------------------------------------------------------
    def OnTaskBarLeftClick(self, evt):
        """
        Create the right-click menu
        """
        self.frame.Show()
        self.frame.Restore()