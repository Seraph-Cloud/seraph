from sec_api import QueryApi
import os
queryApi = QueryApi(api_key="YOUR_API_KEY")
#queryApi = QueryApi(api_key="<api_key_here>")
query = {
  "query": { "query_string": {
      "query": "ticker:TSLA AND filedAt:{2020-01-01 TO 2020-12-31} AND formType:\"10-Q\""
    } },
  "from": "0",
  "size": "10",
  "sort": [{ "filedAt": { "order": "desc" } }]
}

filings = queryApi.get_filings(query)
f = open
print(filings)
