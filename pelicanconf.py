#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

OUTPUT_PATH = 'output'

THEME = 'theme'  # pelican-bootstrap3 mod
BOOTSTRAP_THEME = 'flatly'
BOOTSTRAP_NAVBAR_INVERSE = True
BANNER = 'images/banner.jpg'
BANNER_SUBTITLE = 'Modelleersoftware enzo'

HIDE_SIDEBAR = False
DISPLAY_CATEGORIES_ON_MENU = False

PYGMENTS_STYLE = 'monokai'

STATIC_PATHS = ['../CNAME', 'images']
EXTRA_PATH_METADATA = {'../CNAME': {'path': 'CNAME'}}

PLUGIN_PATHS = ['plugins/', ]
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

AUTHOR = 'Tom Kooij'
SITENAME = 'Tom Kooij'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'nl'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Modelleertaal', 'https://www.tomkooij.nl/modelleertaal/'),
         ('Modelleertaal-dev', 'https://www.tomkooij.nl/modelleertaal-dev/'),)

# Social widget
SOCIAL = (('GitHub @tomkooij', 'https://github.com/tomkooij'),
          ('Twitter @tomkooij', 'https://twitter.com/tomkooij'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
