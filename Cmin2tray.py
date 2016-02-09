import wx

TRAY_TOOLTIP = ' -- application MyLauncher -- '  #"restore"
TRAY_ICON  = '.\IMAGES\icon.ico'
TRAY_ICONs = [TRAY_ICON , '.\IMAGES\quad.png']


def create_menu_item(menu, label, func, icon_ndx=0):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    item.SetBitmap(wx.Bitmap(TRAY_ICONs[icon_ndx]))
    menu.AppendItem(item)
    return item

########################################################################
class CustomTaskBarIcon(wx.TaskBarIcon):
    """"""
    #----------------------------------------------------------------------
    def __init__(self, frame):
        """Constructor"""
        wx.TaskBarIcon.__init__(self)
        self.frame = frame

        img = wx.Image(TRAY_ICON,   wx.BITMAP_TYPE_ANY)
        bmp = wx.BitmapFromImage(img)
        self.icon = wx.EmptyIcon()
        self.icon.CopyFromBitmap(bmp)   # = wx.IconFromBitmap(wx.Bitmap(path))
 
        self.SetIcon(self.icon, TRAY_TOOLTIP)

        self.Bind(wx.EVT_TASKBAR_LEFT_DOWN, self.OnTaskBarLeftClick)
 
    #----------------------------------------------------------------------

    def CreatePopupMenu(self):
        menu = wx.Menu()
        create_menu_item(menu, 'Say func1', self.func_call_1 , icon_ndx=1)
        menu.AppendSeparator()
        create_menu_item(menu, 'Exit', self.func_call_exit, icon_ndx=0)
        return menu

    def OnTaskBarActivate(self, evt):
        """"""
        print "ACTIVATED"
        pass
 
    #----------------------------------------------------------------------
    def OnTaskBarClose(self, evt):
        """
        Destroy the taskbar icon and frame from the taskbar icon itself
        """
        print "CLOSING"
        self.frame.Close()
 
    #----------------------------------------------------------------------
    def OnTaskBarLeftClick(self, evt):
        """
        Create the right-click menu
        """
        print 'Tray icon was left-clicked.'
        self.frame.Show()
        self.frame.Restore()

    def func_call_1(self, event):
        print "func1 entered"

    def func_call_exit(self, event):
        print "pressed exit"
        # wx.CallAfter(self.Destroy)
        self.frame.Close()
        self.Destroy()