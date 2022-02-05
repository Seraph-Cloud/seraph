# User Token and NYSE Symbol Selection Scipt
# Author: @diveyez
#
from seraph_vars import *
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

# Twelvedata Token
SELECTED_TOKEN = input("What Token:")
# Write to file
f = open('selected_token.txt', "w")
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
