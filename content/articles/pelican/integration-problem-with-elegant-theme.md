Title: Problem Faced when integrating with Elegant Themes.
Date: 2017-05-09 22:55:40
Modified: 2017-05-10 22:42:42
Category: Pelican
Tags: pelican
Slug: integration-problem-with-elegant-theme
Author: Animesh Bhadra
subtitle: Surprise.
Summary: Elegant was my theme choice, and while integrating this theme with my blog I found that a lot of things does not work out of the box, and some changes are required in the themes itself. I am listing these changes here, if this are still unresolved in the future.
keywords: favicon.ico not displayed with Elegant, Tipue search return undefined URL, Tipue Search not working, TOC format changes.

[TOC]

Elegant was my theme choice, and while integrating this theme with my blog I found that a lot of things does not work out of the box, and some changes are required in the themes itself. I am listing these changes here, if this are still unresolved in the future.

[Elegant ](http://oncrashreboot.com/elegant-best-pelican-theme-features "Elegant theme"), requires a lot of different plugins to make it work the way it was designed. If you see the documentation on the above link, it does not mention the important plugins which are required to make it work, it just provides an explanation on the feature.

In this blog post I am listing down the issues which I faced while integrating the Elegant themes.

## favicon.ico not displayed with Elegant  ##

If you read the [documentation ](http://oncrashreboot.com/elegant-best-pelican-theme-features#favicon-and-speed-dial-icon "Favicon Integration Elegant") on how to enable `favicon.ico` for Elegant themes, the process is pretty straight forward, just place the icons into this directory `content/theme/images`, and define `STATIC_PATHS` with `STATIC_PATHS = ['theme/images', 'images']`.

If you follow the above process then most probably you will still not be getting the `favicon.ico`, the reason being there is one more configuration which needs to enabled in `pelicanconf.py` in addition to above two.

````python
STATIC_PATHS = ['theme/images', 'images']
USE_SHORTCUT_ICONS=True
````

The reason for this is, the links for including `favicon` are generated in this template `themes/elegant/templates/_includes/favicon_links.html`, and the link generation is under a configuration named `USE_SHORTCUT_ICONS`, so until we make it `True ` the links will not be generated.


## Issues while integrating Tipue Search ##

### Prerequisite ###

[Tipue Search plugin ](https://github.com/getpelican/pelican-plugins/tree/master/tipue_search. "Tipue Search plugin ") integration is little different from other plugin.

This plugin has an external dependency on `BeautifulSoup`, we have to install this python package first in our environment `pelican1`

````shell
pip install beautifulsoup4
````

We have to add this plugin name into `pelicanconf.py`

````python
PLUGINS = ['sitemap', 'tipue_search']
````

When we build our blog after this we should see our search functionality working, but we see 2 issues.

* Search Result are not displayed.
* Tipue search return undefined URL.

### Search Result are not displayed ###

Elegant uses some predefined HTML pages to render few of its content, `search ` functionality is based on one such file, so we have to provide that in the `pelicanconf.py`

````python
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))
````

When we do this changes we will see the search result getting listed, but on clicking those link it will redirect to an undefined URL.

### Tipue search return undefined URL. ###

When we click on the Search result, we get the URL as undefined, this issues is still not solved, there is already a pull request pending on the Github.

Kindly visit these two links for more details.
* [Tipue search return undefined url ](https://github.com/talha131/pelican-elegant/issues/147 "Tipue search return undefined url").
* To solve the issue, we have to modify the plugin manually as mentioned in the [pull request](https://github.com/getpelican/pelican-plugins/pull/873/files "Tipue search return undefined url")
    - Change the file in `plugins/tipue_search/tipue_search.py`, line no 61 add this code `'loc': page_url`

## TOC Integration with Elegant ##

Elegant theme has a side bar with the Table of Content of the blog post displayed. This is also achieved based on a plugin named `extract_toc`.

We have to add this into the `pelicanconf.py`

````python
PLUGINS = ['sitemap', 'tipue_search', 'extract_toc']
````

There is also a Markdown settings which we have to update in the same file like this.

````python
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.toc' :{'permalink' : 'true'}
    }
}
````

In addition to the above changes, every blog post after the file meta-data section should have an entry named `[TOC]`


## Syntax Highlighting  ##

When writing a technical blog we might be interested in syntax highlighting of the code we write, we can achieve this with following configuration in `pelicanconf.py`

````python
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc' :{'permalink' : 'true'},

    },
    'output_format': 'html5',
}

````

## Next and Previous Articles. ##

When we read the documentation of [Elegant Next and Previous Articles](http://oncrashreboot.com/elegant-best-pelican-theme-features#next-and-previous-articles), it clearly states that we do not require any additional plugins for this feature, but it does not work out of the box.

We have to integrate the `neighbors` plugins and then it works. Now we will have these in our `pelicanconf.py`

````python
PLUGINS = ['sitemap', 'tipue_search', 'extract_toc', 'neighbors']
````

## References ##

* [Elegant ](http://oncrashreboot.com/elegant-best-pelican-theme-features "Elegant theme")
    - Kindly read this documentation for other configuration which gives more flexibility in terms of the themes like Article Subtitle, Add License to your Site etc.
* [pelicanconf of oncrashreboot blog](https://github.com/talha131/onCrashReboot/blob/master/pelicanconf.py)
    - Visit this configuration file for any doubts on the setting of elegant theme.
* [Favicon documentation ](http://oncrashreboot.com/elegant-best-pelican-theme-features#favicon-and-speed-dial-icon "Favicon Integration Elegant")
* [Tipue Search plugin ](https://github.com/getpelican/pelican-plugins/tree/master/tipue_search. "Tipue Search plugin ")
* [Tipue search return undefined url ](https://github.com/talha131/pelican-elegant/issues/147 "Tipue search return undefined url").
* [Tipue search return undefined url pull request](https://github.com/getpelican/pelican-plugins/pull/873/files "Tipue search return undefined url")
