Title: Understanding the Pelican Settings files.
Date: 2017-04-30 17:07:03
Modified: 2017-04-30 18:11:34
Category: Pelican
Tags: pelican
Slug: pelican-settings-files
Author: Animesh Bhadra
subtitle: Enhancing Pelican
Summary: By default pelican comes with 2 settings files, pelicanconf.py and publishconf.py. In this post we try to understand the meaning of these to files and some basic settings.
keywords: pelicanconf.py, publishconf.py

The basic work flow in pelican blogging is to first generate content, verify it locally using a [localhost:8000](http://localhost:8000/), and when everything is fine will publish it.

Pelican comes with two settings files to separate these 2 process. These two files are.

* `pelicanconf.py`
* `publishconf.py`

Lets check what is the use of these 2 files, and how to manipulate these files to get the most out of pelican.

These setting files are mostly passed to the templates associated with the themes to generate the site, all these settings are some parameters to these templates.

## pelicanconf.py ##

We had used the `pelican-quickstart` to generate this blog, when we use this command, we get a pre-configured `pelicanconf.py` and a `publishconf.py` files. This have the bare basic configuration to be used based on the questions we answered on the options.

These files basically contains the settings identifier for the pelican blog, all the setting identifiers are in all-caps, and the values numbers (5, 20, etc.), booleans (True, False, None, etc.), dictionaries, or tuples should not be enclosed in quotation marks.

`pelicanconf.py` is used to generate the site locally and tested over [localhost:8000](http://localhost:8000/). The basic `pelicanconf.py` would look like this.

````python
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Animesh'
SITENAME = u'Hello World'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_PATHS = ['articles',]
ARTICLE_URL = 'articles/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{slug}.html'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

````

If you remember correctly some of the settings value we had provided during the `pelican-quickstart` commands, like

* `AUTHOR`
    - This is the name of the site author which we had entered during the questions asked.
* `SITENAME` 
    - This is the Name of the site which we provided.
* `SITEURL`
    - Since we still do not have domain name registered, we had kept this empty, and also it make sense to keep this empty for `localhost` testing.
* `PATH`
    - `content ` where we write our blog is the default path set.
* `TIMEZONE`
    - This we had entered during the initial process, and in future if we want to change this we can change this settings.
* `DEFAULT_LANG`
    - This was also entered during the `pelican-quickstart` process.
* `FEEDS_*`
    - All the `FEEDS_*` related settings are empty because we have still not configured the RSS feeds settings, this we will change in future.
* `ARTICLE_*`
    - This is the settings which we modified for keeping the path of the post into one folder.
* `LINKS`
    - This is a tuple of tuple, with each entry showing a links which you want provide in you blog.
* `SOCIAL`
    - This is also a tuple of tuple, were each entry is meant to point to a name of a social network say `Facebook` and the link to your profile.
* `DEFAULT_PAGINATION`
    - This is a number showing how many blogs should be listed on the front page. Some Themes use this setting for some other purposes.

Now these settings are not fully exhaustive, Pelican has a huge list of setting, which we will revisit once we have the need of them.


## publishconf.py ##

Unlike `pelicanconf.py`, this setting file is only used when we are supposed to publish our blog to the domain hosting. This configuration is accessed when we generate the site using the following commands.

````shell
pelican content -s publishconf.py
````

The basic content of these files look like this.

````python
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = ''
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""

````

This file, basically build on top of the `pelicanconf.py`, as we can see from this line, `from pelicanconf import *`. What this means is all the configuration from `pelicancongf.py` is taken into consideration along with some specific configuration which is required for just publishing.

If you see this setting most of them are empty which we will fill one by one as we make progress in our blog, but from the structure you might get an idea that this file pertains to its integraton with the `DISQUS` comment system, and the `GOOGLE_ANALYTICS` code. We will see the use of this code once we integrate these feature into our blog.

## Reference ##

* [Pelican Settings](http://docs.getpelican.com/en/stable/settings.html)
