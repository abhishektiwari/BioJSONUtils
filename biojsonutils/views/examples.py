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
	keyword = TextField('Keyword:', [validators.Length(min=4, max=25)])

@examples.route('/')
def index():
	return render_template('examples.html', subtitle = 'Examples')


@examples.route('/getjson/', methods=['GET', 'POST'])
def getjson():
	form = AjaxForm(request.form)
	if request.method == 'POST' and form.validate():
		keyterm = form.keyword.data
		return render_template('getjson.html', subtitle = 'Examples-Using jQuery.getJSON', form = form, keyword = keyterm)
	elif request.method == 'POST' and not form.validate():
		form = AjaxForm(keyword = 'star')
		keyterm = form.keyword.data
		return render_template('getjson.html', subtitle = 'Examples-Using jQuery.getJSON', form = form, keyword = keyterm)
	else:
		form = AjaxForm(keyword = 'star')
		keyterm = form.keyword.data
		return render_template('getjson.html', subtitle = 'Examples-Using jQuery.getJSON', form = form, keyword = keyterm)
