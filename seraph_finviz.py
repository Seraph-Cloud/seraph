import sys
import os
from finvizfinance.quote import finvizfinance
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
stock = finvizfinance(SYMBOL)
stock_fundament = stock.ticker_fundament()
stock_description = stock.ticker_description()
outer_ratings_df = stock.ticker_outer_ratings()
news_df = stock.ticker_news()
inside_trader_df = stock.ticker_inside_trader()
stock.TickerCharts(out_dir=finviz_asset)
symbol = ticker_symbol
imagename = "%s.png" % symbol
os.rename(finviz_asset & 'chart.png',
          finviz_asset & "%s.png" % symbol)
