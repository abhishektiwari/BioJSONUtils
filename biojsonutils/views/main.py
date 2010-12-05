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



main = Module(__name__)

@main.route('/')
def index():
	return render_template('index.html', subtitle = 'Welcome')
