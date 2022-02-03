# TESTING SCRIPT WHERE ALL THINGS ARE TESTED
#
#from discord.ext.commands import Bot
#from discord.ext import commands
#from discord import Embed
#import discord
import requests
#import asyncio
import os
import time
import sys
# JAVA SCRIPT OBJECT ORIENTATION
import json
from json import loads
import twelvedata
import plotly.io as pio
import plotly
import plotly.express as px
from twelvedata import TDClient
import pandas as pd
import mplfinance as mf
import nasdaqdatalink
# adding graph graph_objects
import plotly.graph_objects as go  # or plotly.express as px
fig = go.Figure()  # or any Plotly Express function e.g. px.bar(...)
# fig.add_trace( ... )
# fig.update_layout( ... )

# SYSTEM STUFF
# import dotenv
# MAKE IMAGES DIR
if not os.path.exists("data/images"):
    os.mkdir("data/images")
if not os.path.exists("data/csv"):
    os.mkdir("data/csv")
if not os.path.exists("data/json"):
    os.mkdir("data/json")

# TOKENS
# twelvedata token R Neff
#td = TDClient(apikey="991b6d046946451281a740fa21f4da61")
# twelvedata token T Shull
td = TDClient(apikey="3f2818aaa9ee4a7195e1237830de9876")
#
#api = td.api_usage()
file_path = 'data/json/NFLX-options-calls.json'
file_path2 = 'data/json/NFLX-options-puts.json'

## Get all expiration dates
expirations = td.get_options_expiration(
    symbol="NFLX").as_json()['dates']
time.sleep(60)
#
## Extract only put options for the soonest expiration date
put_options = td.get_options_chain(
    symbol="NFLX",
    side="put",
    expiration_date=expirations[0]
).as_json()['puts']
sys.stdout = open(file_path2, "w")
print(put_options)
time.sleep(60)
#
# Extract only put options for the soonest expiratio../other-apps/bots/seraph/data/imagesn date
put_options = td.get_options_chain(
    symbol="NFLX",
    side="call",
    expiration_date=expirations[0]
    ).as_json()['calls']
sys.stdout = open(file_path, "w")
print(put_options)
time.sleep(60)
#
# CHARTS AS TIME SERIES
#
# Construct the necessary time series
ts = td.time_series(
   symbol="NFLX",
   interval="1min",
   outputsize=250,).with_macd_slope().with_vwap().with_ema(time_period=24).with_floor().as_plotly_figure().write_image("data/images/time_series_plots/NFLX1.min.png")
time.sleep(30)
ts = td.time_series(
   symbol="NFLX",
   interval="1min",
   outputsize=250,).with_stochrsi().with_bbands().with_percent_b().as_plotly_figure().write_image("data/images/time_series_plots/NFLX1.1.min.png")
time.sleep(30)

# Construct the necessary time series
ts = td.time_series(
   symbol="NFLX",
   interval="5min",
   outputsize=125,).with_macd_slope().with_vwap().with_ema(time_period=72).with_floor().as_plotly_figure().write_image("data/images/time_series_plots/NFLX5.min.png")
time.sleep(30)
ts = td.time_series(
   symbol="NFLX",
   interval="5min",
   outputsize=125,).with_stochrsi().with_bbands().with_percent_b().as_plotly_figure().write_image("data/images/time_series_plots/NFLX5.1.min.png")
time.sleep(60)
# Construct the necessary time series
ts = td.time_series(
   symbol="NFLX",
   interval="15min",
   outputsize=750,).with_macd_slope().with_vwap().with_ema(time_period=128).with_floor().as_plotly_figure().write_image("data/images/time_series_plots/NFLX15.min.png")
time.sleep(30)
ts = td.time_series(
   symbol="NFLX",
   interval="15min",
   outputsize=750,).with_stochrsi().with_bbands().with_percent_b().as_plotly_figure().write_image("data/images/time_series_plots/NFLX15.1min.png")
time.sleep(60)
# Construct the necessary time series
ts = td.time_series(
   symbol="NFLX",
   interval="30min",
   outputsize=750,).with_macd_slope().with_vwap().with_ema(time_period=24).with_floor().as_plotly_figure().write_image("data/images/time_series_plots/NFLX15.min.png")
time.sleep(30)
ts = td.time_series(
   symbol="NFLX",
   interval="30min",
   outputsize=1000,).with_stochrsi().with_bbands().with_percent_b().as_plotly_figure().write_image("data/images/time_series_plots/NFLX15.1min.png")
time.sleep(60)

#ts.as_url()
# returns Plotly dash
#ts.as_plotly_figure()
#time.sleep(30)
# BOT CODE
#
# CANCELED
# Setup for Discord bot
# Loading cog by default without need of any commands.

#
# FOR testing
# bot.run("")
#bot.run(bot_token)

print("finished")
