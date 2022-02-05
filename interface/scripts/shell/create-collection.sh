#!/bin/bash

#./bin/solr create -c zylk -shards 1 -replicationFactor 2 -p 8983 -d server/solr/configsets/nutchconfig-base
SOLRHOME=/opt/solr6/solr-6.6.0
CONFIGSET=server/solr/configsets/nutchconfig-base
COLLECTION=${1:-zylk}
PORT=${2:-8983}

if [ -z "$1" ]; then
  # Usage
  echo 'Usage: create-collection.sh <collection-name> [ <port=8080> ]'
else
  echo "Creating SOLR collection ${COLLECTION}"
  (cd ${SOLRHOME} && ./bin/solr create -c ${COLLECTION} -shards 1 -replicationFactor 2 -p ${PORT} -d ${CONFIGSET})
fi