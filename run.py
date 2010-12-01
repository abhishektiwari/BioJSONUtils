#! /usr/bin/env python
# -*- coding: utf8 -*-

# Copyright © 2010 Abhishek Tiwari (abhishek@abhishek-tiwari.com)
#
# This file is part of BioJSONUtils.
#
# Files included in this package BioJSONUtils are copyrighted freeware
# distributed under the terms and conditions as specified in file LICENSE.

"""
This scripts starts BioJSONUtils server. You need to provide the port 
information to start the server successfully.

Example uses:
1. For help information,
python run.py --help 
OR
python run.py --h 
2. For starting server at port 8000,
python run.py 8000

"""

from biojsonutils import webserver
import sys
import getopt

class Usage(Exception):
	"""
	Usage() exception class, which we catch in an except clause at the 
	end of main()
	"""
	def __init__(self, msg):
		self.msg = msg
		
def main(argv = None):
	"""
	Description of main() function, if required collect the command line
	arguments, and activate further anlysis. 
	"""
	# An optional 'argv' argument, which allows us to call it from the 
	# interactive Python prompt
	if argv is None:
		argv = sys.argv
	try:
		if len(argv) < 2:
			raise Usage(__doc__)
		try:
			opts, args = getopt.getopt(argv[1:], "h", ["help"])
		except getopt.error, msg:
			raise Usage(msg)
		# Option processing
		for option, value in opts:
			if option in ("-h","--help"):
				raise Usage(__doc__)
				sys.exit(0)
			#do something with options here
		# Argument processing
		for argument in args:
			try:
				argument.strip()
				cargument = int(argument)
			except:
				print "Can not cast argument to int"
			try:
				if cargument >= 8000 & cargument < 9000:
					print argument
					twi_instance = webserver.StartServer(cargument)
					twi_instance.start_server()
			except Usage, err:
				print "Unexpected error:", sys.exc_info()[0]
				print >>sys.stderr, err.msg
	except Usage, err:
		print >>sys.stderr, err.msg
		print >>sys.stderr, "for help use --help"
		return 2
	

if __name__ == "__main__":
	"""
	The main program collected into function main()
	"""
	sys.exit(main())
