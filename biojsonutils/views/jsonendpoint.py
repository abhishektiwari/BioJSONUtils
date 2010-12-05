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
from flask import render_template
from biojsonutils.webservices.ncbi.eutils import EUtils

ENTREZ_EMAIL = "sandbox@gmail.com"

jsonendpoint = Module(__name__)

@jsonendpoint.route('/ncbi/<keyword>', methods=['GET'])
def ncbi_egquery(keyword):
	"""
	Search with NCBI EGQuery and return the JSON results
	"""
	if request.args.has_key('callback'):
		kwargs = {"term": keyword}
		print "term:",keyword
		return EUtils.egquery(request.args['callback'], request.args['email'], **kwargs)
	else:
		kwargs = {"term": keyword}
		return EUtils.egquery(None, ENTREZ_EMAIL, **kwargs)

@jsonendpoint.route('/ncbi/esearch/<keyword>', methods=['GET'])
def ncbi_esearch(keyword):
	"""
	Search with NCBI EGQuery and return the JSON results
	"""
	if request.args.has_key('callback'):
		kwargs = {"term": keyword, "db": request.args['db']}
		return EUtils.esearch(request.args['callback'], request.args['email'], **kwargs)
	else:
		kwargs = {"term": keyword, "db": request.args['db']}
		return EUtils.esearch(None, ENTREZ_EMAIL, **kwargs)


