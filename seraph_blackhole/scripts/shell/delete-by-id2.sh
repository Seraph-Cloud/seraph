#!/bin/bash

SOLR_DIR=/opt/solr6/solr-6.6.0/
COLLECTION=${2:-gettingstarted}
PORT=${3:-8983}
if [ -z "$1" ]; then
  # Usage
  echo 'Usage: delete-by-id2.sh <id> [<collection>]'
else
  cd SOLR_DIR
  ./bin/post -p $PORT -c $COLLECTION -d "<delete><id>$1</id></delete>"
fi