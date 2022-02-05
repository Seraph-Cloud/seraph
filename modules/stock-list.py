# List of Stocks to a File Function
# Author: @diveyez

from seraph_vars import *
from twelvedata import TDClient
import twelvedata
from json import loads
import json
import os
import time
import sys
# sys.path.append('../') # DONT WORK FOR VARS MODULE
# MAKE IMAGES DIR

if not os.path.exists("data/json"):
    os.mkdir("data/json")

# TOKENS

td = TDClient(apikey=TOKEN2)
#
# Define File for Stocks List
file_stocks_list = 'data/json/12_stocks_list.json'
## Get Stocks List
json_list_data = td.get_stocks_list().as_json()
sys.stdout = open(file_stocks_list, "w")
print(json_list_data)
time.sleep(60)
