Title: Home Page feature for Elegant Theme
Date: 2017-05-09 23:53:05
Modified: 2017-05-10 00:15:37
Category: Pelican
Tags: pelican
Slug: home-page-features-elegant-theme
Author: Animesh Bhadra
subtitle: Home Coming  
Summary: Elegant has a nice feature called the Home Page, which provides a About Me combined with information from GitHub on the project someone is working.
keywords: Home Pages, About Me.

[TOC]

Elegant has a nice feature called the Home Page, which provides a About Me combined with information from GitHub on the project someone is working. These feature are again controlled by a configuration.

In place of adding this configuration into `pelicanconf.py` we will create a new file called `elegantconfig.py`, and import this file into `pelicanconf.py` by calling `from elegantConfig import *`. This will make sure all the configuration from `elegantconfig.py` is available while generating the blog.

There are two configuration for the Home Page.

## `LANDING_PAGE_ABOUT` ##


* `LANDING_PAGE_ABOUT`
    - This is a Dictionary with two field `"title"` and `"details"`
        + `"title"` : This gives a heading Home Page.
        + `"details"` : It is the content in HTML which mostly contains the `About Me` description which one wants to provide.
            * One clever way of writing this HTML is, write a about page in markdown, generate the pelican blog with this about page and then right click on the page and select view source, copy the relevant text with the HTML code in it.

## `PROJECTS` ##

* `PROJECTS`
    - This is also a list of Dictionary with these field in each dictionary, and the value of each of these field is a `string ` and not `HTML` in case of `LANDING_PAGE_ABOUT`'s `"details"`
        + `"name"` : The project name which you want to be displayed.
        + `"url"` : The link to the project.
        + `"description"` : The description you want to provide for the project.