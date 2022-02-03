# Charts Grabber Code
# Author: @diveyez
# without the time.sleep(30) or time.sleep(60)
# this module consumes lots of API uses at TwelveData
import numpy as np
import seaborn as sns
from seraph_vars import *
import plotly.graph_objects as go  # or plotly.express as px
import nasdaqdatalink
import mplfinance as mf
import pandas as pd
from twelvedata import TDClient
import plotly.express as px
import plotly
import plotly.io as pio
import twelvedata
from json import loads
import json
import requests
import os
import time
import sys
###########################################
# Twelvedata Token
#selected_token = input("What Token:")

#f = open('selected_token.txt', "w")
#f.write(
#        selected_token
#)
#f.close()
#
td = TDClient(apikey=TOKEN1)
## TICKER SELECTION
ticker_symbol = input("What Ticker:")
# WRITE TO FILE
f = open('seraph_pid.txt', "w")
f.write(
        ticker_symbol
)
f.close()

# There is 8 charts, 4 sets being made
# 1,5,15,30 minutes
# two of each with different strategies and indicators
# The files are renamed after the write
# This set of charts is meant to be simple, and used for small detail images
# in things like blog posts or articles and not intended for usage trading
# Charts are as a Time Series in Plotly Figures
# Source: twelvedata-client
data = np.array([-100, 1, 2, 5, 15, 17, 20, 60, 80, 100])
fig = px.box(data, points="all")
fig.show()


print("Finished Plotting")
print("Image Files can be located at data/images/time_series_plots/1min*/5min*/15min*/30min")
