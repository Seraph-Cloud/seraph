# Options Chain Data
# Author: @diveyez
# sys.path.append('../') # DONT WORK FOR VARS MODULE
import requests
import os
import time
from seraph_vars import *
import json
from json import loads
import twelvedata
from twelvedata import TDClient
import sys
drive, tcase_dir = os.path.splitdrive(os.path.abspath(__file__))
paths = tcase_dir.split(os.sep)[:-2]
base_dir = os.path.join(drive,os.sep,*paths)
# Get PID
from seraph_vars import *
data_dir = r'data'
data_csv_dir = r'data/csv'
data_db_dir = r'data/db'
data_json_dir = r'data/json'
data_ticker_data_dir = r'data/ticker-data'
data_lists = r'data/lists'
data_images_dir = r'data/images'
data_images_finviz_dir = r'data/images/finviz'
data_images_time_series_plots_dir = r'data/images/time_series_plots'
data_images_time_series_plots_1min_dir = r'data/images/time_series_plots/1min'
data_images_time_series_plots_5min_dir = r'data/images/time_series_plots/5min'
data_images_time_series_plots__15min_dir = r'data/images/time_series_plots/15min'
data_images_time_series_plots_30min_dir = r'data/images/time_series_plots/30min'
# Defines seraph_abs_path
seraph_abs_path = os.path.join(base_dir, data_dir, data_csv_dir, data_db_dir, 
                               data_json_dir, data_ticker_data_dir, data_lists,
                                data_images_dir, data_images_time_series_plots_dir)
# Example Defining
# <something>_abs_path = os.path.join(base_dir, dir2, dir3)

def get_tid(data):
    data = open(data, "r")
get_pid = open('seraph_pid.txt')
# not needed now?
# # print(get_pid)
pid = print(get_pid)

# JAVA SCRIPT OBJECT ORIENTATION
if not os.path.exists("data/json"):
    os.mkdir("data/json")
# TOKENS
f = open(os.path.join(seraph_abs_path, r'selected_token.txt'), "r")
td = TDClient(apikey=SELECTED_12dTOKEN)

path_calls = var.options_calls(
    'options-calls-' > '%s.json % pid')  # " % s.json" % pid
path_puts = var.options_calls(
    'options-puts-' > '%s.json % pid')  # "%s.json" % pid

## Get all expiration dates
expirations = td.get_options_expiration(
            symbol=var.pid().as_json()['dates'])
time.sleep(5)
#
## Extract only put options for the soonest expiration date...
put_options = td.get_options_chain(
        symbol="pid",
        side="put",
        expiration_date=expirations[0]
        ).as_json()['puts']
sys.stdout = open(var.options_puts, "w")
print(put_options)
time.sleep(5)
#
# Extract only put options for the soonest expiration....
put_options = td.get_options_chain(
                                       symbol="pid",
                                       side="call",
                                       expiration_date=expirations[0]
                                       ).as_json()['calls']
sys.stdout = open(var.options_calls, "w")
print(put_options)
