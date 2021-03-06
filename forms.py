# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb 16 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Scoter", pos = wx.DefaultPosition, size = wx.Size( 981,643 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.Notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DataPanel0 = wx.Panel( self.Notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.ControlPanel00 = wx.Panel( self.DataPanel0, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText31 = wx.StaticText( self.ControlPanel00, wx.ID_ANY, u"δ18O record", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		bSizer7.Add( self.m_staticText31, 0, wx.ALIGN_CENTER|wx.RIGHT, 5 )
		
		self.button_read_d18o_record = wx.Button( self.ControlPanel00, wx.ID_ANY, u"Read", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.button_read_d18o_record, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.button_clear_d18o_record = wx.Button( self.ControlPanel00, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.button_clear_d18o_record, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText32 = wx.StaticText( self.ControlPanel00, wx.ID_ANY, u"Limits", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		bSizer7.Add( self.m_staticText32, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )
		
		self.text_d18o_record_start = wx.TextCtrl( self.ControlPanel00, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer7.Add( self.text_d18o_record_start, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )
		
		self.text_d18o_record_end = wx.TextCtrl( self.ControlPanel00, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer7.Add( self.text_d18o_record_end, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.text_d18o_record_filename = wx.TextCtrl( self.ControlPanel00, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RIGHT )
		self.text_d18o_record_filename.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer7.Add( self.text_d18o_record_filename, 1, wx.ALL, 5 )
		
		
		self.ControlPanel00.SetSizer( bSizer7 )
		self.ControlPanel00.Layout()
		bSizer7.Fit( self.ControlPanel00 )
		bSizer2.Add( self.ControlPanel00, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.DataPanel00 = wx.Panel( self.DataPanel0, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.DataPanel00.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		
		self.DataPanel00.SetSizer( bSizer5 )
		self.DataPanel00.Layout()
		bSizer5.Fit( self.DataPanel00 )
		bSizer2.Add( self.DataPanel00, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.ControlPanel01 = wx.Panel( self.DataPanel0, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText311 = wx.StaticText( self.ControlPanel01, wx.ID_ANY, u"δ18O target", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText311.Wrap( -1 )
		bSizer20.Add( self.m_staticText311, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )
		
		self.button_read_d18o_target = wx.Button( self.ControlPanel01, wx.ID_ANY, u"Read", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.button_read_d18o_target, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.button_clear_d18o_target = wx.Button( self.ControlPanel01, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.button_clear_d18o_target, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText321 = wx.StaticText( self.ControlPanel01, wx.ID_ANY, u"Limits", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText321.Wrap( -1 )
		bSizer20.Add( self.m_staticText321, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )
		
		self.text_d18o_target_start = wx.TextCtrl( self.ControlPanel01, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer20.Add( self.text_d18o_target_start, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )
		
		self.text_d18o_target_end = wx.TextCtrl( self.ControlPanel01, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer20.Add( self.text_d18o_target_end, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.text_d18o_target_filename = wx.TextCtrl( self.ControlPanel01, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RIGHT )
		bSizer20.Add( self.text_d18o_target_filename, 1, wx.ALL, 5 )
		
		
		self.ControlPanel01.SetSizer( bSizer20 )
		self.ControlPanel01.Layout()
		bSizer20.Fit( self.ControlPanel01 )
		bSizer2.Add( self.ControlPanel01, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.DataPanel01 = wx.Panel( self.DataPanel0, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.DataPanel01.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		
		self.DataPanel01.SetSizer( bSizer6 )
		self.DataPanel01.Layout()
		bSizer6.Fit( self.DataPanel01 )
		bSizer2.Add( self.DataPanel01, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.DataPanel0.SetSizer( bSizer2 )
		self.DataPanel0.Layout()
		bSizer2.Fit( self.DataPanel0 )
		self.Notebook.AddPage( self.DataPanel0, u"δ18O data", False )
		self.DataPanel1 = wx.Panel( self.Notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer21 = wx.BoxSizer( wx.VERTICAL )
		
		self.ControlPanel001 = wx.Panel( self.DataPanel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer71 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText43 = wx.StaticText( self.ControlPanel001, wx.ID_ANY, u"RPI record", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )
		bSizer71.Add( self.m_staticText43, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )
		
		self.button_read_rpi_record = wx.Button( self.ControlPanel001, wx.ID_ANY, u"Read", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer71.Add( self.button_read_rpi_record, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.button_clear_rpi_record = wx.Button( self.ControlPanel001, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer71.Add( self.button_clear_rpi_record, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText44 = wx.StaticText( self.ControlPanel001, wx.ID_ANY, u"Limits", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )
		bSizer71.Add( self.m_staticText44, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )
		
		self.text_rpi_record_start = wx.TextCtrl( self.ControlPanel001, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer71.Add( self.text_rpi_record_start, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.text_rpi_record_end = wx.TextCtrl( self.ControlPanel001, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer71.Add( self.text_rpi_record_end, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.text_rpi_record_filename = wx.TextCtrl( self.ControlPanel001, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RIGHT )
		bSizer71.Add( self.text_rpi_record_filename, 1, wx.ALL, 5 )
		
		
		self.ControlPanel001.SetSizer( bSizer71 )
		self.ControlPanel001.Layout()
		bSizer71.Fit( self.ControlPanel001 )
		bSizer21.Add( self.ControlPanel001, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.DataPanel10 = wx.Panel( self.DataPanel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.DataPanel10.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer51 = wx.BoxSizer( wx.VERTICAL )
		
		
		self.DataPanel10.SetSizer( bSizer51 )
		self.DataPanel10.Layout()
		bSizer51.Fit( self.DataPanel10 )
		bSizer21.Add( self.DataPanel10, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel271 = wx.Panel( self.DataPanel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer201 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText46 = wx.StaticText( self.m_panel271, wx.ID_ANY, u"RPI target", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )
		bSizer201.Add( self.m_staticText46, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.button_read_rpi_target = wx.Button( self.m_panel271, wx.ID_ANY, u"Read", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer201.Add( self.button_read_rpi_target, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )
		
		self.button_clear_rpi_target = wx.Button( self.m_panel271, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer201.Add( self.button_clear_rpi_target, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )
		
		self.m_staticText47 = wx.StaticText( self.m_panel271, wx.ID_ANY, u"Limits", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )
		bSizer201.Add( self.m_staticText47, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.text_rpi_target_start = wx.TextCtrl( self.m_panel271, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer201.Add( self.text_rpi_target_start, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.text_rpi_target_end = wx.TextCtrl( self.m_panel271, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer201.Add( self.text_rpi_target_end, 0, wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.text_rpi_target_filename = wx.TextCtrl( self.m_panel271, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_RIGHT )
		bSizer201.Add( self.text_rpi_target_filename, 1, wx.ALL, 5 )
		
		
		self.m_panel271.SetSizer( bSizer201 )
		self.m_panel271.Layout()
		bSizer201.Fit( self.m_panel271 )
		bSizer21.Add( self.m_panel271, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.DataPanel11 = wx.Panel( self.DataPanel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.DataPanel11.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer61 = wx.BoxSizer( wx.VERTICAL )
		
		
		self.DataPanel11.SetSizer( bSizer61 )
		self.DataPanel11.Layout()
		bSizer61.Fit( self.DataPanel11 )
		bSizer21.Add( self.DataPanel11, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.DataPanel1.SetSizer( bSizer21 )
		self.DataPanel1.Layout()
		bSizer21.Fit( self.DataPanel1 )
		self.Notebook.AddPage( self.DataPanel1, u"RPI data", False )
		self.PreprocessingPanel = wx.Panel( self.Notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer24 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel25 = wx.Panel( self.PreprocessingPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel25, wx.ID_ANY, u"General" ), wx.VERTICAL )
		
		self.m_panel26 = wx.Panel( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1 = wx.FlexGridSizer( 4, 2, 0, 0 )
		fgSizer1.AddGrowableCol( 1 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText3 = wx.StaticText( self.m_panel26, wx.ID_ANY, u"Detrending", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer1.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.LEFT, 5 )
		
		preproc_detrendChoices = [ u"None", u"Subtract mean", u"Linear detrend" ]
		self.preproc_detrend = wx.Choice( self.m_panel26, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, preproc_detrendChoices, 0 )
		self.preproc_detrend.SetSelection( 0 )
		fgSizer1.Add( self.preproc_detrend, 0, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self.m_panel26, wx.ID_ANY, u"Normalization", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer1.Add( self.m_staticText6, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.LEFT, 5 )
		
		self.preproc_normalize = wx.CheckBox( self.m_panel26, wx.ID_ANY, u"Normalize", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.preproc_normalize.SetValue(True) 
		fgSizer1.Add( self.preproc_normalize, 0, wx.ALL, 5 )
		
		self.m_staticText29 = wx.StaticText( self.m_panel26, wx.ID_ANY, u"δ18O weighting", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		fgSizer1.Add( self.m_staticText29, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.LEFT, 5 )
		
		self.preproc_weight_d18o = wx.TextCtrl( self.m_panel26, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.preproc_weight_d18o, 0, wx.ALL, 5 )
		
		self.m_staticText291 = wx.StaticText( self.m_panel26, wx.ID_ANY, u"RPI weighting", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText291.Wrap( -1 )
		fgSizer1.Add( self.m_staticText291, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.LEFT, 5 )
		
		self.preproc_weight_rpi = wx.TextCtrl( self.m_panel26, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.preproc_weight_rpi, 0, wx.ALL, 5 )
		
		
		self.m_panel26.SetSizer( fgSizer1 )
		self.m_panel26.Layout()
		fgSizer1.Fit( self.m_panel26 )
		sbSizer3.Add( self.m_panel26, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel25.SetSizer( sbSizer3 )
		self.m_panel25.Layout()
		sbSizer3.Fit( self.m_panel25 )
		bSizer24.Add( self.m_panel25, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel28 = wx.Panel( self.PreprocessingPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel28, wx.ID_ANY, u"Interpolation" ), wx.VERTICAL )
		
		self.m_panel30 = wx.Panel( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer6 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText27 = wx.StaticText( self.m_panel30, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )
		fgSizer6.Add( self.m_staticText27, 0, wx.ALL, 5 )
		
		self.preproc_interp_active = wx.CheckBox( self.m_panel30, wx.ID_ANY, u"Use interpolation", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.preproc_interp_active, 0, wx.ALL, 5 )
		
		self.m_staticText28 = wx.StaticText( self.m_panel30, wx.ID_ANY, u"Type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		fgSizer6.Add( self.m_staticText28, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.LEFT, 5 )
		
		preproc_interp_typeChoices = [ u"linear", u"nearest", u"zero", u"slinear", u"quadratic", u"cubic" ]
		self.preproc_interp_type = wx.Choice( self.m_panel30, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, preproc_interp_typeChoices, 0 )
		self.preproc_interp_type.SetSelection( 0 )
		fgSizer6.Add( self.preproc_interp_type, 0, wx.ALL, 5 )
		
		self.m_staticText7121 = wx.StaticText( self.m_panel30, wx.ID_ANY, u"Number of points", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7121.Wrap( -1 )
		fgSizer6.Add( self.m_staticText7121, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.LEFT, 5 )
		
		self.m_panel13 = wx.Panel( self.m_panel30, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.preproc_interp_min = wx.RadioButton( self.m_panel13, wx.ID_ANY, u"Minimum", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.preproc_interp_min.SetToolTipString( u"Interpolate to the minimum number of points in any of the data-sets" )
		
		bSizer12.Add( self.preproc_interp_min, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.preproc_interp_max = wx.RadioButton( self.m_panel13, wx.ID_ANY, u"Maximum", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.preproc_interp_max, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer12.AddSpacer( ( 16, 0), 0, 0, 5 )
		
		self.preproc_interp_explicit = wx.RadioButton( self.m_panel13, wx.ID_ANY, u"Custom:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.preproc_interp_explicit.SetToolTipString( u"Interpolate to the specified number of points" )
		
		bSizer12.Add( self.preproc_interp_explicit, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.preproc_interp_npoints = wx.SpinCtrl( self.m_panel13, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, 0, 1000000, 0 )
		bSizer12.Add( self.preproc_interp_npoints, 0, wx.ALL, 5 )
		
		self.m_staticText19 = wx.StaticText( self.m_panel13, wx.ID_ANY, u"points", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		bSizer12.Add( self.m_staticText19, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		self.m_panel13.SetSizer( bSizer12 )
		self.m_panel13.Layout()
		bSizer12.Fit( self.m_panel13 )
		fgSizer6.Add( self.m_panel13, 1, wx.EXPAND, 5 )
		
		
		self.m_panel30.SetSizer( fgSizer6 )
		self.m_panel30.Layout()
		fgSizer6.Fit( self.m_panel30 )
		sbSizer5.Add( self.m_panel30, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel28.SetSizer( sbSizer5 )
		self.m_panel28.Layout()
		sbSizer5.Fit( self.m_panel28 )
		bSizer24.Add( self.m_panel28, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.PreprocessingPanel.SetSizer( bSizer24 )
		self.PreprocessingPanel.Layout()
		bSizer24.Fit( self.PreprocessingPanel )
		self.Notebook.AddPage( self.PreprocessingPanel, u"Preprocessing", False )
		self.panel_correlate = wx.Panel( self.Notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel17 = wx.Panel( self.panel_correlate, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel17, wx.ID_ANY, u"Simulated Annealing" ), wx.VERTICAL )
		
		self.corr_sa_active = wx.CheckBox( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Use simulated annealing", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer2.Add( self.corr_sa_active, 0, wx.ALL, 5 )
		
		fgSizer2 = wx.FlexGridSizer( 0, 6, 0, 10 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText191 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Number of intervals", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText191.Wrap( -1 )
		fgSizer2.Add( self.m_staticText191, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.corr_sa_intervals = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.corr_sa_intervals, 0, wx.BOTTOM|wx.RIGHT|wx.TOP, 5 )
		
		self.m_staticText12 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Initial temperature", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		fgSizer2.Add( self.m_staticText12, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.corr_sa_temp_init = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.corr_sa_temp_init, 0, wx.BOTTOM|wx.RIGHT|wx.TOP, 5 )
		
		self.m_staticText13 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Final temperature", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		fgSizer2.Add( self.m_staticText13, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.LEFT, 5 )
		
		self.corr_sa_temp_final = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.corr_sa_temp_final, 0, wx.BOTTOM|wx.RIGHT|wx.TOP, 5 )
		
		self.m_staticText14 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Cooling rate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		fgSizer2.Add( self.m_staticText14, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.corr_sa_cooling = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.corr_sa_cooling, 0, wx.BOTTOM|wx.RIGHT|wx.TOP, 5 )
		
		self.m_staticText15 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Changes threshold", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		fgSizer2.Add( self.m_staticText15, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.LEFT, 5 )
		
		self.corr_sa_max_changes = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.corr_sa_max_changes, 0, wx.BOTTOM|wx.RIGHT|wx.TOP, 5 )
		
		self.m_staticText16 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Steps threshold", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		fgSizer2.Add( self.m_staticText16, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.corr_sa_max_steps = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.corr_sa_max_steps, 0, wx.BOTTOM|wx.RIGHT|wx.TOP, 5 )
		
		self.m_staticText151 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Random seed", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText151.Wrap( -1 )
		fgSizer2.Add( self.m_staticText151, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.LEFT, 5 )
		
		self.corr_sa_seed = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.corr_sa_seed, 0, wx.BOTTOM|wx.RIGHT|wx.TOP, 5 )
		
		self.m_staticText161 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Rate change penalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText161.Wrap( -1 )
		fgSizer2.Add( self.m_staticText161, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.BOTTOM|wx.LEFT|wx.TOP, 5 )
		
		self.corr_sa_rc_penalty = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.corr_sa_rc_penalty, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.BOTTOM|wx.RIGHT|wx.TOP, 5 )
		
		self.m_staticText17 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Maximum rate", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		fgSizer2.Add( self.m_staticText17, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.LEFT, 5 )
		
		self.corr_sa_max_rate = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.corr_sa_max_rate, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.RIGHT, 5 )
		
		
		sbSizer2.Add( fgSizer2, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel17.SetSizer( sbSizer2 )
		self.m_panel17.Layout()
		sbSizer2.Fit( self.m_panel17 )
		bSizer14.Add( self.m_panel17, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.panel_match = wx.Panel( self.panel_correlate, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sbSizer21 = wx.StaticBoxSizer( wx.StaticBox( self.panel_match, wx.ID_ANY, u"Match" ), wx.VERTICAL )
		
		self.corr_match_active = wx.CheckBox( sbSizer21.GetStaticBox(), wx.ID_ANY, u"Use Match", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer21.Add( self.corr_match_active, 0, wx.ALL, 5 )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.corr_match_guess_button = wx.RadioButton( sbSizer21.GetStaticBox(), wx.ID_ANY, u"Guess location of Match program", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP )
		gbSizer1.Add( self.corr_match_guess_button, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.corr_match_specify_button = wx.RadioButton( sbSizer21.GetStaticBox(), wx.ID_ANY, u"Specify location:", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.corr_match_specify_button, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )
		
		self.corr_match_guessed_path = wx.TextCtrl( sbSizer21.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.corr_match_guessed_path.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		gbSizer1.Add( self.corr_match_guessed_path, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 7 ), wx.ALL|wx.EXPAND, 5 )
		
		self.corr_match_specified_path = wx.TextCtrl( sbSizer21.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.corr_match_specified_path, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 7 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText20 = wx.StaticText( sbSizer21.GetStaticBox(), wx.ID_ANY, u"No match penalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		gbSizer1.Add( self.m_staticText20, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.corr_match_nomatch = wx.TextCtrl( sbSizer21.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.corr_match_nomatch, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText21 = wx.StaticText( sbSizer21.GetStaticBox(), wx.ID_ANY, u"Speed penalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		gbSizer1.Add( self.m_staticText21, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.corr_match_speed_p = wx.TextCtrl( sbSizer21.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.corr_match_speed_p, wx.GBPosition( 2, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText24 = wx.StaticText( sbSizer21.GetStaticBox(), wx.ID_ANY, u"Tie penalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		gbSizer1.Add( self.m_staticText24, wx.GBPosition( 2, 4 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.corr_match_tie_p = wx.TextCtrl( sbSizer21.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.corr_match_tie_p, wx.GBPosition( 2, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText22 = wx.StaticText( sbSizer21.GetStaticBox(), wx.ID_ANY, u"Target speed", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		gbSizer1.Add( self.m_staticText22, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.corr_match_target = wx.TextCtrl( sbSizer21.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.corr_match_target, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText23 = wx.StaticText( sbSizer21.GetStaticBox(), wx.ID_ANY, u"Speed change penalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		gbSizer1.Add( self.m_staticText23, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.corr_match_speedchange = wx.TextCtrl( sbSizer21.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.corr_match_speedchange, wx.GBPosition( 3, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText25 = wx.StaticText( sbSizer21.GetStaticBox(), wx.ID_ANY, u"Gap penalty", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		gbSizer1.Add( self.m_staticText25, wx.GBPosition( 3, 4 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.corr_match_gap = wx.TextCtrl( sbSizer21.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.corr_match_gap, wx.GBPosition( 3, 5 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText252 = wx.StaticText( sbSizer21.GetStaticBox(), wx.ID_ANY, u"Intervals", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText252.Wrap( -1 )
		gbSizer1.Add( self.m_staticText252, wx.GBPosition( 3, 6 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.LEFT, 5 )
		
		self.corr_match_intervals = wx.TextCtrl( sbSizer21.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.corr_match_intervals, wx.GBPosition( 3, 7 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_staticText251 = wx.StaticText( sbSizer21.GetStaticBox(), wx.ID_ANY, u"Permitted rates", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText251.Wrap( -1 )
		gbSizer1.Add( self.m_staticText251, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.corr_match_rates = wx.TextCtrl( sbSizer21.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer1.Add( self.corr_match_rates, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 7 ), wx.ALL|wx.EXPAND, 5 )
		
		
		gbSizer1.AddGrowableCol( 1 )
		gbSizer1.AddGrowableCol( 3 )
		
		sbSizer21.Add( gbSizer1, 1, wx.EXPAND, 5 )
		
		
		self.panel_match.SetSizer( sbSizer21 )
		self.panel_match.Layout()
		sbSizer21.Fit( self.panel_match )
		bSizer14.Add( self.panel_match, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer14.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.button_correlate = wx.Button( self.panel_correlate, wx.ID_ANY, u"Start correlation", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.button_correlate, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		self.panel_correlate.SetSizer( bSizer14 )
		self.panel_correlate.Layout()
		bSizer14.Fit( self.panel_correlate )
		self.Notebook.AddPage( self.panel_correlate, u"Correlation", True )
		self.panel_progress = wx.Panel( self.Notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel18 = wx.Panel( self.panel_progress, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		self.text_progress = wx.StaticText( self.m_panel18, wx.ID_ANY, u"No correlation in progress.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.text_progress.Wrap( -1 )
		bSizer17.Add( self.text_progress, 0, wx.ALL, 5 )
		
		
		self.m_panel18.SetSizer( bSizer17 )
		self.m_panel18.Layout()
		bSizer17.Fit( self.m_panel18 )
		bSizer16.Add( self.m_panel18, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.simann_progress_gauge = wx.Gauge( self.panel_progress, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.simann_progress_gauge.SetValue( 0 ) 
		bSizer16.Add( self.simann_progress_gauge, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.panel_progressplot = wx.Panel( self.panel_progress, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.panel_progressplot.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNSHADOW ) )
		
		bSizer19 = wx.BoxSizer( wx.VERTICAL )
		
		
		self.panel_progressplot.SetSizer( bSizer19 )
		self.panel_progressplot.Layout()
		bSizer19.Fit( self.panel_progressplot )
		bSizer16.Add( self.panel_progressplot, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel21 = wx.Panel( self.panel_progress, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer18.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.button_abort = wx.Button( self.m_panel21, wx.ID_ANY, u"Abort", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.button_abort, 0, wx.ALL, 5 )
		
		
		self.m_panel21.SetSizer( bSizer18 )
		self.m_panel21.Layout()
		bSizer18.Fit( self.m_panel21 )
		bSizer16.Add( self.m_panel21, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.panel_progress.SetSizer( bSizer16 )
		self.panel_progress.Layout()
		bSizer16.Fit( self.panel_progress )
		self.Notebook.AddPage( self.panel_progress, u"Progress", False )
		self.ResultsPanel = wx.Panel( self.Notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13 = wx.BoxSizer( wx.VERTICAL )
		
		self.panel_resultsplot = wx.Panel( self.ResultsPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		
		self.panel_resultsplot.SetSizer( bSizer15 )
		self.panel_resultsplot.Layout()
		bSizer15.Fit( self.panel_resultsplot )
		bSizer13.Add( self.panel_resultsplot, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_button9 = wx.Button( self.ResultsPanel, wx.ID_ANY, u"Save results", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_button9, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		self.ResultsPanel.SetSizer( bSizer13 )
		self.ResultsPanel.Layout()
		bSizer13.Fit( self.ResultsPanel )
		self.Notebook.AddPage( self.ResultsPanel, u"Results (SA)", False )
		self.ResultsPanelMatch = wx.Panel( self.Notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer131 = wx.BoxSizer( wx.VERTICAL )
		
		self.panel_resultsplot_match = wx.Panel( self.ResultsPanelMatch, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer151 = wx.BoxSizer( wx.VERTICAL )
		
		
		self.panel_resultsplot_match.SetSizer( bSizer151 )
		self.panel_resultsplot_match.Layout()
		bSizer151.Fit( self.panel_resultsplot_match )
		bSizer131.Add( self.panel_resultsplot_match, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_button91 = wx.Button( self.ResultsPanelMatch, wx.ID_ANY, u"Save results", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer131.Add( self.m_button91, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		self.ResultsPanelMatch.SetSizer( bSizer131 )
		self.ResultsPanelMatch.Layout()
		bSizer131.Fit( self.ResultsPanelMatch )
		self.Notebook.AddPage( self.ResultsPanelMatch, u"Results (Match)", False )
		
		bSizer1.Add( self.Notebook, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.menubar = wx.MenuBar( 0 )
		self.menu_file = wx.Menu()
		self.submenu_config = wx.Menu()
		self.menuitem_save_config = wx.MenuItem( self.submenu_config, wx.ID_ANY, u"&Save configuration to file…", u"Save the current configuration settings to a file.", wx.ITEM_NORMAL )
		self.submenu_config.AppendItem( self.menuitem_save_config )
		
		self.menuitem_read_config = wx.MenuItem( self.submenu_config, wx.ID_ANY, u"&Read configuration from file…", u"Read a configuration from a previously saved Scoter file.", wx.ITEM_NORMAL )
		self.submenu_config.AppendItem( self.menuitem_read_config )
		
		self.menuitem_revert_config = wx.MenuItem( self.submenu_config, wx.ID_ANY, u"Re&vert configuration…", u"Revert any changes made during this session, returning to the configuration Scoter had when it was started.", wx.ITEM_NORMAL )
		self.submenu_config.AppendItem( self.menuitem_revert_config )
		
		self.menuitem_reset_config = wx.MenuItem( self.submenu_config, wx.ID_ANY, u"R&eset configuration…", u"Reset all confuration settings to their default values.", wx.ITEM_NORMAL )
		self.submenu_config.AppendItem( self.menuitem_reset_config )
		
		self.menu_file.AppendSubMenu( self.submenu_config, u"&Configuration" )
		
		self.submenu_export = wx.Menu()
		self.menuitem_export_scoter = wx.MenuItem( self.submenu_export, wx.ID_ANY, u"&Plain Scoter configuration…", u"Create a configuration file for the non-interactive version of Scoter.", wx.ITEM_NORMAL )
		self.submenu_export.AppendItem( self.menuitem_export_scoter )
		
		self.menuitem_export_bundle = wx.MenuItem( self.submenu_export, wx.ID_ANY, u"Self-contained &bundle…", u"Create a bundle containing the configuration and all the data.", wx.ITEM_NORMAL )
		self.submenu_export.AppendItem( self.menuitem_export_bundle )
		
		self.menu_file.AppendSubMenu( self.submenu_export, u"&Export" )
		
		self.menuitem_quit = wx.MenuItem( self.menu_file, wx.ID_EXIT, wx.EmptyString, wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.AppendItem( self.menuitem_quit )
		
		self.menubar.Append( self.menu_file, u"&File" ) 
		
		self.menu_help = wx.Menu()
		self.menuitem_userguide = wx.MenuItem( self.menu_help, wx.ID_ANY, u"&User guide…", u"Open the Scoter user guide in a web browser.", wx.ITEM_NORMAL )
		self.menu_help.AppendItem( self.menuitem_userguide )
		
		self.menuitem_show_licence = wx.MenuItem( self.menu_help, wx.ID_ANY, u"Show licence…", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_help.AppendItem( self.menuitem_show_licence )
		
		self.menuitem_about = wx.MenuItem( self.menu_help, wx.ID_ABOUT, wx.EmptyString, wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_help.AppendItem( self.menuitem_about )
		
		self.menubar.Append( self.menu_help, u"&Help" ) 
		
		self.SetMenuBar( self.menubar )
		
	
	def __del__( self ):
		pass
	

###########################################################################
## Class LicenceDialog
###########################################################################

class LicenceDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Scoter Licence", pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer23 = wx.BoxSizer( wx.VERTICAL )
		
		self.text_licence = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TE_MULTILINE )
		self.text_licence.SetMinSize( wx.Size( 200,200 ) )
		
		bSizer23.Add( self.text_licence, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.button_close = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer23.Add( self.button_close, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		self.SetSizer( bSizer23 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class SaveBundleDialog
###########################################################################

class SaveBundleDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Create bundle", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer24 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel28 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer4 = wx.FlexGridSizer( 3, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText35 = wx.StaticText( self.m_panel28, wx.ID_ANY, u"Bundle type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		fgSizer4.Add( self.m_staticText35, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		choice_bundle_typeChoices = [ u"Zip file", u"Folder" ]
		self.choice_bundle_type = wx.Choice( self.m_panel28, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choice_bundle_typeChoices, 0 )
		self.choice_bundle_type.SetSelection( 0 )
		fgSizer4.Add( self.choice_bundle_type, 0, wx.ALL, 5 )
		
		self.m_staticText36 = wx.StaticText( self.m_panel28, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )
		fgSizer4.Add( self.m_staticText36, 0, wx.ALL, 5 )
		
		self.check_include_results = wx.CheckBox( self.m_panel28, wx.ID_ANY, u"Include results", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.check_include_results, 0, wx.ALL, 5 )
		
		self.m_staticText37 = wx.StaticText( self.m_panel28, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )
		fgSizer4.Add( self.m_staticText37, 0, wx.ALL, 5 )
		
		self.check_include_scoter = wx.CheckBox( self.m_panel28, wx.ID_ANY, u"Include Scoter program", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.check_include_scoter.SetValue(True) 
		fgSizer4.Add( self.check_include_scoter, 0, wx.ALL, 5 )
		
		
		self.m_panel28.SetSizer( fgSizer4 )
		self.m_panel28.Layout()
		fgSizer4.Fit( self.m_panel28 )
		bSizer24.Add( self.m_panel28, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel29 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer25.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.button_cancel = wx.Button( self.m_panel29, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.button_cancel, 0, wx.ALL, 5 )
		
		self.button_create = wx.Button( self.m_panel29, wx.ID_ANY, u"Create", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.button_create, 0, wx.ALL, 5 )
		
		
		self.m_panel29.SetSizer( bSizer25 )
		self.m_panel29.Layout()
		bSizer25.Fit( self.m_panel29 )
		bSizer24.Add( self.m_panel29, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer24 )
		self.Layout()
		bSizer24.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

