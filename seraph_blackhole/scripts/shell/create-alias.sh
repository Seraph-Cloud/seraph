#!/bin/bash

ALIAS=${1:-zylk-alias}
COLLECTION=${3:-zylk}
SERVER=${3:-localhost}
PORT=${4:-8983}

if [ -z "$1" ]; then
  # Usage
  echo 'Usage: create-alias.sh <alias-name> <collection-name-list> [<solr-server=localhost> <port=8983>]'
  #curl -s "http://${SERVER}:${PORT}/solr/admin/collections?action=LISTALIASES" | xmllint --format -
else
  echo "Creating SOLR alias collection $ALIAS for ${COLLECTION}"
  curl -s "http://${SERVER}:${PORT}/solr/admin/collections?action=CREATEALIAS&name=${ALIAS}&collections=${COLLECTION}" | tidy -q -xml -i - 
fi
  
curl -s "http://${SERVER}:${PORT}/solr/admin/collections?action=LISTALIASES" | tidy -q -xml -i -