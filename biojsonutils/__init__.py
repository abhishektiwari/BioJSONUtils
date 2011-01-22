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

application = Flask(__name__)
application.register_module(main)
application.register_module(jsonendpoint)
application.register_module(examples, url_prefix='/examples')



