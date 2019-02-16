#!/bin/bash

# json2txt.sh - given a HathiTrust JSON file, output "human-readable" plain text

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# February 10, 2019 - fist cut


# configure
HTJSON2NAME='./bin/htjson2name.py'
HTJSON2TXT='./bin/htjson2txt.py'

# get input
JSON=$1
DIRECTORY=$2

# sanity check
if [[ -z $JSON || -z $DIRECTORY ]]; then

    echo "Usage: $0 <JSON> <directory>" >&2
    exit
    
fi

# do the work and done
$HTJSON2TXT $JSON > $DIRECTORY/$($HTJSON2NAME $JSON)
exit

