#! /usr/bin/env python
# -*- coding: utf8 -*-

# Copyright © 2010 Abhishek Tiwari (abhishek@abhishek-tiwari.com)
#
# This file is part of ToyProjects.
#
# Files included in this package ToyProjects are copyrighted freeware
# distributed under the terms and conditions as specified in file LICENSE.

from Bio import Entrez
import simplejson as json

Entrez.email = "Sandbox sandbox@gmail.com"

def EGQuery(keyword):
	"""
	this function takes the keyword and search in NCBI using eUtils
	"""
	
	handle = Entrez.egquery(term = keyword)
	record = Entrez.read(handle)
	return json.dumps(record)

def ESearch(keyword, database):
	"""
	this function takes the keyword and search in a specified NCBI 
	database using eUtils
	"""
	handle = Entrez.esearch(db = database, term = keyword)
	record = Entrez.read(handle)
	return json.dumps(record)
