#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Gordon Chiam'
SITENAME = u"gchiam's Playground"
SITEURL = ''

TIMEZONE = 'Asia/Singapore'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (
    ('Source Project', 'https://github.com/gchiam/gchiam-playground'),
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
    ('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (
    ('GitHub+', 'https://github.com/gchiam'),
    ('Google+', 'https://plus.google.com/+GordonChiam'),
    ('Facebook', 'https://www.facebook.com/gordon.chiam'),
    ('Twitter', 'https://www.twitter.com/gordonchiam'),
    ('Flickr', 'http://www.flickr.com/photos/gchiam/'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'pelican-themes/pelican-bootstrap3'
