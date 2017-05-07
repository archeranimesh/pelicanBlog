Title: Expressing the content with Pelican Themes.
Date: 2017-05-07 22:35:15
Modified: 2017-05-08 00:10:47
Category: Pelican
Tags: pelican
Slug: expressing-with-pelican-themes
Author: Animesh Bhadra
subtitle: Expand Horizon
Summary: We will customize of the very popular themes, Elegant, and make it to suit our need and also integrate with the plugins required for Elegant to work.
keywords: Elegant Theme, Pelican Themes, Pelican Plugins.

We have already discussed about Pelican Themes and Plugins to support them in this [blog]({filename}customizing-pelican-blog-with-plugin-and-themes.md). We have seen the comparison between the various popular themes. [Elegant ](http://oncrashreboot.com/elegant-best-pelican-theme-features) is our choice of Themes, for the search functionality which it provides and the minimalistic concepts.

## Integrating the Theme ##

We have already created folder named `plugins` and `themes`, which are clone of the Pelican Plugins and Themes repository. If we see the directory listing inside `themes` folder we fill find different folders with distinguished names, These are the themes name. 

To use any of the themes in this folder we have to add this pelican settings in the `pelicanconf.py`.

````python
THEME = 'themes/elegant'
````

Follow the commands to generate the site and launch the site, and you have your new themes applied.

````shell
pelican content
cd output/
python -m pelican.server
````

## Next Step. ##

There is a completed tutorials on the various configuration available in [Elegant ](http://oncrashreboot.com/elegant-best-pelican-theme-features "Elegant Themes "), follow this.

I have mentioned whatever have not worked for me when using the above themes. 


## Issues when using Elegant ##

[Elegant ](http://oncrashreboot.com/elegant-best-pelican-theme-features "Elegant Themes "), comes its own handicap and hidden information necessary to get the full power of this themes. I am listing some of the issues which I have faced.

### Integration of favicon.ico with Elegant ###

`favicon.ico` did not worked out of the box as suggested in the blog post 

* [Elegant | favicon ](http://oncrashreboot.com/elegant-best-pelican-theme-features#favicon-and-speed-dial-icon "Elegant Themes Favicon "). 


The reason for this is, in this template file `../themes/elegant/templates/_includes/favicon_links.html`, the templates looks for the `favicon.ico` only if `USE_SHORTCUT_ICONS` is defined as `True ` in the `pelicanconf.py`.

Add this line into `pelicanconf.py`, 

````python
USE_SHORTCUT_ICONS=True
````


### Integration of Tipue Search with Elegant ###

* [Elegant | favicon ](http://oncrashreboot.com/elegant-best-pelican-theme-features#search "Elegant Themes search "). 

The process for the integration of Tipue Search, or any of these feature requires plugins.

* Tipue Search
* Table of Content
* Sitemap.

#### Plugin Integration ####

The process to integrate any of the above plugin is the same. We will see how to integrate the Tipue Search.

* Tipue Search, requires BeautifulSoup for its functionality to work, so install BeautifulSoup
    - `pip install beautifulsoup4`
        + This is an additional task required to be done only for Tipue Search.
* The Tipue Search plugin is available in the folder, `plugins/tipue_search/`
* There are two configuration which need to be enabled in `pelicanconf.py`
    - `PLUGIN_PATHS = ['plugin']`
        + This tells the root folder of the `plugin`, since we had cloned the plugins repository to this folder we gave this path.
    * `PLUGINS = ['tipue_search']`
        - This python list gets appended by the folder name of the plugins which we want to add.
* There might be some plugin specific setting which needs to be added, just check the individual plugins git repository.

We have followed the above process, we built our content, but still the search does not work. The reason is few configuration which needs to be enabled in `pelicanconf.py`

* `DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))`
    - This is required to add the default `search ` HTML page into the `output` folder.
    - After this change the search will give the listing.
* Tipue search return undefined url
    - This problem is still not solved, a pull request is present [Tipue search return undefined url ](https://github.com/talha131/pelican-elegant/issues/147 "Tipue search return undefined url"), but this has not been merged.
    - To solve the issue, we have to modify the plugin manually as mentioned in the [pull request](https://github.com/getpelican/pelican-plugins/pull/873/files "Tipue search return undefined url")


