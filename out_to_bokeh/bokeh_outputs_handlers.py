from bokeh.plotting import figure
from bokeh.io import output_notebook, output_file, show
from bokeh.sampledata.iris import flowers

def plot_to_bokeh(data_frame, channels_names, desired_col_index=-1):
    '''

    :param data_frame:  pandas dataframe
    :param desired_col_index: -1 for all, i>0 for any other
    :return: non
    '''
    if desired_col_index>=0:
        header_str = data_frame._info_axis.values[desired_col_index]
        col_data = data_frame._series[channels_names[desired_col_index]].values     # returns nd_array
        # data_frame[data_frame._info_axis.values[3]]
        print col_data
        ###################
        output_file("iris.html")

        # Create the figure object
        f = figure()

        # adding glyphs
        f.circle(range(0,len(col_data)), col_data)

        # Save and show the figure
        show(f)

        print f

        ###################
        return col_data


