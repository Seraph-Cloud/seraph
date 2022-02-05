#!/bin/bash

COLLECTION=${2:-gettingstarted}
SERVER=${3:-localhost}
PORT=${4:-8983}
if [ -z "$1" ]; then
  # Usage
  echo 'Usage: delete-by-id3.sh <id> [<collection> <solr-server=localhost> <port=8383>]'
else
  curl -X POST "http://${SERVER}:${PORT}/solr/${COLLECTION}/update?commit=true" -H "Content-Type: application/json" --data-binary "{\"delete\": {\"id\":\"$1\"}}"
fi