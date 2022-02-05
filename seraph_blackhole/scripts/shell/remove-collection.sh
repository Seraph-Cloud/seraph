#!/bin/bash

#./bin/solr delete -c zylk
SOLRHOME=/opt/solr6/solr-6.6.0
COLLECTION=${1:-zylk}

if [ -z "$1" ]; then
  # Usage
  echo 'Usage: remove-collection.sh <collection-name>'
else
  echo "Removing SOLR collection ${COLLECTION}"
  (cd ${SOLRHOME} && ./bin/solr delete -c ${COLLECTION})
fi