#! /usr/bin/env python
# -*- coding: utf8 -*-

# Copyright © 2010 Abhishek Tiwari (abhishek@abhishek-tiwari.com)
#
# This file is part of BioJSONUtils.
#
# Files included in this package BioJSONUtils are copyrighted freeware
# distributed under the terms and conditions as specified in file LICENSE.
from twisted.internet import reactor
from twisted.web import resource, server
from ncbi import ncbi

class StartServer:
	"""
	class_documentation
	"""
	
	def __init__(self, port = 8000):
		self.port = port
	
	def start_server(self):
		root = resource.Resource()
		# Service index
		root.putChild('', HomePage())
		# Service sub-types
		root.putChild('ncbi', NCBIRoot())
		#root.putChild('ebi', EBIRoot())
		#root.putChild('kegg', KEGGRoot())
		# Description of Reactor
		reactor.listenTCP(self.port, server.Site(root))
		# Starting Reactor
		print "Web service started, to stop it use <ctrl-c>"
		reactor.run()
		print "Web service stopped."


class HomePage(resource.Resource):
	def render(self, request):
		return """
			<html>
			<head>
			<title>MolSeek Public API</title>
			</head>
		    <body>
		    <h1>MolSeek Public API</h1>
		    <h3>For a simple Demo</h2>
		    Try,
		    <ul>
		      <li><a href='/ncbi/cortisol'>Search for "cortisol"</a></li>
		      <li><a href='/ncbi/star'>Search for "StAR"</a></li>
			</ul>
			<h3>For more details</h3>
			Check, <a href='/ncbi'>NCBI page</a>
			</body>
			</html>
		"""

class NCBIRoot(resource.Resource):
	def __init__(self):
		resource.Resource.__init__(self)
		self.putChild('', NCBIIndexPage())
		self.putChild('egquery', NCBIEGQueryRoot())
		self.putChild('esearch', NCBIESearchRoot())
		
	
	def render(self, request):
		# redirect /ncbi -> /ncbi/
		request.redirect(request.path + '/')
		return "Please use /ncbi/ instead."
	
	def getChild(self, path, request):
		return NCBIEGQueryPage(path)

class NCBIIndexPage(resource.Resource):
	def __init__(self):
		resource.Resource.__init__(self)
    
	def render(self, request):
		request.write("""
			<html>
			<head>
			<title>MolSeek Public API- NCBI</title>
			</head>
			<body>
			<h3>NCBI</h3>
			</body>
			</html>
	    """)
		return ""

class NCBIESearchRoot(resource.Resource):
	def __init__(self):
		resource.Resource.__init__(self)
		self.putChild('', NCBIESearchIndexPage())

	
	def render(self, request):
		# redirect /esearch -> /esearch/
		request.redirect(request.path + '/')
		return "Please use /esearch/ instead."
	
	def getChild(self, path, request):
		return NCBIESearcPage(path)

class NCBIESearcPage(resource.Resource):
	def __init__(self, keyword, database = "pubmed"):
		self.keyword = keyword
		self.database = database

	def render(self, request):
		return ncbi.ESearch(self.keyword, self.database) 
		
class NCBIESearchIndexPage(resource.Resource):
	def __init__(self):
		resource.Resource.__init__(self)
    
	def render(self, request):
		request.write("""
			<html>
			<head>
			<title>MolSeek Public API- NCBI</title>
			</head>
			<body>
			<h3>ESearch</h3>
			</body>
			</html>
	    """)
		return ""

class NCBIEGQueryRoot(resource.Resource):
	def __init__(self):
		resource.Resource.__init__(self)
		self.putChild('', NCBIEGQueryIndexPage())
		self.putChild('pubmed', NCBIEGQueryIndexPage())
	
	def render(self, request):
		# redirect /egquery -> /egquery/
		request.redirect(request.path + '/')
		return "Please use /egquery/ instead."
	
	def getChild(self, path, request):
		return NCBIEGQueryPage(path)

	
class NCBIEGQueryPage(resource.Resource):
	def __init__(self, keyword):
		self.keyword = keyword

	def render(self, request):
		return ncbi.EGQuery(self.keyword) 
		
class NCBIEGQueryIndexPage(resource.Resource):
	def __init__(self):
		resource.Resource.__init__(self)
    
	def render(self, request):
		request.write("""
			<html>
			<head>
			<title>MolSeek Public API- NCBI</title>
			</head>
			<body>
			<h3>EGQuery</h3>
			</body>
			</html>
	    """)
		return ""
