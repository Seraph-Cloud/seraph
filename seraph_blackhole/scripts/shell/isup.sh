#!/bin/#!/usr/bin/env bash
echo "Checking to see if Solr is running or not..."
sleep 5.0
RESULT=$(curl -s -o /dev/null -I -w '%{http_code}' http://example.com:8983/solr/admin/cores?action=STATUS)
if [ "$RESULT" -eq '200' ]; then
    # Solr is running...
else
    # Solr is not running...
fi
sleep 5.0
echo " bash /path/to/solr/bin/solr start | if the server is not running, use that line, set the path first"
