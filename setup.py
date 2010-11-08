#! /usr/bin/env python
# -*- coding: utf8 -*-

# Copyright © 2010 Abhishek Tiwari (abhishek@abhishek-tiwari.com)
#
# This file is part of BioJSONUtils.
#
# Files included in this package BioJSONUtils are copyrighted freeware
# distributed under the terms and conditions as specified in file LICENSE.


try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
 
config = {
	'name' : 'BioJSONUtils',
	'description': 'JSON Endpoint for the various Bio web services',
	'author': 'Abhishek Tiwari',
	'url': 'http://github.com/abhishektiwari/BioJSONUtils',
	'download_url': 'http://github.com/abhishektiwari/BioJSONUtils',
	'author_email': 'abhishek@abhishek-tiwari.com',
	'version': '0.1',
	'install_requires': ['twisted','biopython'],
	'packages': ['biojsonutils'],
	'scripts': [],
}

setup(**config)


