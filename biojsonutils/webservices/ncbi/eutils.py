#! /usr/bin/env python
# -*- coding: utf8 -*-

# Copyright © 2010 Abhishek Tiwari (abhishek@abhishek-tiwari.com)
#
# This file is part of BioJSONUtils.
#
# Files included in this package BioJSONUtils are copyrighted freeware
# distributed under the terms and conditions as specified in file LICENSE.

from Bio import Entrez
from flask import json

ENTREZ_TOOL  = "MolSeekSandbox"

class EUtils:
	"""
	NCBI Entrez web-services handling
	"""

	@classmethod
	def call_and_cache_result(eclass, efunction, callback_id, email_id, **options):
		handle = efunction(tool=ENTREZ_TOOL, email=email_id, **options)
            	record = Entrez.read(handle)
		return json_response(record, callback_id)

	@classmethod
	def egquery(eclass, callback_id, email_id, **options):
		return eclass.call_and_cache_result(Entrez.egquery, callback_id, email_id, **options)

	@classmethod
	def esearch(eclass, callback_id, email_id, **options):
		return eclass.call_and_cache_result(Entrez.esearch, callback_id, email_id, **options)

def json_response(record, callback_id):
	"""
	Helper to handle JSON/JSONP calls
	"""
	if callback_id == None:
		return json.dumps(record)
	else:
		data = json.dumps(record)
		response = "%s(%s)" % (callback_id, data)
		return response


	

	


