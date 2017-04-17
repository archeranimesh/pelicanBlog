#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Animesh Bhadra'
SITENAME = u'Archer Imagine'


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
STATIC_PATHS = ['images']

#In place of having content all over the content folder,
# moving it to a centralized place.
ARTICLE_PATHS = ['articles',]
ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'

OUTPUT_RETENTION = [".hg", ".git", "CNAME"]



