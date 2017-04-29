#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys
sys.path.append(os.curdir)
from elegantConfig import *
AUTHOR = u'Animesh Bhadra'
SITENAME = u'Archer Imagine'
SITESUBTITLE = u"Anyone can do my job, but no one can be me. Harvey"


PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

SOCIAL_PROFILE_LABEL = u'Stay in Touch'
# Social widget
SOCIAL = (('github', 'https://github.com/archeranimesh'),
          ('linkedin-square', 'https://www.linkedin.com/in/animeshkbhadra/'),
          ('facebook','https://www.facebook.com/animeshkbhadra'),
          ('quora', 'https://www.quora.com/profile/Animesh-Bhadra'),
          ('reddit', 'https://www.reddit.com/user/archerimagine/'),
          ('twitter', 'https://twitter.com/animeshkbhadra')
          )

TWITTER_USERNAME = 'animeshkbhadra'
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# My Modifications.
# To Ignore the cache when modifying the meta data in files.
LOAD_CONTENT_CACHE = False

#Static Path for Images.
STATIC_PATHS = ['extra', 'images']

EXTRA_PATH_METADATA = {
  'extra/favicon.ico': {'path': 'favicon.ico'},
  'extra/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
  'extra/apple-touch-icon-57x57.png': {'path': 'apple-touch-icon-57x57.png'},
  'extra/apple-touch-icon-72x72.png': {'path': 'apple-touch-icon-72x72.png'},
  'extra/apple-touch-icon-76x76.png': {'path': 'apple-touch-icon-76x76.png'},
  'extra/apple-touch-icon-114x114.png': {'path': 'apple-touch-icon-114x114.png'},
  'extra/apple-touch-icon-120x120.png': {'path': 'apple-touch-icon-120x120.png'},
  'extra/apple-touch-icon-144x144.png': {'path': 'apple-touch-icon-144x144.png'},
  'extra/apple-touch-icon-152x152.png': {'path': 'apple-touch-icon-152x152.png'},
  'extra/apple-touch-icon-180x180.png': {'path': 'apple-touch-icon-180x180.png'}
}

#In place of having content all over the content folder,
# moving it to a centralized place.
ARTICLE_PATHS = ['articles',]
ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'

OUTPUT_RETENTION = [".hg", ".git", "CNAME"]

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc' :{'permalink' : 'true'},

    },
    'output_format': 'html5',
}

THEME = 'themes/elegant'

PLUGIN_PATHS = ['plugin']
PLUGINS = ['sitemap', 'tipue_search', 'extract_toc']

SITEMAP = {
    'exclude': ['tag/', 'category/'],
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))