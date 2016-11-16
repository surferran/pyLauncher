import wx
import win32con #for the VK keycodes

class FrameWithHotKey(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.regHotKey()
        self.Bind(wx.EVT_HOTKEY, self.handleHotKey, id=self.hotKeyId)
    def regHotKey(self):
        """
        This function registers the hotkey Alt+F1 with id=100
        """
        self.hotKeyId = 100
        self.RegisterHotKey(
            self.hotKeyId, #a unique ID for this hotkey
            win32con.MOD_ALT, #the modifier key
            win32con.VK_F1) #the key to watch for
    def handleHotKey(self, evt):
        """
        Prints a simple message when a hotkey event is received.
        """
        print "do hot key actions"
