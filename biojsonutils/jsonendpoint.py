#! /usr/bin/env python
# -*- coding: utf8 -*-

# Copyright © 2010 Abhishek Tiwari (abhishek@abhishek-tiwari.com)
#
# This file is part of BioJSONUtils.
#
# Files included in this package BioJSONUtils are copyrighted freeware
# distributed under the terms and conditions as specified in file LICENSE.
from flask import Flask
from ncbi import ncbi

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


@app.route('/ncbi/<keyword>.js')
def show_user_profile(keyword):
	"""
	Search with NCBI EGQuery and return the JSON results
	"""
	return ncbi.EGQuery(keyword) 

if __name__ == '__main__':
	app.run()
