Title: Expressing the content with Pelican Themes.
Date: 2017-05-07 22:35:15
Modified: 2017-05-09 23:38:17
Category: Pelican
Tags: pelican
Slug: expressing-with-pelican-themes
Author: Animesh Bhadra
subtitle: Expand Horizon
Summary: We will customize of the very popular themes, Elegant, and make it to suit our need and also integrate with the plugins required for Elegant to work.
keywords: Elegant Theme, Pelican Themes, Pelican Plugins.

[TOC]

We have already discussed about Pelican Themes and Plugins in this [blog]({filename}customizing-pelican-blog-with-plugin-and-themes.md "Customizing Pelican Blog with plugin and themes"). 

We have also seen the comparison between the various popular themes. [Elegant ](http://oncrashreboot.com/elegant-best-pelican-theme-features "Comparison between different themes.") is our choice of Themes because of search functionality which it provides along with the minimalist concepts.

We will first focus on how we can integrate one particular themes and also one particular plugins which will give us a fair amount of idea on how to integrate different plugins.

## Integrating the Elegant Theme ##

We have already created folder named `plugins` and `themes`, which are clone of the Pelican [Plugins](https://github.com/getpelican/pelican-plugins "Pelican Plugins ") and [Themes](https://github.com/getpelican/pelican-themes "Pelican Themes ") repository. If we see the directory listing inside `themes` folder we fill find different folders with distinguished names, these are the themes name. 

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

## Integrating A Plugin into Pelican ##

The process to integrate any plugin is also similar to integrating Themes. If we see inside the `plugins` directory which we had cloned, we will find a lot of different folder name just like in `themes` directory. Each of these name is a `plugin` name.

To integrate a plugin into Pelican we have to add these 2 configuration into the `pelicanconf.py` file.

````python
PLUGIN_PATHS = ['plugin']   # Name of the directory where plugin are kept.
PLUGINS = ['sitemap']       # Name of the particular plugin inside the directory.
````

In the above code sample, we can see we have integrated the `sitemap` plugin, and as per the [documentation](https://github.com/getpelican/pelican-plugins/tree/master/sitemap "Sitemap Plugin "), this generates a Sitemap which we generally submit it to some Webmaster tools. 

Likewise, if we want to integrate any other `plugins`, we have just add it to the list variable `PLUGINS` along with the settings required for that plugins defined in its documentation.



## References ##

* [Elegant ](http://oncrashreboot.com/elegant-best-pelican-theme-features "Elegant Themes")
* [Pelican Plugins](https://github.com/getpelican/pelican-plugins "Pelican Plugins ")
* [Pelican Themes](https://github.com/getpelican/pelican-themes "Pelican Themes ")
* [Sitemap Documentation](https://github.com/getpelican/pelican-plugins/tree/master/sitemap "Sitemap Documentation "),

