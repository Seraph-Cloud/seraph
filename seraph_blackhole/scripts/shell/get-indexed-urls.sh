#! /bin/bash

###
### Script for getting indexed urls from SOLR 
###

# Usage functions
usage() { echo "Usage: $0 [-c <collection-name>] [-h <solr-host>] [-p <solr-port>]" 1>&2; exit 1; }

# Command line options
while getopts "c:h:p:" o; do
    case "${o}" in
        c)
            COLLECTION=${OPTARG}
            ;;
        h)
            SERVER=${OPTARG}
            ;;
        p)
            PORT=${OPTARG}
            ;;
        \?)
            echo "Invalid Option: -$OPTARG" 1>&2
            exit 1
            ;;
        *)
            usage
            ;;
    esac
done
shift $((OPTIND-1))

# Needs at least COLLECTION as parameter 
if [ -z "${COLLECTION}" ]; then
    usage
fi

# Exports SERVER, PORT ? 
#source ./exportENVARS.sh

# Default parameters
#COLLECTION=${COLLECTION:-garbiker}
SERVER=${SERVER:-localhost}
PORT=${PORT:-8983}

# Main
NUMROWS=`curl -s "http://${SERVER}:${PORT}/solr/${COLLECTION}/select?indent=on&q=*:*&wt=json" | jq '.response.numFound'`
echo "Number of indexed urls in $1 : $NUMROWS"
ROWS=10000
COUNT=0
START=0
while [ $START -lt $NUMROWS ]; do
    curl -s "http://${SERVER}:${PORT}/solr/${COLLECTION}/select?fl=url&indent=on&q=*:*&rows=$ROWS&start=$START&sort=url%20desc&wt=json" | jq '.response.docs[].url'
    COUNT=$((COUNT+1))
    START=$((ROWS*COUNT))
done