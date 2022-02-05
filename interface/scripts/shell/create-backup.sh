#!/bin/bash

COLLECTION=${1:-zylk}
MYDATE=`/bin/date +%Y%m%d`
MYBACK="${COLLECTION}-${MYDATE}-backup"
BACKUPNAME=${2:-${MYBACK}}
BACKUPDIR=${3:-/opt/solr6/backups}
SERVER=${4:-localhost}
PORT=${5:-8983}

if [ -z "$1" ]; then
  # Usage
  echo 'Usage: create-backup.sh <collection-name> <backupname> <local-path> [<solr-server=localhost> <port=8983>]'
else
  echo "Creating SOLR backup collection for ${COLLECTION}"
  curl -s "http://${SERVER}:${PORT}/solr/admin/collections?action=BACKUP&name=${BACKUPNAME}&collection=${COLLECTION}&location=${BACKUPDIR}" 
fi