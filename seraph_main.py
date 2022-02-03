# Serpah Main Python File #################################
# Author: @diveyez                                        #
# Import App sys/env vars                                 #
# Import Module and Run From Prompt                       #
############################################################
#from seraph_vars import TOKEN1
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
# ADD UI CODE HERE ########################

###########################################
print("-----SERAPH------")
print("-------is--------")
print("-----loading-----")
print("-----------------")

##############################################################
# MAKE IMAGE DIR's
##############################################################
print("Making image directories if they do not exist...")
if not os.path.exists("data/images"):
    os.mkdir("data/images")
if not os.path.exists("data/images/time_series_plots"):
    os.mkdir("data/images/time_series_plots")
if not os.path.exists("data/images/time_series_plots/1min"):
    os.mkdir("data/images/time_series_plots/1min")
if not os.path.exists("data/images/time_series_plots/5min"):
    os.mkdir("data/images/time_series_plots/5min")
if not os.path.exists("data/images/time_series_plots/15min"):
    os.mkdir("data/images/time_series_plots/15min")
################################################################
# END OF SETUP
# DEFINE VARS BY USER INPUT
############################################
# Twelvedata Token
SELECTED_TOKEN = input("What Token:")
f = open('selected_token.txt', "w")
f.write(
    SELECTED_TOKEN
)
f.close()
td = TDClient(apikey=SELECTED_TOKEN)
print("Imported Vars and Modules....")
## TICKER SELECTION
ticker_symbol = input("What Ticker:")
# WRITE TO FILE
f = open('seraph_pid.txt', "w")
f.write(
        ticker_symbol
)
f.close()
