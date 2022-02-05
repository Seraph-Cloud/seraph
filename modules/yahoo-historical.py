# Yahoo Historical Data Digestion
import requests
from seraph_vars import *

## TICKER SELECTION
ticker_symbols = input("What Ticker('s):")
# WRITE TO FILE
f = open('seraph_pid.txt', "w")
f.write(
        ticker_symbols
)
f.close()
url = "https://yfapi.net/v6/finance/quote"

querystring = {
    "symbols": ticker_symbols
    }

headers = {
    'x-api-key': YAHOO_TOKEN
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
