#! /usr/bin/env python
# -*- coding: utf8 -*-

# Copyright © 2010 Abhishek Tiwari (abhishek@abhishek-tiwari.com)
#
# This file is part of BioJSONUtils.
#
# Files included in this package BioJSONUtils are copyrighted freeware
# distributed under the terms and conditions as specified in file LICENSE.
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from jsonendpoint import app


class StartServer:
	"""
	class_documentation
	"""
	
	def __init__(self, port = 5000):
		self.port = port
	
	def start_server(self):
		http_server = HTTPServer(WSGIContainer(app))
		http_server.listen(self.port)
		print "Web service started, to stop it use <ctrl-c>"
		IOLoop.instance().start()
		print "Web service stopped."

if __name__ == '__main__':
	tar_instance = StartServer(5000)
	tar_instance.start_server()
