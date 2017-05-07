Title: Expressing the content with Pelican Themes.
Date: 2017-05-07 22:35:15
Modified: 2017-05-07 22:50:01
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
