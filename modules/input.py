# User Token and NYSE Symbol Selection Test Scipt
# Author: @diveyez
# adding more test code to this file
# this is only for testing
import plotly.graph_objects as go
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
# Setting up the absolue path & app data paths
drive, tcase_dir = os.path.splitdrive(os.path.abspath(__file__))
paths = tcase_dir.split(os.sep)[:-2]
base_dir = os.path.join(drive,os.sep,*paths)
# Importing the rest of Seraph files
import modules
from seraph_vars import *
data_dir = r'data'
data_csv_dir = r'data/csv'
data_db_dir = r'data/db'
data_images_dir = r'data/images'
data_images_finviz_dir = r'data/images/finviz'
data_images_time_series_plots_dir = r'data/images/time_series_plots'
data_images_time_series_plots_1min_dir = r'data/images/time_series_plots/1min'
data_images_time_series_plots_5min_dir = r'data/images/time_series_plots/5min'
data_images_time_series_plots__15min_dir = r'data/images/time_series_plots/15min'
data_images_time_series_plots_30min_dir = r'data/images/time_series_plots/30min'
data_images_time_series_plots_dir = r'data/images/time_series_plots'
seraph_abs_path = os.path.join(base_dir, data_dir, data_csv_dir, data_db_dir, data_images_dir, data_images_time_series_plots_dir )
# Example Defining
# <something>_abs_path = os.path.join(base_dir, dir2, dir3)

# Twelvedata Token
SELECTED_12dTOKEN = input("What Token:")
# Write to file
f = with open(os.path.join())('selected_token.txt', "w")
f.write(
    SELECTED_12dTOKEN
)
f.close()
td = TDClient(apikey=SELECTED_12dTOKEN)
print("Imported Vars and Modules....")
# TICKER SELECTION
ticker_symbol = input("What Ticker:")
# Write to file
f = open('seraph_pid.txt', "w")
f.write(
        ticker_symbol
)
f.close()
