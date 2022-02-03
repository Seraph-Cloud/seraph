# Serpah Main Python File #################################
# Author: @diveyez                                        #
# Import App sys/env vars                                 #
# Import Module and Run From Prompt                       #
############################################################
# import seraph_vars
import sys
from seraph_vars import *
import plotly.graph_objects as go  # or plotly.express as pxd
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
import modules
# ADD UI CODE HERE ########################
## 1) Progress Bar
## 2) Image as URL
## 3) Image as Interactive Chart / Figure
## 4) Image as Web Page Embed
## 5) Image as Ghost Webpost
###########################################
print("-----SERAPH------")
print("-------is--------")
print("-----loading-----")
print("-----------------")
time.sleep(5)
print("Imported Vars and Modules....")
time.sleep(2)
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
time.sleep(3)
################################################################
# END OF SETUP
# DEFINE VARS BY USER INPUT
ticker_symbol = input("What Ticker: (Please Write In Quotes 'XXX'):")
print("Ticker is:" + ticker_symbol)
sys.stdout_pid = open('seraph_pid.txt', "w")
print(ticker_symbol)
time.sleep(3)
# NOW WE MOVE TO STRUCTURE FORMATION OF APPLICATION
# twelvedata token
#token_selected = input("What Token: (TOKEN1,TOKEN2,TOKEN3,TOKEN4)")
#print("Token Selected: " + token_selected)
#sys.stdout = open('selected_token.txt', "w")
#print(token_selected)
#td = TDClient(apikey=token_selected)
#time.sleep(3)
############################################
# Twelvedata Token
token_selected = input("What Token (TOKEN1,TOKEN2,TOKEN3,TOKEN4)?: ")
print("Token Selected:" + token_selected)
# WRITE TO FILE
sys.stdout_token = open('selected_token.txt', "w")
print(token_selected)  # DO NOT UNCOMMENT
# READING THE SELECTED TOKEN
f = open('selected_token.txt', 'r')
toksel = f.read(seraph_vars)
print("Token Selected:",
      toksel
      )
td = TDClient(apikey=toksel)
print("Imported API key....")
time.sleep(10)
