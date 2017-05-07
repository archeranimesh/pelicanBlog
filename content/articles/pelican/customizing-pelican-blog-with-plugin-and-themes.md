Title: Customizing Pelican blog with the help of Plugin and themes
Date: 2017-05-03 23:05:51
Modified: 2017-05-07 22:56:29
Category: Pelican
Tags: pelican
Slug: customizing-pelican-blog-with-plugin-and-themes
Author: Animesh Bhadra
subtitle: Eternal Customization
Summary: Pelican blog has an active community of developers who are always at the look out to modify and enhance the power of Pelican blog. Pelican plugin and Themes are one way of doing the same.
keywords: Pelican themes, Pelican plugins, Flex Vs Elegant vs BootStrap3 Themes.

[TOC]

Pelican Blogs gives its user the full power to customize to the want of the user. We have been using the default themes and default setting provided by Pelican with not much customization and the results are also quite good.

Enhancing the present blog further will require us to use certain Plugins and Themes which will extended the functionality. These are the 2 repository which we should clone into for getting these enhancements.

* [pelican-plugins](https://github.com/getpelican/pelican-plugins "Pelican Plugins ")
    - This is the repository for the plugins.
    - `git clone --recursive https://github.com/getpelican/pelican-plugins.git plugins`
* [pelican-themes ](https://github.com/getpelican/pelican-themes "Pelican Themes")
    - This is the themes repository.
    - `git clone --recursive https://github.com/getpelican/pelican-themes.git themes`


## Plugins Vs Themes ##

The first things which we have to decide is to choose the list of plugins or the Themes we want to use. I would say first decide on Themes and the see what all plugins are required to support these themes. All plugins are not plug able with all the themes.

We have to first start by choosing the themes, and the corresponding plugin required for it. This path is again the easiest as we are already treading the known, when we are comfortable with this integration we can always go ahead and enhance the existing themes and plugins to suit our needs. Till we reach the Jedi stage this precooked solution is the best approach.


## Flex Vs Elegant vs BootStrap3##

When we are deciding on which themes to choose for the blog, broadly the working choice would be 

* [Flex: Responsive Pelican theme ](https://blog.alexandrevicenzi.com/flex-pelican-theme.html "Flex: Responsive Pelican theme ")
* [Elegant Why it is the best Pelican theme ](http://oncrashreboot.com/elegant-best-pelican-theme-features "Elegant Why it is the best Pelican theme")
* [BootStrap3](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3 "BootStrap3")

There are many others, which you are free to explore, but for my blog I had considered these 3 options. Each one has its own pros and cons, the choice was very difficult between these 3, and in future I might even consider jumping ships to the other themes.

Let's discuss some outline of the above 3 themes 

* [Flex: Responsive Pelican theme ](https://blog.alexandrevicenzi.com/flex-pelican-theme.html "Flex: Responsive Pelican theme ")
    - This has out of the box integration with a lot of plugins including [AddThis](http://www.addthis.com/ "AddThis"), which is not available for any other themes.
    - This also has support for Google AdSense, which again is missing in most of the plugin.
    - Actively maintained, the last check-in on its Github repository was on Apr 24, 2017.
    - Tipue_Search is also on the way, there is an open issue on the repository, [Search #49](https://github.com/alexandrevicenzi/Flex/issues/49 "Tipue Search ")
        + This facility of search is the only reason I dropped [Flex ](https://blog.alexandrevicenzi.com/flex-pelican-theme.html "Flex: Responsive Pelican theme ").
* [BootStrap3](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3 "BootStrap3")
    - This is a full hack able implementation of BootStrap3, and will try to use these Themes, once I get my hand dirty enough with the modern CSS and Web Technologies.
* [Elegant Why it is the best Pelican theme ](http://oncrashreboot.com/elegant-best-pelican-theme-features "Elegant Why it is the best Pelican theme")
    - I chose this theme just for its minimalist design and search feature.
    - It has an integration with MailChimp.
    - This is not an actively managed project, the last commit on this repository was on Sep 8, 2014, which is good 3 years ago.
    - We can use and modify this theme for our satisfaction if a bug is hampering our development.


We have decided on our Themes, the Plugins required for these themes are as below.

* sitemap
* tipue_search
* extract_toc
* neighbors

The standard features and enhancements already available

* Disqus
* Google Analytics
* MailChimp Integration.
* Custom 404 Page.
* Collapsible Comments
* Page and Article Subtitle.


We will not try to see the integration of all the above feature with the Elegant themes.


## Reference ##

* [Elegant Why it is the best Pelican theme ](http://oncrashreboot.com/elegant-best-pelican-theme-features "Elegant Why it is the best Pelican theme")
* [BootStrap3](https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3 "BootStrap3")
* [Flex: Responsive Pelican theme ](https://blog.alexandrevicenzi.com/flex-pelican-theme.html "Flex: Responsive Pelican theme ")
* [pelican-themes ](https://github.com/getpelican/pelican-themes "Pelican Themes")
* [pelican-plugins ](https://github.com/getpelican/pelican-plugins "Pelican Plugins ")

