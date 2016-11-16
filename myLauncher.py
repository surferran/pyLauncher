# myLauncher app
# by Ran
# last update on 10/02/16
#
# TODO:  22/01/16
# add text field in the 2nd panel
# compile to exe stand alone
# try py2web to see what it gives.
# think about put in GiHub as well 

##
'''
'''
##
from myImports import *

myGlobals = {}
myGlobals['user_dict']      = {}
myGlobals['emptyFrame#2']   = 'true'

#inherit from the MainFrame created in wxFowmBuilder and create CalcFrame
class LauncherFrame(myGUI_Frames.LauncherFrame):
    #constructor
    def __init__(self,parent):

        # # read user file: ( read-only mode by default )
        # f_name = myGlobals['user_path'] + myGlobals['user_file']
        # f = open(  f_name )
        # # read all the lines in the file and return them in a list
        # lines = f.readlines()
        # f.close()
        # if MY_DEBUG :
        #     print lines

        # table = pd.read_table(f_name ) #, sep='|')
        # print table

        conf = json.load(open('./USER_data/conf.json.txt'))
        print conf

        #initialize parent class
        myGUI_Frames.LauncherFrame.__init__(self,parent) # defined by the wx.Builder.class in outer file
        LauncherFrame.btn_3_func(self,None)

        self.tbIcon = Cmin2tray.CustomTaskBarIcon(self)

        self.Bind(wx.EVT_ICONIZE, self.onMinimize)
        self.Bind(wx.EVT_CLOSE  , self.onClose)

        self.state = 'regular_shown'
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
        print "closing main frame"

        tmp = self.ribbon_link
        tmp.Close()
        tmp.Destroy()

        # if myGlobals['emptyFrame#2'] != 'true':
        frame2.Close()
        frame2.Destroy()
        print " closed the #2nd frame "

    def onMinimize(self, event):
        """
        When minimizing, hide the frame so it "minimizes to tray"
        """
        self.Hide()
    #----------------------------------------------------------------------

class webSitesFrame(myGUI_Frames.webSitesFrame):
    #constructor
    def __init__(self,parent):
        #initialize parent class
        myGUI_Frames.webSitesFrame.__init__(self,parent) # defined by the wx.Builder.class in outer file
        self.Bind(wx.EVT_CLOSE  , self.onClose)
        self.SetBackgroundColour(wx.YELLOW)
        '''# self.m_WebLinks_listCtrl.SetDropTarget'''
        myGlobals['emptyFrame#2'] = 'false'

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
        '''# self.m_WebLinks_listCtrl.SetDropTarget(self.OnDropText) '''

    def OnDropText(self, x, y, data):
        """ Implement Text Drop """
        print "func: Text Drop"

    def onClose(self, evt):
        self.Hide()
        myGlobals['emptyFrame#2'] = 'true'
        print "frame 2nd is hidden"
        pass



app     = wx.App(False)
frame   = LauncherFrame(None)
frame2  = webSitesFrame(None)
frame2.add_to_list('new new test')
win     = myRibbonBar.RibbonFrame(frame, -1, "wxPython Ribbon Sample Application", size=(270, 200), pos=(950,530))
win.Show(False)

# frame   =
frame.Show(True)
app.MainLoop()