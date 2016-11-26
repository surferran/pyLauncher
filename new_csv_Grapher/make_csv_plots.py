'''

make_csv_plots.py

* desire:
run this file by command prompt :
    bokeh serve make_csv_plots.py

* script will include:
-user selects CSV file to read
-conversion from csv to pandas dataframe
-
-
-
-
-


* general details:
the packages to use are:
bokeh
pandas

all operations should be in small functions. in order to bind those actions to the widgets of the html to be.
should be a '_main_' option in order to run and test this script in standalone form

* future considerations:
check use of package 'pandas-highcharts'

* references:
bokeh documents
bokeh course in udemy

'''
import show_versions
from needed_imports import *
''''''''''''''''''''''''''''''

def get_headers_to_channels_list(df):
    return df._info_axis.values

def populate_channels_list(filter_text=''):
    print "populated call"
    pass

def open_local_file_dialog():
    app = wx.PySimpleApp()
    wildcard = "CSV files (*.csv)|*.csv|" \
               "Python source (*.py)|*.py|" \
               "Compiled Python (*.pyc)|*.pyc|" \
               "All files (*.*)|*.*"
    dialog = wx.FileDialog(None, "Choose a file", os.getcwd(), "", wildcard, wx.OPEN)
    if dialog.ShowModal() == wx.ID_OK:
        csv_file_path = dialog.GetPath()
        print " chosen file is : " + csv_file_path
        # read and populate the dataFrame
        global df, original_source
        df = pd.read_csv(csv_file_path, sep=';')
        original_source = ColumnDataSource(df)
        print df
        print original_source
        populate_channels_list()

    dialog.Destroy()

''''''''''''''''''''''''''''''

''' will be activated by server '''

df = []
original_source =[]


button = Button(label="load file", button_type="success")
button.on_click(open_local_file_dialog)




#create layout and add to curdoc
lay_out=layout([[button]])
curdoc().add_root(lay_out)