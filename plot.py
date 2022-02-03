# TEST PLOT
from seraph_vars import *
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
# sys.path.append('../') # DONT WORK FOR VARS MODULE
import os
import time
import sys
print("Working... Please be patient...")
df = px.data.stocks(indexed=True)-1
fig = px.area(df, facet_col="company", facet_col_wrap=2)
fig.write_image(chart_test)
print("Finished, the image is in '../data/images/grid_plots'")
