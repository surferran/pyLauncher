import wx
import os
import sys

import coded_images as          images
from   coded_images_2   import  *
import wx.lib.agw.ribbon as RB


# --------------------------------------------------- #
# Some constants for ribbon buttons
ID_CIRCLE       = wx.ID_HIGHEST + 1
ID_CROSS        = ID_CIRCLE + 1
ID_TRIANGLE     = ID_CIRCLE + 2
ID_SQUARE       = ID_CIRCLE + 3
ID_POLYGON      = ID_CIRCLE + 4
ID_TOGGLE_PANELS = ID_CIRCLE + 20

Strings = ["Project1",
           "Project2"]

def CreateBitmap(xpm):
    bmp = eval(xpm).Bitmap
    return bmp
# --------------------------------------------------- #

class RibbonFrame(wx.Frame):

    def __init__(self, parent, id=wx.ID_ANY, title="", pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, log=None):

        wx.Frame.__init__(self, parent, id, title, pos, size, wx.DEFAULT_FRAME_STYLE+wx.NO_BORDER+wx.CAPTION+wx.HORIZONTAL  )

        parent.ribbon_link = self

        panel = wx.Panel(self,wx.EXPAND)
        # panel.CanScroll(False)
        # self.AlwaysShowScrollbars(False)
        self._ribbon = RB.RibbonBar(panel, wx.ID_ANY, agwStyle=RB.RIBBON_BAR_DEFAULT_STYLE|RB.RIBBON_BAR_SHOW_PANEL_EXT_BUTTONS)

        # self._bitmap_creation_dc = wx.MemoryDC()
        # self._colour_data = wx.ColourData()
        
        home  = RB.RibbonPage(self._ribbon, wx.ID_ANY, Strings[0], CreateBitmap("ribbon") )
        home2 = RB.RibbonPage(self._ribbon, wx.ID_ANY, Strings[1], CreateBitmap("ribbon") )


        # # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # ## # #
        shapes_panel = RB.RibbonPanel(home, wx.ID_ANY, "Shapes", CreateBitmap("circle_small"))
        shapes = RB.RibbonButtonBar(shapes_panel)
        shapes.AddButton(ID_CIRCLE, "Circle", CreateBitmap("circle"), CreateBitmap("circle_small"),
                         help_string="This is a tooltip for the circle button\ndemonstrating another tooltip",
                         kind=RB.RIBBON_BUTTON_TOGGLE)
        shapes.AddSimpleButton(ID_CROSS     , "Cross", CreateBitmap("cross"), "")
        shapes.AddHybridButton(ID_TRIANGLE  , "Triangle", CreateBitmap("triangle"))
        shapes.AddSimpleButton(ID_SQUARE    , "Square", CreateBitmap("square"), "")
        shapes.AddDropdownButton(ID_POLYGON , "Other Polygon", CreateBitmap("hexagon"), "")

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
        shapes.Bind(RB.EVT_RIBBONBUTTONBAR_CLICKED              , self.OnCircleButton       , id=ID_CIRCLE)
        shapes.Bind(RB.EVT_RIBBONBUTTONBAR_CLICKED              , self.OnCrossButton        , id=ID_CROSS)
        shapes.Bind(RB.EVT_RIBBONBUTTONBAR_CLICKED              , self.OnTriangleButton     , id=ID_TRIANGLE)
        shapes.Bind(RB.EVT_RIBBONBUTTONBAR_CLICKED              , self.OnSquareButton       ,  id=ID_SQUARE)
        shapes.Bind(RB.EVT_RIBBONBUTTONBAR_DROPDOWN_CLICKED     , self.OnTriangleDropdown   , id=ID_TRIANGLE)
        shapes.Bind(RB.EVT_RIBBONBUTTONBAR_DROPDOWN_CLICKED     , self.OnPolygonDropdown    , id=ID_POLYGON)

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
    app = wx.App(redirect=False)
    win = RibbonFrame(None, -1, "wxPython Ribbon Sample Application", size=(270, 200), pos=(950,530))
    win.Show()
    app.MainLoop()


#----------------------------------------------------------------------


