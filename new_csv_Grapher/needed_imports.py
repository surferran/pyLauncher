#importing libraries
from bokeh.io import curdoc
from bokeh.layouts import layout
from bokeh.plotting import figure
from bokeh.models.annotations import LabelSet
from bokeh.models import ColumnDataSource

from bokeh.models.widgets import Button     # button of load_file


import wx               # for open_local_file_dialog()
import os               # for open_local_file_dialog()

import pandas as pd     # for reading and handling the files and data