# User Token and NYSE Symbol Selection Test Scipt
# Author: @diveyez
# adding more test code to this file
# this is only for testing
# TD Client is only here for testing of input
from twelvedata import TDClient
import twelvedata
from json import loads
import json
import requests
import os
import time
import sys
import importlib
# Setting up the absolue path & app data paths
#drive, tcase_dir = os.path.splitdrive(os.path.abspath(__file__))
#paths = tcase_dir.split(os.sep)[:-0]
#base_dir = os.path.join(drive,os.sep,*paths)
# Importing the rest of Seraph files
import modules
from seraph_vars import *
#data_dir = r'data'
#data_csv_dir = r'data/csv'
#data_db_dir = r'data/db'
##data_json_dir = r'data/json'
#data_ticker_data_dir = r'data/ticker-data'
#data_lists = r'data/lists'
#data_images_dir = r'data/images'
#data_images_finviz_dir = r'data/images/finviz'
#data_images_time_series_plots_dir = r'data/images/time_series_plots'
#data_images_time_series_plots_1min_dir = r'data/images/time_series_plots/1min'
#data_images_time_series_plots_5min_dir = r'data/images/time_series_plots/5min'
#data_images_time_series_plots__15min_dir = r'data/images/time_series_plots/15min'
#data_images_time_series_plots_30min_dir = r'data/images/time_series_plots/30min'
# Defines seraph_abs_path
#seraph_abs_path = os.path.join(base_dir)
                             #  (base_dir, data_dir, data_csv_dir, data_db_dir, 
                              # data_json_dir, data_ticker_data_dir, data_lists,
                              #  data_images_dir, data_images_time_series_plots_dir)
# Example Defining
# <something>_abs_path = os.path.join(base_dir, dir2, dir3)

# Twelvedata Token
SELECTED_12dTOKEN = input("What Token:")
# Write to file
f = open('selected_token.txt', "w")
#f = open(os.path.join(seraph_abs_path, r'selected_token.txt'), "w")
f.write(
    SELECTED_12dTOKEN
)
f.close()
td = TDClient(apikey=SELECTED_12dTOKEN)
print("Imported Vars and Modules....")
# TICKER SELECTION
ticker_symbol = input("What Ticker:")
# Write to file
# f = open(os.path.join(seraph_abs_path, r'seraph_pid.txt'), "w")
f = open('seraph_pid.txt', "w")
f.write(
        ticker_symbol
)
f.close()
from modules import options_chain
# hacking exec for now
# NOT SAFE
#exec(open(options_chain.py).read())
importlib.import_module('options_chain')
# for testing 
# # importlib.reload()