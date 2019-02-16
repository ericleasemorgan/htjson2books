#!/usr/bin/env python

# json2name.py - given a HathiTrust JSON file, output a something can be use as a file name based on bibliographics

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# February 10, 2019 - based on other HathiTrust work; bogus metadata; ugly


# require
import json
import sys
import re

# sanity check
if ( len( sys.argv ) != 2 ) :
	sys.stderr.write( "Usage: " + sys.argv[ 0 ] + ' <json>\n' )
	quit()

# open the input; parse, format, and output
with open( sys.argv[ 1 ] ) as HANDLE : json  = json.load( HANDLE )

# read/normalize the title
title = ( json[ 'metadata' ][ 'title' ] )
title = title.lower()
title = re.sub(r'[^\w\s]','',title)
words = title.split()

# read date
date  = ( json[ 'metadata' ][ 'pubDate' ] ) 

# output, conditionally
if ( words[ 0 ] == 'a'   or 
     words[ 0 ] == 'the' or 
     words[ 0 ] == 'an'  or 
     words[ 0 ] == 'la' ) : print( words[ 1 ] + '-' + date + '.txt' )

else : print( words[ 0 ] + '-' + date + '.txt' )

# done
quit()
