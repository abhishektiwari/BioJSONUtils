#! /usr/bin/env python
# -*- coding: utf8 -*-

# Copyright © 2010 Abhishek Tiwari (abhishek@abhishek-tiwari.com)
#
# This file is part of BioJSONUtils.
#
# Files included in this package BioJSONUtils are copyrighted freeware
# distributed under the terms and conditions as specified in file LICENSE.

from flask import Flask
from biojsonutils.views.main import main
from biojsonutils.views.examples import examples
from biojsonutils.views.jsonendpoint import jsonendpoint

app = Flask(__name__)
app.register_module(main)
app.register_module(jsonendpoint)
app.register_module(examples, url_prefix='/examples')



