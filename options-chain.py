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
# Get PID


def get_tid(data):
    data = open(data, "r")


get_pid = open('seraph_pid.txt')
print(get_pid)
pid = print(get_pid)

## one of the above should work...
#import asyncio
# JAVA SCRIPT OBJECT ORIENTATION
if not os.path.exists("data/json"):
    os.mkdir("data/json")
# TOKENS
td = TDClient(apikey=TOKEN1)

path_calls = var.options_calls(
    'options-calls-' > '%s.json % pid')  # " % s.json" % pid
path_puts = var.options_calls(
    'options-puts-' > '%s.json % pid')  # "%s.json" % pid

## Get all expiration dates
expirations = td.get_options_expiration(
            symbol=var.pid().as_json()['dates'])
time.sleep(60)
#
## Extract only put options for the soonest expiration date...
put_options = td.get_options_chain(
        symbol="pid",
        side="put",
        expiration_date=expirations[0]
        ).as_json()['puts']
sys.stdout = open(var.options_puts, "w")
print(put_options)
time.sleep(60)
#
# Extract only put options for the soonest expiration....
put_options = td.get_options_chain(
                                       symbol="pid",
                                       side="call",
                                       expiration_date=expirations[0]
                                       ).as_json()['calls']
sys.stdout = open(var.options_calls, "w")
print(put_options)
