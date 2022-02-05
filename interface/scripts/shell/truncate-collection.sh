#! /bin/bash

###
### Script for truncating SOLR collection via REST API  
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
#COLLECTION=${COLLECTION:-turismoberria}
SERVER=${SERVER:-localhost}
PORT=${PORT:-8983}

# Truncate 
curl -X POST http://${SERVER}:${PORT}/solr/${COLLECTION}/update?commit=true -H "Content-Type: text/xml" --data-binary '<delete><query>*:*</query></delete>'
# Reload
curl "http://${SERVER}:${PORT}/solr/admin/collections?action=RELOAD&name=${COLLECTION}"