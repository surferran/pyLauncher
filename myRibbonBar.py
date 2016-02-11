# import wx
# import os
# import sys
#
# import coded_images as          images
# from   coded_images_2   import  *
# import wx.lib.agw.ribbon as RB

from util_functions import *

# --------------------------------------------------- #
# Some constants for ribbon buttons
ID_CIRCLE       = wx.ID_HIGHEST + 1
ID_CROSS        = ID_CIRCLE + 1
ID_TRIANGLE     = ID_CIRCLE + 2
ID_SQUARE       = ID_CIRCLE + 3
ID_POLYGON      = ID_CIRCLE + 4
ID_TOGGLE_PANELS = ID_CIRCLE + 20

def CreateBitmap(xpm):
    bmp = eval(xpm).Bitmap
    return bmp
# --------------------------------------------------- #

class RibbonFrame(wx.Frame):

    def __init__(self, parent, id=wx.ID_ANY, title="", pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, log=None):

        wx.Frame.__init__(self, parent, id, title, pos, size, wx.HORIZONTAL  )
        # wx.Frame.__init__(self, parent, id, title, pos, size, wx.DEFAULT_FRAME_STYLE+wx.NO_BORDER+wx.CAPTION+wx.HORIZONTAL  )

        parent.ribbon_link = self

        panel = wx.Panel(self,wx.EXPAND)
        #
        panel.CanScroll(False)
        #
        self.AlwaysShowScrollbars(False)

        self._ribbon = RB.RibbonBar(panel, wx.ID_ANY, agwStyle=RB.RIBBON_BAR_DEFAULT_STYLE|RB.RIBBON_BAR_SHOW_PANEL_EXT_BUTTONS)

        subj_list = load_user_list()
        # RB_pages = []
        # for idx, value in enumerate(subj_list['item index']):
        #     if value % 1 == 0 :
        #         RB_page  = RB.RibbonPage(self._ribbon, wx.ID_ANY, subj_list['name'][idx], CreateBitmap("ribbon") )
        #         RB_pages.append(RB_page)
        RB_page1 = RB.RibbonPage(self._ribbon, wx.ID_ANY, subj_list['name'][0], (subj_list['image file'][0]) )
        RB_page2 = RB.RibbonPage(self._ribbon, wx.ID_ANY, subj_list['name'][2], (subj_list['image file'][2]) )
        RB_page3 = RB.RibbonPage(self._ribbon, wx.ID_ANY, subj_list['name'][5], (subj_list['image file'][5]) )
        # RB_page2 = RB.RibbonPage(self._ribbon, wx.ID_ANY, subj_list['name'][1], CreateBitmap("ribbon") )


        # # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # #
        # shapes_panel = RB.RibbonPanel(RB_page, wx.ID_ANY, "Shapes", CreateBitmap("circle_small"))
        RB_panel = RB.RibbonPanel(RB_page1, wx.ID_ANY, "items", CreateBitmap("circle_small"))
        RBp_items = RB.RibbonButtonBar(RB_panel)
        RBp_items.AddButton(ID_CIRCLE, "Circle", CreateBitmap("circle"), CreateBitmap("circle_small"),
                         help_string="This is a tooltip for the circle button\ndemonstrating another tooltip",
                         kind=RB.RIBBON_BUTTON_TOGGLE)
        RBp_items.AddSimpleButton(ID_CROSS     , "Cross", CreateBitmap("cross"), "")
        RBp_items.AddHybridButton(ID_TRIANGLE  , "Triangle", CreateBitmap("triangle"))
        RBp_items.AddSimpleButton(ID_SQUARE    , "Square", CreateBitmap("square"), "")
        RBp_items.AddDropdownButton(ID_POLYGON , "Other Polygon", CreateBitmap("hexagon"), "")

        self._ribbon.Realize()
        # # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # #


        self._togglePanels = wx.ToggleButton(panel, ID_TOGGLE_PANELS, "&Toggle panels")
        self._togglePanels.SetValue(True)
    
        s = wx.BoxSizer(wx.VERTICAL)

        s.Add(self._ribbon, 0, wx.EXPAND)
        s.Add(self._togglePanels, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 10)
        panel.SetSizer(s)
        panel.CanScroll(False)
        self.panel = panel

        self.panel.SetSizerAndFit(s)    # one of those is good
        self.SetSizerAndFit(s)          #

        # self.BindEvents([selection, shapes, provider_bar, toolbar_panel])
        RBp_items.Bind(RB.EVT_RIBBONBUTTONBAR_CLICKED              , self.OnCircleButton       , id=ID_CIRCLE)
        RBp_items.Bind(RB.EVT_RIBBONBUTTONBAR_CLICKED              , self.OnCrossButton        , id=ID_CROSS)
        RBp_items.Bind(RB.EVT_RIBBONBUTTONBAR_CLICKED              , self.OnTriangleButton     , id=ID_TRIANGLE)
        RBp_items.Bind(RB.EVT_RIBBONBUTTONBAR_CLICKED              , self.OnSquareButton       ,  id=ID_SQUARE)
        RBp_items.Bind(RB.EVT_RIBBONBUTTONBAR_DROPDOWN_CLICKED     , self.OnTriangleDropdown   , id=ID_TRIANGLE)
        RBp_items.Bind(RB.EVT_RIBBONBUTTONBAR_DROPDOWN_CLICKED     , self.OnPolygonDropdown    , id=ID_POLYGON)

        self._togglePanels.Bind(wx.EVT_TOGGLEBUTTON, self.OnTogglePanels, id=ID_TOGGLE_PANELS)

        self._ribbon.Realize()

        self.SetIcon(images.Mondrian.Icon)
        # self.CenterOnScreen()
        self.Show()

        self._ribbon.ShowPanels(True)

        self._ribbon.RefreshTabBar()
        self.AlwaysShowScrollbars(False)
        self.ShowWithoutActivating()


    def OnCircleButton(self, event):
        print("Circle button clicked.")
    def OnCrossButton(self, event):
        print("Cross button clicked.")


    def OnTriangleButton(self, event):

        print("Triangle button clicked.")


    def OnTriangleDropdown(self, event):

        menu = wx.Menu()
        menu.Append(wx.ID_ANY, "Equilateral")
        menu.Append(wx.ID_ANY, "Isosceles")
        menu.Append(wx.ID_ANY, "Scalene")

        event.PopupMenu(menu)


    def OnSquareButton(self, event):

        print("Square button clicked.")


    def OnPolygonDropdown(self, event):

        menu = wx.Menu()
        menu.Append(wx.ID_ANY, "Pentagon (5 sided)")
        menu.Append(wx.ID_ANY, "Hexagon (6 sided)")
        menu.Append(wx.ID_ANY, "Heptagon (7 sided)")
        menu.Append(wx.ID_ANY, "Octogon (8 sided)")
        menu.Append(wx.ID_ANY, "Nonagon (9 sided)")
        menu.Append(wx.ID_ANY, "Decagon (10 sided)")

        event.PopupMenu(menu)



    def OnTogglePanels(self, event):

        self._ribbon.ShowPanels(self._togglePanels.GetValue())



#---------------------------------------------------------------------------


if __name__ == '__main__':

    class Frame(wx.Frame):
        def __init__(self, title):
            wx.Frame.__init__(self, None, title=title, pos=(150,150), size=(550,200))

    app = wx.App(redirect=False)
    frame = Frame("ribbon main")
    win = RibbonFrame(frame, -1, "wxPython Ribbon Sample Application", size=(570, 200), pos=(950,530))
    win.Show()
    app.MainLoop()


#----------------------------------------------------------------------


