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
from wtforms import Form, TextField, validators

examples = Module(__name__)

class AjaxForm(Form):
	keyword = TextField('Keyword:', [validators.Length(min=4, max=30)])

@examples.route('/')
def index():
	return render_template('examples.html', subtitle = 'Examples')


@examples.route('/getjson/', methods=['GET', 'POST'])
def getjson():
	form = AjaxForm(request.form)
	if request.method == 'POST' and form.validate():
		keyterm = form.keyword.data
		return render_template('getjson.html', subtitle = 'Examples-Using jQuery.getJSON', form = form, keyword = keyterm)
	else:
		form = AjaxForm(keyword = 'star')
		keyterm = form.keyword.data
		return render_template('getjson.html', subtitle = 'Examples-Using jQuery.getJSON', form = form, keyword = keyterm)

@examples.route('/searchfetch/', methods=['GET', 'POST'])
def searchfetch():
	form = AjaxForm(request.form)
	if request.method == 'POST' and form.validate():
		keyterm = form.keyword.data
		return render_template('searchfetch.html', subtitle = 'Examples-Using jQuery.getJSON', form = form, keyword = keyterm)
	else:
		form = AjaxForm(keyword = 'star')
		keyterm = form.keyword.data
		return render_template('searchfetch.html', subtitle = 'Examples-Using jQuery.getJSON', form = form, keyword = keyterm)

@examples.route('/selectedsearch/', methods=['GET', 'POST'])
def selectedsearch():
		return render_template('selectedsearch.html', subtitle = 'Examples-Using jQuery/UI')

@examples.route('/similarsearch/', methods=['GET', 'POST'])
def similarsearch():
	form = AjaxForm(request.form)
	if request.method == 'POST' and form.validate():
		keyterm = form.keyword.data
		return render_template('similarsearch.html', subtitle = 'Examples-Using jQuery.getJSON', form = form, keyword = keyterm)
	else:
		form = AjaxForm(keyword = 'star')
		keyterm = form.keyword.data
		return render_template('similarsearch.html', subtitle = 'Examples-Using jQuery.getJSON', form = form, keyword = keyterm)
