#!/bin/bash

COLLECTION=${1:-zylk-backup}
BACKUPNAME=${2:-zylk-backup-name}
BACKUPDIR=${3:-/opt/solr6/backups}
SERVER=${4:-localhost}
PORT=${5:-8983}

if [ -z "$2" ]; then
  # Usage
  echo 'Usage: restore-backup.sh <collection-name> <backupname> <local-path> [<solr-server=localhost> <port=8983>]'
else
  echo "Restoring SOLR backup collection for ${COLLECTION}"
  curl -s "http://${SERVER}:${PORT}/solr/admin/collections?action=RESTORE&name=${BACKUPNAME}&collection=${COLLECTION}&location=${BACKUPDIR}" 
fi