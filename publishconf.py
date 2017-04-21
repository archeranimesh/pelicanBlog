#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://archerimagine.com'
RELATIVE_URLS = False

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing
COMMENTS_INTRO = u'So what do you think? Did I miss something? Is any part unclear? Leave your comments below.'
DISQUS_SITENAME = "archerimagine"

GOOGLE_ANALYTICS = "UA-97386090-1"
MAILCHIMP_FORM_ACTION="//archerimagine.us15.list-manage.com/subscribe/post?u=e95cf93fc00f17a742b9480eb&amp;id=b690f10a78"
