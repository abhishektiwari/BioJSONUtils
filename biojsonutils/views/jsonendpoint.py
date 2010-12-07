#! /usr/bin/env python
# -*- coding: utf8 -*-

# Copyright © 2010 Abhishek Tiwari (abhishek@abhishek-tiwari.com)
#
# This file is part of BioJSONUtils.
#
# Files included in this package BioJSONUtils are copyrighted freeware
# distributed under the terms and conditions as specified in file LICENSE.

from flask import request
from flask import Module
from biojsonutils.webservices.ncbi.eutils import EUtils


jsonendpoint = Module(__name__)

@jsonendpoint.route('/ncbi/egquery', methods=['GET'])
def ncbi_egquery():
	"""
	Search with NCBI EGQuery and return the JSON results
	"""
	if request.args.has_key('callback'):
		kwargs = {"term": request.args['term']}
		print "term:", request.args['term']
		return EUtils.egquery(request.args['callback'], request.args['email'], **kwargs)

@jsonendpoint.route('/ncbi/esearch', methods=['GET'])
def ncbi_esearch():
	"""
	Search with NCBI EGQuery and return the JSON results
	"""
	if request.args.has_key('callback'):
		kwargs = {"term": request.args['term'], "db": request.args['db']}
		print "term:", request.args['term'], "db:", request.args['db']
		return EUtils.esearch(request.args['callback'], request.args['email'], **kwargs)


