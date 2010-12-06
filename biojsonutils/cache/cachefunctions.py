#! /usr/bin/env python
# -*- coding: utf8 -*-

# Copyright © 2010 Abhishek Tiwari (abhishek@abhishek-tiwari.com)
#
# This file is part of BioJSONUtils.
#
# Files included in this package BioJSONUtils are copyrighted freeware
# distributed under the terms and conditions as specified in file LICENSE.




# Using Simple cache keeps the item stored in the memory of the Python interpreter
from werkzeug.contrib.cache import SimpleCache
cache = SimpleCache()

# Using App Engine, you can connect to the App Engine memcache server easily
# from werkzeug.contrib.cache import GAEMemcachedCache
# cache = GAEMemcachedCache()

# Using memcached server, you will need supported memcache modules installed
#from werkzeug.contrib.cache import MemcachedCache
#cache = MemcachedCache(['127.0.0.1:11211'])


def get_from_cache(cache_key):
	cached_value = cache.get(cache_key)
	return cached_value

def set_the_cache(cache_key, cache_value):
	cache.set(cache_key, cache_value, timeout=5 * 60)
