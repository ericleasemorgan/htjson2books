#!/usr/bin/env python

# require
import sys
import json
import re

# sanity check
if ( len( sys.argv ) != 2 ) :
	sys.stderr.write( "Usage: " + sys.argv[ 0 ] + ' <json>\n' )
	quit()

# get input; sanity check
file = sys.argv[ 1 ]

# initialize
with open( sys.argv[ 1 ] ) as HANDLE : json  = json.load( HANDLE )
words     = {}
book      = ( json[ 'metadata' ][ 'title' ] ) + '\t' + ( json[ 'metadata' ][ 'handleUrl' ] ) + '\n\n'

# process each page
pages = json['features' ][ 'pages' ]
for page in pages :
	
	# process each token (word) on the page
	tokens = page[ 'body' ][ 'tokenPosCount' ]
	for token in tokens : book = book + token + ' ' 
				
	# delimit a page in the book
	book = book + '\n\n'
	
# output book, or
print ( re.sub( '\n\n+', '\n\n', book ) )

# done
quit()


