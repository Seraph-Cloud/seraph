# Serpah Main Python File #################################
# Author: @diveyez github.com/diveyez diveyez.com #########
# Import Resources ########################################
# Import App sys/env vars #################################
# Import Module and Run From Prompt #######################
###########################################################
#from seraph_vars import TOKEN1
from modules import * # will eventually import all 
# necessary python scripts as modules from ./modules
from seraph_vars import * # imports the vars module
import plotly.graph_objects as go  # or plotly.express as px
import nasdaqdatalink # nasda data packages for python
import mplfinance as mf # finance libraries needed for charting and processing data
import pandas as pd # required
from twelvedata import TDClient #twelvedata.com's official packages
import plotly.express as px # plot charts for usage with twelvedata
import plotly # plotly main package
import plotly.io as pio # import export
import twelvedata # importing rest of twelvedata 
# ^ not necessary after development and testing
from json import loads # required
import json # required for api's
import requests # required for interaction and taking data
import os # required for management of application and files
import time # required for other modules
import sys # required for dir creation and file management
# ADD UI CODE HERE ########################

###########################################
print("-----SERAPH------")
print("-------is--------")
print("-----loading-----")
print("--------∆--------")

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
# adding the modules path
sys.path.insert(0, 'modules')
################################################################
# END OF SETUP
# DEFINE VARS BY USER INPUT
############################################

## TICKER SELECTION
ticker_symbol = input("What Ticker:")
# WRITE TO FILE
f = open('seraph_pid.txt', "w")
f.write(
        ticker_symbol
)
f.close()
# Twelvedata Token
SELECTED_12dTOKEN = input("What TewlveData Token:")
f = open('selected_token.txt', "w")
f.write(
    SELECTED_12dTOKEN
)
f.close()
td = TDClient(apikey=SELECTED_12dTOKEN)
print("Imported Vars and Modules....")
