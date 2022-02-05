#!/bin/bash

COLLECTION=${2:-zylk}
SERVER=${3:-localhost}
PORT=${4:-8983}
if [ -z "$1" ]; then
  # Usage
  echo 'Usage: delete-by-id.sh <id> [<collection> <solr-server=localhost> <port=8983>]'
else
  curl -X POST "http://${SERVER}:${PORT}/solr/${COLLECTION}/update?commit=true" -H "Content-Type: text/xml" --data-binary "<delete><id>$1</id></delete>"
fi