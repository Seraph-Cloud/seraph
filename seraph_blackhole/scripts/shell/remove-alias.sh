#!/bin/bash

ALIAS=${1:-zylk-alias}
SERVER=${2:-localhost}
PORT=${3:-8983}

if [ -z "$1" ]; then
  # Usage
  echo 'Usage: remove-alias.sh <alias-name> [<solr-server=localhost> <port=8983>]'
  #curl -s "http://${SERVER}:${PORT}/solr/admin/collections?action=LISTALIASES" | xmllint --format -
else
  echo "Removing SOLR alias collection ${ALIAS}"
  curl -s "http://${SERVER}:${PORT}/solr/admin/collections?action=DELETEALIAS&name=${ALIAS}" | tidy -q -xml -i -

fi
  
curl -s "http://${SERVER}:${PORT}/solr/admin/collections?action=LISTALIASES" | tidy -q -xml -i -