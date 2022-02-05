# Seraph

**The Historical Information Dataminer Companion**

_configure example.seraph_vars.py as needed_
```mv examples.seraph_vars.py seraph_vars.py```
# Requirements
-   docker docker-compose
-   python3+ flask
-   wsgi serer
# Local App Setup

# Development
```bash 
pip install -r requirements.txt
export FLASK_APP=app
export FLASK_ENV=development
python3 init-db.py
flask run -p <port number>
```
# Login Source
[https://github.com/maxcountryman/flask-login](https://github.com/maxcountryman/flask-login)
#  API Auth Tokens Required
-   TwelveData
*More Planned*
# Current Integrations

-   twelvedata charts/data
-   yahoo data
-   finviz charts/data

# TODO
-  TDA Developer Tools
-  NASDAQ Datalink
-  SecAPI
-  Plotter 3d Market Datalink
-  Webull Developer Tools
-  OPSTRAT Python Scripting
-  TOS Options TA & Webpage Generation
-  Images Webpage Generation
-  Finish UI
-  Full Encryption
-  Full Containerization


# how the json from twelvedata looks
```json
[
  {
  'contract_name': '',
  'option_id': '',
  'last_trade_date': '',
  'strike': '',
  'last_price': '',
  'bid': '',
  'ask': '',
  'change': '',
  'percent_change': '',
  'volume': '',
  'open_interest': '',
  'implied_volatility': ''
  'in_the_money': ''
}
],
[
  {
    'contract_name': '',
    'open_interest': '',
    'volme': '',
    'bid',
    'implied_volatility': '',
    'percent_change': '',
    'in_the_money': ''
  }
]
```

## YAHOO STUFF

```python
# turning the yahoo link into something that processes environment vars
yahoo_url = [('https://query1.finance.yahoo.com/v7/finance/download/'), ticker_symbol,
             ('?period1=1612356150&period2=1643892150&interval=1d&events=history&includeAdjustedClose=true')]
print(url)
```

## YAHOO API endpoints

The Yahoo Finance API provides 11 endpoints, each of which covers a specific feature that you can use:
```
/v6/finance/quote - real time quote data for stocks, ETFs, mutuals funds, bonds, crypto and national currencies.
/v7/finance/options - option chains data for a particular stock market company
/v8/finance/spark - historical data for various intervals and ranges
/v11/finance/quoteSummary - very detailed information for a particular ticker symbol
/v8/finance/chart - chart data
/v6/finance/recommendationsbysymbol - list of similar stocks
/ws/screeners/v1/finance/screener/predefined/saved - list of most added stocks to the watchlist
/ws/insights/v1/finance/insights - research insights
/v6/finance/autocomplete - auto complete stock suggestions
/v6/finance/quote/marketSummary - live market summary information at the request time
/v1/finance/trending - trending stocks in a specific region
```


### Finviz Finance Documents
[https://finvizfinance.readthedocs.io/en/latest/](https://finvizfinance.readthedocs.io/en/latest/)

# SEC API
All data comes from [SEC.gov](https://SEC.gov) through [https://sec-api.io](https://sec-api.io)

*Examples and Reference Code*
[github.com/janlukasschroeder/sec-api-python](https://github.com/janlukasschroeder/sec-api-python)


# API URLs

[Query API:](https://api.sec-api.io)
[Stream API:](https://api.sec-api.io:3334/all-filings)
[Full-Text Search API:](https://api.sec-api.io/full-text-search)
[XBRL-to-JSON Converter API:](https://api.sec-api.io/xbrl-to-json)
[10-K/Q Item Extractor API:](https://api.sec-api.io/extractor)
[Filing Render & Download API:](https://api.sec-api.io/filing-reader)
[CIK, Ticker, CUSIP Mapping API:](https://api.sec-api.io/mapping)
[Executive Compensation API:](https://api.sec-api.io/compensation)