# minimize example are taken from : http://www.blog.pythonlibrary.org/2013/07/12/wxpython-how-to-minimize-to-system-tray/
# GUI settings are created with wxFormBuilder.
# icons from https://www.iconexperience.com/o_collection/icons/?icon=bridge&color_style=green_dark_grey 
#            http://en.miankoutu.com/zt-8359-1.html 
#
# TODO:  22/01/16
# add text field in the 2nd panel
# compile to exe stand alone
# try py2web to see what it gives.
# think about put in GiHub as well 

import wx, os
import myMainMenu
import Cmin2tray

#inherit from the MainFrame created in wxFowmBuilder and create CalcFrame
class LauncherFrame(myMainMenu.LauncherFrame):
    #constructor
    def __init__(self,parent):
        #initialize parent class
        myMainMenu.LauncherFrame.__init__(self,parent) # defined by the wx.Builder.class in outer file
        LauncherFrame.btn_3_func(self,None)

        self.tbIcon = Cmin2tray.CustomTaskBarIcon(self)

        self.Bind(wx.EVT_ICONIZE, self.onMinimize)
        self.Bind(wx.EVT_CLOSE  , self.onClose)
        # myMainMenu.m_panel1.ShowYourself()
        # myMainMenu.LauncherFrame.m_panel2.Show()
        # myMainMenu.LauncherFrame.

        # myMainMenu.projectsFrame.Hide(self)

    def btn_1_func(self,event):
        print "func: btn_1_func"
        self.m_panel1.Hide()
        self.m_panel2.Show()

    def btn_2_func(self,event):
        print "func: btn_2_func"
        frame2.Show()

    def btn_3_func(self,event):
        print "func: btn_3_func"
        self.m_panel2.Hide()
        self.m_panel1.Show()
    def onClose(self, evt):
        """
        Destroy the taskbar icon and the frame
        """
        self.tbIcon.RemoveIcon()
        self.tbIcon.Destroy()
        self.Destroy()

        frame2.Close()

    #----------------------------------------------------------------------
    def onMinimize(self, event):
        """
        When minimizing, hide the frame so it "minimizes to tray"
        """
        self.Hide()

class webSitesFrame(myMainMenu.webSitesFrame):
    #constructor
    def __init__(self,parent):
        #initialize parent class
        myMainMenu.webSitesFrame.__init__(self,parent) # defined by the wx.Builder.class in outer file
        self.SetBackgroundColour(wx.YELLOW)
        self.m_WebLinks_listCtrl.SetDropTarget

    def add_to_list(self,txt):
        print "func: add to list"

        files_table_w_h = (450, 250)

        self.m_WebLinks_listCtrl.Size = files_table_w_h

        files = os.listdir('.')

        # self.list_ctrl.InsertColumn(0, 'Name')
        # self.list_ctrl.SetColumnWidth(0, 120)

        j = 0
        for i in files:
            (name, ext) = os.path.splitext(i)
            self.m_WebLinks_listCtrl.InsertStringItem(j, name)
            # if (j % 2) == 0:
            #     self.m_WebLinks_listCtrl.SetItemBackgroundColour(j, '#e6f1f5')
            j = j + 1

    def OnDropText(self, x, y, data):
        """ Implement Text Drop """
        print "func: Text Drop"

    def onClose(self, evt):
        self.Hide()
        pass

app     = wx.App(False)
frame   = LauncherFrame(None)
frame2  = webSitesFrame(None)
frame2.add_to_list('new new test')

# frame   =
frame.Show(True)
app.MainLoop()