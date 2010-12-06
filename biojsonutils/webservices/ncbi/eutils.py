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
from biojsonutils.cache.cachefunctions import get_from_cache, set_the_cache

ENTREZ_TOOL  = "MolSeekSandbox"

class EUtils:
	"""
	NCBI Entrez web-services handling
	"""
	
	@classmethod
	def cache_key_generator(eclass, efunction, **options):
		keydict = {'calltype':efunction}
		keydict.update(options)
		keys = sorted(keydict.keys())
		return "&".join(["%s=%s" % (k, keydict[k]) for k in keys])	
	
	@classmethod
	def call_and_cache_result(eclass, efunction, sfunction, callback_id, email_id, **options):
		cache_key = eclass.cache_key_generator(sfunction, **options)
		cached_value = get_from_cache(cache_key)
		if cached_value is None:
			handle = efunction(tool=ENTREZ_TOOL, email=email_id, **options)
			record = Entrez.read(handle)
			json_record = json.dumps(record)
			set_the_cache(cache_key, json.loads(json_record))
			return json_response(json_record, callback_id)
		else:
			return json_response(cached_value, callback_id)
			

	@classmethod
	def egquery(eclass, callback_id, email_id, **options):
		return eclass.call_and_cache_result(Entrez.egquery, 'Entrez.egquery', callback_id, email_id, **options)

	@classmethod
	def esearch(eclass, callback_id, email_id, **options):
		return eclass.call_and_cache_result(Entrez.esearch, 'Entrez.esearch', callback_id, email_id, **options)

def json_response(json_record, callback_id):
	"""
	Helper to handle JSON/JSONP calls
	"""
	if callback_id == None:
		return json_record
	else:
		response = "%s(%s)" % (callback_id, json_record)
		return response


	

	


