#!/bin/bash

COLLECTION=${2:-zylk}
SERVER=${3:-localhost}
PORT=${4:-8983}
if [ -z "$1" ]; then
  # Usage
  echo 'Usage: add-by-id.sh <id> [<collection> <solr-server=localhost> <port=8383>]'
else
  curl -X POST "http://${SERVER}:${PORT}/solr/${COLLECTION}/update?commit=true" -H "Content-Type: text/xml" --data-binary "<add><doc><field name='id'>$1</field><field name='url'>$1</field></doc></add>"
fi