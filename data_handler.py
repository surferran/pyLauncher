#this file will treat data stuff

#read csv (or any other data file ) - store it as pandas dataframe.
#   it is a table with headers. the headers can be saved also as list of 'channels'
#   each line is a record of a time point.
#   displays:
#     1. as a table that can be scrolled. visible are headers and indices.

#         few culomns can be selected and put into a graph.

#         in the graph they will be displayed as -points -line with points -line
#         on the corner there will be a visible dictionary, with checkboxes to allow visibility on graph.+other icon to select channel for manipulation
#         right click on graph will allow:
#            export checked-boxed channels to be exported to a floating separated graph.
#                   each graph or figure will be stored in list of figures. with properties of:
#                     (sub)figure id
#                     location : -main gui display -hidden -floating
#     2. graphs - list of chanels aside. with the text filter. (keep the id relation properly)
#                pressing a channel item will display it in graph. several selection will be added accordingly.
#                 have button for 'keep channel(s) in graph'.
#                 y axis will be channel values.
#                 x axis will be indices. or default time channel - will be set by option in 'table' display mode.
#   drag & drop :
#     dragable :
#        figure : will contain data structure of :
#                        channels contained : dataframe id, model name, variable name, display properties (line/points,color,width)
#        table : drag column(s) to figure - to be added and displayed. will contain (dataframe id, model name, variable name)
#   channel manipulations:
#     by macro (from virtual channel):
#            have an initial drag box with watermark of 'drop here'
#             show at  side possible actions texts
#              will display 'X# = model+var name'
#            make copy of chanel(s) with nick name of X#.
#     by imidiate action : offset in x or y ,

from myImports import *

def read_csv_to_pandas_df(file_name):
    pd_df =  pd.read_csv(file_name, sep=';')
    return pd_df

def get_headers_or_channels(df):
    return df._info_axis.values
    pass

def display_df_as_table(df_to_show_in_grid):
    # certain ref: http://stackoverflow.com/questions/16958513/showing-pandas-data-frame-as-a-table
    if __name__ == '__main__':
        app = wx.App()
        frame = PandasTable(None, 'pandas grid unit-test', df_to_show_in_grid)
        #TODO: consider using the 'GridHugeTable.py' example. it feels much faster for display.
        #       consider influence of the 'autosize' functions on reaction speed for the user
        app.MainLoop()
    else:
        frame = PandasTable(None, 'pandas dataframe in wx grid display', df_to_show_in_grid)
    pass

if __name__ == '__main__':
    print " -- running main of 'data_handler' -- "

    print " testing loading csv to dataframe "
    filepath = u'C:/Users/Ran_the_User/Documents/GitHub/pyLauncher/USER_data/'
    filename = u'Sensor_record_20150810_002415_AndroSensor.csv'

    df_from_csv = read_csv_to_pandas_df(filepath + filename)
    # print df_from_csv
    # print df_from_csv['LOCATION Speed ( Kmh)']

    channels = get_headers_or_channels(df_from_csv)
    print channels

    '''
    print " testing showing csv as dataframe in wxPy grid "
    display_df_as_table(df_from_csv)
    # display_df_as_table(returned_values)    #trial
    '''

    returned_values = plot_to_bokeh(df_from_csv, channels, 1)  # returnes nd array

    pass

