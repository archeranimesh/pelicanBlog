Title: Cost effective blogging with Pelican and Github
Date: 2017-04-25 23:20:03
Modified: 2017-05-02 23:07:42
Category: Pelican
Tags: pelican
Slug: cost-effective-blogging-with-Pelican-and-Github
Author: Animesh Bhadra
subtitle: The easy way.
Summary: This is a series of blog post to help set up a static blog at minimal cost and integrating with Google Analytics, MailChimp, Disqus, Google Adsense. This will be the one stop place to find all the details for setting up a beginner level blog.
keywords: pelican, Google Analytics, MailChimp, Disqus, Google Adsense, Github

[TOC]

This is a series of blog post to help set up a static blog at minimal cost and integrating with all the popular tools such as Google Analytics, MailChimp, Disqus, Google Adsense. This will be the one stop place to find all the details for setting up a beginner level blog.

I am a novice blogger and this blog would act as a journal, which will document my approach towards blogging, software development. The idea is to generate some revenues out of this blog in the long run. We all might have read about so many blogs which are able to generate good amount of traffic but in none one of those we have never read how do they achieve it.

I may fail in my attempt, which might work as a guidance for someone to not follow this path and try another path for the same goal. The background theme to support this is to minimize my cost to the bare minimum so that the failure does not hurt me financially.

## Why Static Blog? ##
There are already a lot of literature present behind this, just wanted to summarize those:-

* **Cost:-** This was the deciding factor for me, because of using a static website, this complete website can be hosted and deployed by just registering a domain name with a provider. I do not have to go for any hosting services etc.
* **Easy of Writing Content:-** I wanted to write my content using just [Markdown](https://daringfireball.net/projects/markdown/), as i have grown comfortable writing in markdown. With using a static blog this was possible.
* **Hosting:-** We can serve these static HTML pages practically from any place, be it [Github](https://github.com/), [Amazon S3](https://aws.amazon.com/s3/), [Dropbox](https://www.dropbox.com/) or any other place which can serve static HTML pages. I have chosen Github just to save the cost.
* **Easy workFlow:-** The work flow is very simple when deploying with static blogs, just right you content in markdown, generate HTML, push your changes to github and that's it. Your content is not available online. You can even go crazy you cam automate the whole thing other than writing content.

The above three are the main reason for choosing static blogs, but there could be many more valid reason for choosing static blogs. Most of the reason for me was personal in nature so you can also choose accordingly.

## Why Pelican? ##
Once the approach to make this blog as static was finalized, the next big question came was which technology to choose, [Pelican ](https://blog.getpelican.com/) or [Jerkll ](https://jekyllrb.com/). There as already many comparison already available among these, but the only reason for me to choose pelican was because it uses python and jinja. In some near future I want to fully customize my blog with the knowledge of these two.

## Why Github? ##
The final decision to be taken before starting this blog was to finalize the hosting provider. We have already mentioned some popular choice are

* [Github](https://github.com/)
* [Amazon S3](https://aws.amazon.com/s3/)
* [Dropbox](https://www.dropbox.com/)

I chose Github, for its near zero cost, it may cost you if you want to keep your repository private else it is completely free were as Amazon S3 would have required to shell out some money though less, with some extra benefits, but for the time being when I am just measuring the water it made sense to keep my cost down.


Once all the above 3 moral questions were answered, setting up the blogs was easy and which will be documented in the future.

## Collated Blog post. ##

* [How to setup Anaconda Python environment for Pelican Blog.]({filename}python-setup-for-pelican-blog.md)


## Reference ##

* [Making a Static Blog with Pelican ](http://nafiulis.me/making-a-static-blog-with-pelican.html)
    - This above blog explains why a static blog generator is good.
* [Moving Blogs to Pelican ](http://arunrocks.com/moving-blogs-to-pelican/)
    - This blog has a terrific explanation for pelican vs jekyll.
* [Amazon S3 Vs Github Pages](https://discuss.gohugo.io/t/hosting-amazon-s3-vs-github-gh-pages-vs/340)
    - This explains the benefits of Amazon S3 over Github Pages, kindly check if you are affected because of this.
