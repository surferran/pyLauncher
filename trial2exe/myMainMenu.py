# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class LauncherFrame
###########################################################################

class LauncherFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHT ) )
		
		bSizer11 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button1 = wx.Button( self.m_panel1, wx.ID_ANY, u"Projects", wx.DefaultPosition, wx.Size( -1,50 ), 0 )
		bSizer11.Add( self.m_button1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button2 = wx.Button( self.m_panel1, wx.ID_ANY, u"typical Web sites", wx.DefaultPosition, wx.Size( -1,50 ), 0 )
		bSizer11.Add( self.m_button2, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( bSizer11 )
		self.m_panel1.Layout()
		bSizer11.Fit( self.m_panel1 )
		bSizer9.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button11 = wx.Button( self.m_panel2, wx.ID_ANY, u"3D stereo cam", wx.DefaultPosition, wx.Size( -1,50 ), 0 )
		bSizer1.Add( self.m_button11, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button21 = wx.Button( self.m_panel2, wx.ID_ANY, u"Aero cam (IBM)", wx.DefaultPosition, wx.Size( -1,50 ), 0 )
		bSizer1.Add( self.m_button21, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel2.SetSizer( bSizer1 )
		self.m_panel2.Layout()
		bSizer1.Fit( self.m_panel2 )
		bSizer9.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer9 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.btn_1_func )
		self.m_button2.Bind( wx.EVT_BUTTON, self.btn_2_func )
		self.m_button11.Bind( wx.EVT_BUTTON, self.btn_3_func )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btn_1_func( self, event ):
		event.Skip()
	
	def btn_2_func( self, event ):
		event.Skip()
	
	def btn_3_func( self, event ):
		event.Skip()
	

###########################################################################
## Class webSitesFrame
###########################################################################

class webSitesFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_WebLinks_listCtrl = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_EDIT_LABELS|wx.LC_LIST|wx.RAISED_BORDER, wx.DefaultValidator, u"web links" )
		bSizer4.Add( self.m_WebLinks_listCtrl, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

