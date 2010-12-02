#! /usr/bin/env python
# -*- coding: utf8 -*-

# Copyright © 2010 Abhishek Tiwari (abhishek@abhishek-tiwari.com)
#
# This file is part of BioJSONUtils.
#
# Files included in this package BioJSONUtils are copyrighted freeware
# distributed under the terms and conditions as specified in file LICENSE.
from flask import Flask, request
from ncbi.ncbi import EUtils

ENTREZ_EMAIL = "sandbox@gmail.com"

app = Flask(__name__)

@app.route('/')
def index():
	"""
	Render the landing page
	"""
	return """
			<html>
			<head>
			<title>MolSeek Public API</title>
			</head>
		    <body>
		    <h1>MolSeek Public API</h1>
		    <h3>For a simple Demo</h2>
		    Try,
		    <ul>
		      <li><a href='/ncbi/cortisol'>Search for "cortisol"</a></li>
		      <li><a href='/ncbi/star'>Search for "StAR"</a></li>
			</ul>
			<h3>For more details</h3>
			Check, <a href='/ncbi'>NCBI page</a>
			</body>
			</html>
		"""


@app.route('/ncbi/<keyword>.js', methods=['GET'])
def ncbi_egquery(keyword):
	"""
	Search with NCBI EGQuery and return the JSON results
	"""
	if request.args.has_key('callback'):
		kwargs = {"term": keyword}
		return EUtils.egquery(request.args['callback'], request.args['email'], **kwargs)
	else:
		kwargs = {"term": keyword}
		return EUtils.egquery(None, ENTREZ_EMAIL, **kwargs)

@app.route('/ncbi/esearch/<keyword>.js', methods=['GET'])
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

if __name__ == '__main__':
	app.run()
