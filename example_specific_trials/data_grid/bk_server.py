#Categorical axes
from IPython import __version__ as ipython_version
from pandas import __version__ as pandas_version
from bokeh import __version__ as bokeh_version
print("IPython - %s" % ipython_version)
print("Pandas - %s" % pandas_version)
print("Bokeh - %s" % bokeh_version)

#importing libraries
from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.models.annotations import LabelSet
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import RadioButtonGroup
from bokeh.layouts import layout
import tkFileDialog

#crate columndatasource
source=ColumnDataSource(dict(average_grades=["B+","A","D-"],
                             exam_grades=["A+","C","D"],
                             student_names=["Stephan","Helder","Riazudidn"]))

#create the figure
f = figure(x_range=["F","D-","D","D+","C-","C","C+","B-","B","B+","A-","A","A+"],
           y_range=["F","D-","D","D+","C-","C","C+","B-","B","B+","A-","A","A+"])

#add labels for glyphs
labels=LabelSet(x="average_grades",y="exam_grades",text="student_names",x_offset=5, y_offset=5, source=source)
f.add_layout(labels)

#create glyphs
f.circle(x="average_grades", y="exam_grades", source=source, size=8)

#create function
def update_labels(attr,old,new):
    labels.text=options[radio_button_group.active]

''' ran change from original '''
def open_local_file(attr,old,new):
    labels.text = ["chosen file is : " + tkFileDialog.askopenfilename()]
    print labels.text

def open_local_file_long(attr,old,new):
    import wx
    import os

    app = wx.PySimpleApp()
    wildcard = "Python source (*.py)|*.py|" \
               "Compiled Python (*.pyc)|*.pyc|" \
               "All files (*.*)|*.*"
    dialog = wx.FileDialog(None, "Choose a file", os.getcwd(), "", wildcard, wx.OPEN)
    if dialog.ShowModal() == wx.ID_OK:
        print dialog.GetPath()

    dialog.Destroy()


#create select widget
options=["average_grades","exam_grades","student_names"]
radio_button_group=RadioButtonGroup(labels=options)
# radio_button_group.on_change("active",update_labels)
radio_button_group.on_change("active",open_local_file)

#create layout and add to curdoc
lay_out=layout([[radio_button_group]])
curdoc().add_root(f)
curdoc().add_root(lay_out)
