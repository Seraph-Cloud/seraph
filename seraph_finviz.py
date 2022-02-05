# Finviz Python stock_description
# Author: @diveyez
# Just for personal usage
from finvizfinance.insider import Insider
import sys
import os
from finvizfinance.quote import finvizfinance
from finvizfinance.news import News
from finvizfinance.screener.overview import Overview
from seraph_vars import *
import pandas as pd
## TICKER SELECTION
ticker_symbol = input("What Ticker:")
# WRITE TO FILE
f = open('seraph_pid.txt', "w")
f.write(
        ticker_symbol
)
f.close()
# Charts
stock = finvizfinance(ticker_symbol)
stock.ticker_charts(timeframe='daily', charttype='advanced',
                    out_dir='data/images/daily/finviz')
# Rename
symbol = ticker_symbol
imagename = "%s.png" % symbol
