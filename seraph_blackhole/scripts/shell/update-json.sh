#!/bin/bash
json=$(cat <<EOF
[
{
  "id": "$1",
  "url": "$1"
}
]
EOF
)

COLLECTION=${2:-zylk}
SERVER=${3:-localhost}
PORT=${4:-8983}

if [ -z "$1" ]; then
  # Usage
  echo 'Usage: update-json.sh <id> [<collection> <solr-server=localhost> <port=8983>]'
else
  curl -X POST "http://${SERVER}:${PORT}/solr/${COLLECTION}/update?boost=0&commit=true" -H "Content-Type: application/json" --data-binary "$json" 
fi